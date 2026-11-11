#!/usr/bin/env python3
"""Run the official VNCCS Pose Studio workflow through the ComfyUI web UI.

VNCCS_PoseStudio needs the frontend's live capture at execution time, so we
load the graph in the shared browser (our own tab), set the character image and
the pose preset, queue from the UI, then collect the outputs from disk.

Usage:
    run_vnccs_ui.py --pose crawling [--char /path/to/face.png] [--timeout 900]
    run_vnccs_ui.py --pose "squatting leaning back" --prompt "on a rooftop at night"
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # bundled media_lock.py
try:
    from media_lock import media_lock  # noqa: E402
except ImportError:  # fall back to the shared-machine helper if present
    sys.path.insert(0, os.path.expanduser("~/.openclaw/tools"))
    from media_lock import media_lock  # noqa: E402

# route ④ needs a CDP browser; keep --list-poses usable without one
try:
    sys.path.insert(0, os.path.expanduser("~/.openclaw/tools/browser"))
    from browser_client import connect_sync  # noqa: E402
except ImportError:  # standalone hosts: bundled CDP fallback
    try:
        from browser_fallback import connect_sync  # noqa: E402
    except ImportError:
        connect_sync = None
try:
    from playwright.sync_api import sync_playwright  # noqa: E402
except ImportError:
    sync_playwright = None

# ComfyUI-side paths default to $COMFY (or ~/ComfyUI); override individually if needed
def _find_comfy() -> Path:
    for p in [os.environ.get("COMFY"), "/content/ComfyUI", str(Path.home() / "ComfyUI"), "/root/ComfyUI"]:
        if p and (Path(p) / "main.py").exists():
            return Path(p)
    return Path("/content/ComfyUI") if Path("/content").exists() else (Path.home() / "ComfyUI")

_COMFY = _find_comfy()
WF_FILE = Path(os.environ.get("VNCCS_WF_FILE", str(_PKG_DIR / "workflows" / "VNCCS_PoseStudio_QI2.1.json")))
_default_vnccs_lib = _COMFY / "custom_nodes" / "ComfyUI_VNCCS_Utils" / "PoseLibrary"
if not _default_vnccs_lib.is_dir() and (_PKG_DIR / "pose_library").is_dir():
    _default_vnccs_lib = _PKG_DIR / "pose_library"
VNCCS_LIB = Path(os.environ.get("VNCCS_POSELIB", str(_default_vnccs_lib)))
COMFY_INPUT = Path(os.environ.get("COMFYUI_INPUT", str(_COMFY / "input")))
COMFY_OUTPUT = Path(os.environ.get("COMFYUI_OUTPUT", str(_COMFY / "output")))
def _get_default_out() -> Path:
    env_out = os.environ.get("VNCCS_UI_OUT")
    if env_out:
        return Path(env_out)
    drive_root = os.environ.get("DRIVE_ROOT")
    if not drive_root and Path("/content/drive/MyDrive").is_dir():
        drive_root = "/content/drive/MyDrive/qwen21_pose"
    if drive_root:
        return Path(drive_root) / "outputs" / "vnccs_ui"
    return _PKG_DIR / "outputs" / "vnccs_ui"

OUT = _get_default_out()
VNCCS_LORA = "VNCCS_QI2_PoseStudioV1.1.safetensors"
URL = os.environ.get("COMFYUI_URL", "http://127.0.0.1:8188")

# aliases used by the phase4b runs, kept so old commands still work
LEGACY = {
    "crawling": "Crawling",
    "kneel_side": "Kneeling - Side View",
    "lean_back": "Leaning Back",
    "sit_side": "Sitting - Side View",
}


def _slug(s: str) -> str:
    # Strip leading shot index if present (e.g. '05_bent_toe_touch' -> 'bent_toe_touch')
    cleaned = re.sub(r"^\d+_", "", s.strip())
    return "_".join("".join(ch if ch.isalnum() else " " for ch in cleaned.lower()).split())


def sync_local_poses_to_comfy(target_lib: Path) -> None:
    """Ensure repo's 55 curated poses exist in ComfyUI PoseLibrary/local_user_poses."""
    src = _PKG_DIR / "pose_library" / "local_user_poses"
    if not src.is_dir() or not target_lib.is_dir():
        return
    dst = target_lib / "local_user_poses"
    try:
        dst.mkdir(parents=True, exist_ok=True)
        for item in src.rglob("*.json"):
            rel = item.relative_to(src)
            target = dst / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            if not target.exists() or item.stat().st_size != target.stat().st_size:
                shutil.copy2(item, target)
    except Exception:
        pass


def build_pose_index() -> dict[str, Path]:
    """Index every pose JSON across repository bundled poses and VNCCS PoseLibrary.

    Keys: "<repo_slug>/<category_slug>/<pose_slug>" for every pose, plus a bare
    "<pose_slug>" alias when that name is unique across the library (9 pose names
    such as "Standing A" exist in more than one repository).
    """
    idx: dict[str, Path] = {}
    counts: dict[str, int] = {}

    # Auto-sync local poses to ComfyUI's VNCCS directory if available
    comfy_lib = _COMFY / "custom_nodes" / "ComfyUI_VNCCS_Utils" / "PoseLibrary"
    if comfy_lib.is_dir():
        sync_local_poses_to_comfy(comfy_lib)
    if VNCCS_LIB.is_dir() and VNCCS_LIB.resolve() != comfy_lib.resolve():
        sync_local_poses_to_comfy(VNCCS_LIB)

    search_dirs: list[Path] = []
    # 1. Package bundled poses (always available, 55 curated poses)
    pkg_lib = _PKG_DIR / "pose_library"
    if pkg_lib.is_dir():
        search_dirs.append(pkg_lib)

    # 2. ComfyUI custom node pose library (remote repos + custom user poses)
    if comfy_lib.is_dir() and not any(d.resolve() == comfy_lib.resolve() for d in search_dirs):
        search_dirs.append(comfy_lib)

    # 3. Environment or custom VNCCS_POSELIB
    if VNCCS_LIB.is_dir() and not any(d.resolve() == VNCCS_LIB.resolve() for d in search_dirs):
        search_dirs.append(VNCCS_LIB)

    for lib_dir in search_dirs:
        for p in sorted(lib_dir.rglob("*.json")):
            s = p.as_posix()
            if "/poses/" not in s and "/local_user_poses/" not in s:
                continue
            try:
                rel = p.relative_to(lib_dir).parts
            except ValueError:
                continue
            repo, category, name = _slug(rel[0]), _slug(rel[1]), _slug(p.stem)
            if category == "poses":  # local_user_poses nests one level shallower
                category = _slug(rel[2])
            key = f"{repo}/{category}/{name}"
            if key not in idx:
                idx[key] = p
                counts[name] = counts.get(name, 0) + 1

    for key, path in list(idx.items()):
        if key.count("/") != 2:
            continue
        name = key.rsplit("/", 1)[1]
        if counts.get(name) == 1:
            idx[name] = path

    for alias, stem in LEGACY.items():
        for key, path in idx.items():
            if key.count("/") == 2 and key.rsplit("/", 1)[1] == _slug(stem):
                idx.setdefault(alias, path)
                break
    return idx


def resolve_pose(name: str, idx: dict[str, Path]) -> Path:
    if name in idx:
        return idx[name]
    key = _slug(name)
    if key in idx:
        return idx[key]
    hits = sorted({p for k, p in idx.items() if key in k or k in key})
    if len(hits) == 1:
        return hits[0]
    if not hits:
        # Token-based subset matching (e.g. "bent toe touch" -> "bent over toe touch profile")
        tokens = set(key.split("_"))
        token_hits = sorted({
            p for k, p in idx.items()
            if tokens.issubset(set((k.rsplit("/", 1)[1] if "/" in k else k).split("_")))
        })
        if len(token_hits) == 1:
            return token_hits[0]
        if not token_hits:
            raise KeyError(f"unknown pose '{name}' — run with --list-poses to see the {len(idx)} available poses")
        hits = token_hits
    raise KeyError(f"pose '{name}' is ambiguous: {[p.stem for p in hits][:6]} — disambiguate with <repo>/<category>/<name>")


def prep_workflow(pose_json: str, char_name: str, prefix: str, user_prompt: str = "") -> dict:
    wf = json.loads(WF_FILE.read_text(encoding="utf-8"))
    by_id = {n["id"]: n for n in wf["nodes"]}

    # drop the rgthree comparer (only a viewer node; its inputs are decorative here)
    drop = [nid for nid, n in by_id.items() if n["type"].startswith("Image Comparer")]
    wf["nodes"] = [n for n in wf["nodes"] if n["id"] not in drop]
    wf["links"] = [l for l in wf["links"] if l[1] not in drop and l[3] not in drop]

    # character image + save prefix on the existing LoadImage / SaveImage nodes
    for n in wf["nodes"]:
        if n["type"] == "LoadImage" and isinstance(n.get("widgets_values"), list):
            n["widgets_values"][0] = char_name
        if n["type"] == "SaveImage" and isinstance(n.get("widgets_values"), list):
            n["widgets_values"][0] = prefix
        if n["type"] == "VNCCS_PoseStudio" and isinstance(n.get("widgets_values"), list):
            value = pose_json
            if user_prompt:
                # The frontend rebuilds the capture prompt from the scene document's
                # export block (prompt_template "Draw character from image2\n
                # <lighting>\n<user_prompt>"), where <user_prompt> comes from the
                # per-pose prompt. Library pose files carry empty prompt/pose_prompts
                # fields and no export block, so set all three hydration paths:
                # pose.prompt (per-tab), pose_prompts[0] (hydrated array) and
                # export.user_prompt (legacy global default).
                scene = json.loads(pose_json)
                scene["prompt"] = user_prompt
                scene["pose_prompts"] = [user_prompt]
                try:
                    export = dict(json.loads(n["widgets_values"][0]).get("export") or {})
                except (TypeError, ValueError):
                    export = {}
                export["user_prompt"] = user_prompt
                scene["export"] = export
                value = json.dumps(scene)
            n["widgets_values"][0] = value
        if n["type"] == "LoraLoaderModelOnly" and isinstance(n.get("widgets_values"), list):
            n["widgets_values"][0] = VNCCS_LORA
    return wf


def find_new_outputs(prefix: str, since: float) -> list[Path]:
    hits = []
    seen = set()
    search_dirs = [COMFY_OUTPUT, _COMFY / "output", Path("/content/ComfyUI/output"), Path("/root/ComfyUI/output")]
    for sdir in search_dirs:
        if not sdir.exists():
            continue
        for p in sdir.rglob(f"{prefix}*.png"):
            if p in seen:
                continue
            seen.add(p)
            try:
                if p.stat().st_mtime >= since - 1:
                    hits.append(p)
            except OSError:
                pass
    return sorted(hits)


def settle(page, ms: int) -> None:
    """Sleep without relying on the CDP channel staying idle."""
    end = time.time() + ms / 1000.0
    while time.time() < end:
        time.sleep(0.5)
        try:
            page.evaluate("1")
        except Exception:
            pass


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pose", default="crawling",
                    help="pose name/slug from the PoseLibrary (see --list-poses)")
    ap.add_argument("--char", default=str(_PKG_DIR / "references" / "src_standing.png"))
    ap.add_argument("--prompt", default="",
                    help="scene prompt for the capture: sets the pose prompt + export.user_prompt (overrides the workflow default)")
    ap.add_argument("--timeout", type=int, default=1800)
    ap.add_argument("--out", default=None, help=f"output directory for generated images (defaults to {OUT})")
    ap.add_argument("--list-poses", action="store_true", help="print all available pose names and exit")
    a = ap.parse_args()

    idx = build_pose_index()
    if a.list_poses:
        for slug, path in sorted(idx.items()):
            print(f"{slug}\t{path}")
        counts = sum(1 for k in idx if k.count("/") == 2)
        print(f"# {counts} poses (bare aliases not counted)", file=sys.stderr)
        if counts == 0:
            print(f"# nothing under {VNCCS_LIB} — set VNCCS_POSELIB or $COMFY (see install/setup.md §0/§4)",
                  file=sys.stderr)
        return 0
    if connect_sync is None or sync_playwright is None:
        print("ERROR: route ④ needs a CDP browser client and playwright; install playwright "
              "(`pip install playwright && playwright install chromium`) or keep the OpenClaw "
              "adapter at ~/.openclaw/tools/browser/browser_client.py", file=sys.stderr)
        return 2
    try:
        pose_path = resolve_pose(a.pose, idx)
    except KeyError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    tag = _slug(a.pose)  # filesystem-safe tag for output names
    out_dir = Path(a.out) if a.out else OUT
    out_dir.mkdir(parents=True, exist_ok=True)
    char_src = Path(a.char)
    if not char_src.exists():
        print(f"ERROR: character not found: {char_src}", file=sys.stderr)
        return 1
    char_name = char_src.name
    # Copy to all potential ComfyUI input locations
    for inp in [COMFY_INPUT, _COMFY / "input", Path("/content/ComfyUI/input"), Path("/root/ComfyUI/input")]:
        try:
            inp.mkdir(parents=True, exist_ok=True)
            shutil.copy2(char_src, inp / char_name)
        except Exception:
            pass

    pose_json = pose_path.read_text(encoding="utf-8")
    # unique prefix per run — never clobber a previous result
    stamp = int(time.time())
    prefix = f"poselab/vnccs_ui_{tag}_{stamp}"
    wf = prep_workflow(pose_json, char_name, prefix, a.prompt)

    with media_lock(exclusive=False, wait_timeout=a.timeout + 300):
      with sync_playwright() as pw:
        browser = connect_sync(pw)
        page = browser.contexts[0].new_page()
        logs: list[str] = []
        try:
            page.on("console", lambda m: logs.append(f"{m.type}: {m.text}"))
            page.on("pageerror", lambda e: logs.append(f"pageerror: {e}"))
            def _on_resp(r):
                if "/prompt" in r.url and r.status >= 400:
                    try:
                        logs.append(f"HTTP {r.status} /prompt: {r.text()[:1500]}")
                    except Exception as e:
                        logs.append(f"HTTP {r.status} /prompt body unreadable: {e}")
            page.on("response", _on_resp)
        except Exception:
            pass
        try:
            page.goto(URL, timeout=45000)
            print(f"[vnccs-ui] waiting for ComfyUI web frontend to initialize at {URL}...")
            try:
                page.wait_for_function("""() => {
                    if (window.app && typeof window.app.loadGraphData === 'function') return true;
                    if (window.comfyAPI && window.comfyAPI.app && window.comfyAPI.app.app && typeof window.comfyAPI.app.app.loadGraphData === 'function') {
                        window.app = window.comfyAPI.app.app;
                        return true;
                    }
                    return false;
                }""", timeout=60000)
            except Exception as wait_err:
                print(f"[vnccs-ui] ERROR: Timed out waiting for ComfyUI web app to initialize: {wait_err}", file=sys.stderr)
                if logs:
                    print("[vnccs-ui] Browser console / error logs tail:", file=sys.stderr)
                    for log_line in logs[-15:]:
                        print(f"    {log_line}", file=sys.stderr)
                return 2
            settle(page, 2000)
            page.evaluate("(wf) => window.app.loadGraphData(wf)", wf)
            settle(page, 3000)
            # drop QwenImage21Cache (aimdo error on this box) and wire LoRA -> KSampler
            page.evaluate("""() => {
                const g = window.app.graph;
                const nodes = g._nodes;
                const lora = nodes.find(n => n.type === 'LoraLoaderModelOnly');
                const ks = nodes.find(n => n.type === 'KSampler');
                const cache = nodes.find(n => n.type === 'QwenImage21Cache');
                if (lora && ks) {
                    const slot = ks.inputs.findIndex(i => i.name === 'model');
                    lora.connect(0, ks, slot);
                }
                if (cache) g.remove(cache);
                return true;
            }""")
            settle(page, 1500)
            # also persist the rendered pose figure (doll) for comparison
            page.evaluate("""(prefix) => {
                try {
                    const g = window.app.graph;
                    const ps = g._nodes.find(n => n.type === 'VNCCS_PoseStudio');
                    if (!ps || !window.LiteGraph) return false;
                    const sv = window.LiteGraph.createNode('SaveImage');
                    sv.widgets[0].value = prefix;
                    g.add(sv);
                    ps.connect(0, sv, 0);
                    return true;
                } catch (e) { return 'ERR:' + e.message; }
            }""", f"poselab/vnccs_ui_doll_{tag}_{stamp}")
            # confirm widgets landed
            info = page.evaluate("""() => {
                const g = window.app.graph._nodes || [];
                const li = g.find(n => n.type === 'LoadImage');
                const ps = g.find(n => n.type === 'VNCCS_PoseStudio');
                const liWidget = li && li.widgets ? li.widgets.find(w => w && w.name === 'image') : null;
                const psWidget = ps && ps.widgets ? ps.widgets.find(w => w && w.name === 'pose_data') : null;
                return {
                    nodes: g.length,
                    hasVnccsNode: !!ps,
                    loadImage: liWidget ? liWidget.value : null,
                    poseLen: psWidget && psWidget.value ? String(psWidget.value).length : null,
                };
            }""")
            print(f"[vnccs-ui] graph: {info}")
            if not info.get("hasVnccsNode") or info.get("poseLen") is None:
                print("ERROR: VNCCS_PoseStudio custom node is missing or not loaded in ComfyUI!\n"
                      "  -> Please install it: git clone https://github.com/AHEKOT/ComfyUI_VNCCS_Utils custom_nodes/ComfyUI_VNCCS_Utils\n"
                      "  -> And restart ComfyUI once.", file=sys.stderr)
                return 2
            page.screenshot(path=str(out_dir / f"_ui_{tag}_loaded.png"))

            t0 = time.time()
            page.evaluate("() => window.app.queuePrompt()")
            print("[vnccs-ui] queued from UI; waiting for outputs...")
            deadline = time.time() + a.timeout
            got: list[Path] = []
            while time.time() < deadline:
                settle(page, 5000)
                got = find_new_outputs(prefix, t0)
                if got:
                    break
            if not got:
                page.screenshot(path=str(out_dir / f"_ui_{tag}_timeout.png"))
                print("[vnccs-ui] TIMEOUT; console tail:")
                for line in logs[-12:]:
                    print("   ", line)
                return 1
            settle(page, 2000)
            saved: list[str] = []
            for i, p in enumerate(got, 1):
                dst = out_dir / f"result_{tag}{('' if i == 1 else f'_{i}')}.png"
                shutil.copy2(p, dst)
                saved.append(dst.name)
                print(f"[vnccs-ui] saved {dst.name} ({p.name})")

            # Also capture the pose figure (doll) saved by LiteGraph
            doll_prefix = f"poselab/vnccs_ui_doll_{tag}_{stamp}"
            doll_got = find_new_outputs(doll_prefix, t0)
            if not doll_got:
                doll_got = find_new_outputs(f"vnccs_ui_doll_{tag}_{stamp}", t0)
            for i, p in enumerate(doll_got, 1):
                dst_doll = out_dir / f"doll_{tag}{('' if i == 1 else f'_{i}')}.png"
                try:
                    shutil.copy2(p, dst_doll)
                    saved.append(dst_doll.name)
                    print(f"[vnccs-ui] saved pose doll: {dst_doll.name} ({p.name})")
                except Exception as e:
                    print(f"[vnccs-ui] could not copy pose doll: {e}", file=sys.stderr)

            page.screenshot(path=str(out_dir / f"_ui_{tag}_done.png"))
        finally:
            page.close()
    (out_dir / f"{tag}_{stamp}.meta.json").write_text(json.dumps({
        "pose": a.pose, "resolved": str(pose_path), "char": char_name,
        "comfy_prefix": prefix, "seconds": round(time.time() - t0, 1),
        "outputs": saved, "lora": VNCCS_LORA,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    # Auto-sync to Google Drive if standalone run
    drive_root = os.environ.get("DRIVE_ROOT")
    if not drive_root and Path("/content/drive/MyDrive").is_dir():
        drive_root = "/content/drive/MyDrive/qwen21_pose"
    if drive_root:
        try:
            drive_dst = Path(drive_root) / "outputs" / "vnccs_ui"
            if not str(out_dir.resolve()).startswith(str(Path(drive_root).resolve())):
                drive_dst.mkdir(parents=True, exist_ok=True)
                for f_name in saved + [f"{tag}_{stamp}.meta.json", f"_ui_{tag}_done.png"]:
                    src_f = out_dir / f_name
                    if src_f.exists():
                        shutil.copy2(src_f, drive_dst / src_f.name)
                print(f"[vnccs-ui] 💾 已自动同步至 Google Drive: {drive_dst}")
        except Exception as e:
            print(f"[vnccs-ui] drive sync warning: {e}", file=sys.stderr)

    print("[vnccs-ui] done")
    return 0


if __name__ == "__main__":
    sys.exit(main())
