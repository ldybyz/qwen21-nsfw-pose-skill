#!/usr/bin/env python3
"""One-shot Google Colab runner: setup + ComfyUI + one T2I generation.

Merges the step-by-step notebook (notebooks/colab_t4.ipynb) into a single,
re-runnable script. Every step is idempotent: existing files are skipped, an
already running ComfyUI is reused, so re-running only costs the generation.

Google Drive must be mounted from a notebook cell first (drive.mount cannot be
called from a plain script):

    from google.colab import drive; drive.mount("/content/drive")
    !python scripts/colab_quickstart.py --steps 20

Drive layout (DRIVE_ROOT/{models,loras,outputs}):
    models/   base-model cache (copied to the local disk before loading)
    loras/    LoRA files (put them here, or pass --lora-url to download once)
    outputs/  generated images + .json metadata

Only the Python standard library is used. Linux (Colab) only.
"""
from __future__ import annotations

import argparse
import datetime
import os
import shutil
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

PKG_DIR = Path(__file__).resolve().parent.parent
HF_BASE = "https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main"
BASE_MODELS = [
    ("diffusion_models", "qwen_image_2.1_int8_convrot.safetensors"),
    ("text_encoders", "qwen3vl_8b_int8_convrot.safetensors"),
    ("vae", "qwen_image_2.1_vae_bf16.safetensors"),
]
DEFAULT_LORA = "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors"
COMFY_PORT = 8188


def log(msg: str) -> None:
    print(f"[colab] {msg}", flush=True)


def die(msg: str) -> None:
    print(f"[colab] ERROR: {msg}", file=sys.stderr, flush=True)
    sys.exit(1)


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, **kw)


def atomic_copy(src: Path, dst: Path) -> None:
    """Copy via a .part file so an interrupted copy is never mistaken for a finished one."""
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".part")
    shutil.copyfile(src, tmp)
    os.replace(tmp, dst)


def download(url: str, dst: Path, headers: list[str] | None = None) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_name(dst.name + ".part")
    cmd = ["wget", "-c", "-q", "--show-progress", "-O", str(tmp)]
    for h in headers or []:
        cmd += ["--header", h]
    run(cmd + [url])
    os.replace(tmp, dst)


# ---------------------------------------------------------------- steps
def check_drive(a: argparse.Namespace) -> Path | None:
    if a.no_drive:
        log("Drive disabled (--no-drive): nothing will be persisted")
        return None
    if not Path("/content/drive/MyDrive").is_dir():
        die("Google Drive is not mounted. Run in a notebook cell first:\n"
            "  from google.colab import drive; drive.mount('/content/drive')\n"
            "or pass --no-drive.")
    root = Path(a.drive_root)
    for d in ("models", "loras", "outputs"):
        (root / d).mkdir(parents=True, exist_ok=True)
    log(f"Drive root: {root}")
    return root


def setup_comfyui(a: argparse.Namespace) -> Path:
    comfy = Path(a.comfy)
    marker = comfy / ".deps_installed"
    if not (comfy / "main.py").exists():
        log("cloning ComfyUI ...")
        run(["git", "clone", "-q", "https://github.com/comfyanonymous/ComfyUI.git", str(comfy)])
        marker.unlink(missing_ok=True)
    elif a.update:
        log("updating ComfyUI ...")
        run(["git", "-C", str(comfy), "pull", "-q"])
        marker.unlink(missing_ok=True)
    if not marker.exists():
        log("installing ComfyUI requirements (first run only) ...")
        run([sys.executable, "-m", "pip", "install", "-q", "-r", str(comfy / "requirements.txt")])
        marker.write_text("ok")
    return comfy


def fetch_base_models(a: argparse.Namespace, comfy: Path, drive: Path | None) -> None:
    cache = drive is not None and not a.no_cache_base
    for sub, name in BASE_MODELS:
        dst = comfy / "models" / sub / name
        drv = drive / "models" / sub / name if drive else None
        if dst.exists():
            # present locally but missing on Drive -> back-fill the cache
            if cache and not drv.exists():
                log(f"caching to Drive: {name}")
                atomic_copy(dst, drv)
            else:
                log(f"base model ready: {name}")
            continue
        if drv is not None and drv.exists():
            log(f"copying from Drive: {name}")
            atomic_copy(drv, dst)
            continue
        log(f"downloading from HuggingFace: {name}")
        download(f"{HF_BASE}/{sub}/{name}", dst)
        if cache:
            log(f"caching to Drive: {name}")
            atomic_copy(dst, drv)


def fetch_lora(a: argparse.Namespace, comfy: Path, drive: Path | None) -> None:
    dst = comfy / "models" / "loras" / a.lora_name
    drv = drive / "loras" / a.lora_name if drive else None
    if dst.exists():
        return
    if drv is not None and drv.exists():
        log(f"copying LoRA from Drive: {a.lora_name}")
        atomic_copy(drv, dst)
        return
    token = a.civitai_token or os.environ.get("CIVITAI_TOKEN", "")
    if a.lora_url:
        log(f"downloading LoRA: {a.lora_name}")
        headers = [f"Authorization: Bearer {token}"] if token else []
        download(a.lora_url, dst, headers)
        if drv is not None:
            atomic_copy(dst, drv)
        return
    where = f"{drive}/loras/" if drive else str(dst.parent)
    die(f"LoRA not found: {a.lora_name}\n"
        f"  A) put the file (exact name) into {where}\n"
        "  B) pass --lora-url <civitai download url> [--civitai-token <token>]")


def comfy_up(url: str) -> bool:
    try:
        urllib.request.urlopen(f"{url}/system_stats", timeout=3)
        return True
    except Exception:  # noqa: BLE001
        return False


def tail(path: Path, n: int = 60) -> str:
    try:
        return "\n".join(path.read_text(errors="replace").splitlines()[-n:])
    except OSError:
        return "(no log)"


def start_comfyui(a: argparse.Namespace, comfy: Path, url: str) -> None:
    if comfy_up(url):
        log("ComfyUI already running, reusing it")
        return
    logfile = comfy / "comfy.log"
    log(f"starting ComfyUI (log: {logfile}) ...")
    cmd = [sys.executable, "main.py", "--listen", "127.0.0.1", "--port", str(COMFY_PORT)] + a.comfy_args.split()
    # start_new_session: keep ComfyUI alive after this script exits, so a re-run only generates
    proc = subprocess.Popen(cmd, cwd=comfy, stdout=open(logfile, "w"),
                            stderr=subprocess.STDOUT, start_new_session=True)
    deadline = time.monotonic() + 360
    while time.monotonic() < deadline:
        if proc.poll() is not None:
            die(f"ComfyUI exited early (code {proc.returncode}). Last log lines:\n{tail(logfile)}")
        if comfy_up(url):
            log("ComfyUI ready")
            return
        time.sleep(3)
    die(f"ComfyUI did not become ready in 360s. Last log lines:\n{tail(logfile)}")


def generate(a: argparse.Namespace, comfy: Path, drive: Path | None, env: dict) -> Path:
    if a.prompt:
        prompt = a.prompt
    else:
        pf = Path(a.prompt_file)
        if not pf.is_absolute():
            pf = PKG_DIR / pf
        prompt = pf.read_text(encoding="utf-8").strip()
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    out = PKG_DIR / "outputs" / f"colab_{stamp}.png"
    out.parent.mkdir(parents=True, exist_ok=True)
    log(f"generating {a.width}x{a.height}, {a.steps} steps, seed {a.seed} ...")
    cmd = [sys.executable, str(PKG_DIR / "scripts" / "qwen_pose_test.py"),
           "--mode", "t2i", "--name", "colab", "--prompt", prompt,
           "--seed", str(a.seed), "--steps", str(a.steps), "--cfg", str(a.cfg),
           "--sampler", "er_sde", "--scheduler", "beta",
           "--width", str(a.width), "--height", str(a.height),
           "--lora", a.lora_name, "--lora-strength", str(a.lora_strength),
           "--out", str(out)]
    r = subprocess.run(cmd, cwd=PKG_DIR, env=env)
    if r.returncode != 0 or not out.exists():
        die(f"generation failed. ComfyUI log tail:\n{tail(comfy / 'comfy.log')}")
    if drive is not None:
        shutil.copy(out, drive / "outputs")
        meta = out.with_suffix(out.suffix + ".json")
        if meta.exists():
            shutil.copy(meta, drive / "outputs")
        log(f"saved to Drive: {drive / 'outputs' / out.name}")
    return out


def parse() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="One-shot Colab setup + T2I generation (re-runnable)")
    g = p.add_argument_group("paths / Drive")
    g.add_argument("--comfy", default="/content/ComfyUI")
    g.add_argument("--drive-root", default="/content/drive/MyDrive/qwen21_pose")
    g.add_argument("--no-drive", action="store_true", help="do not use Google Drive at all")
    g.add_argument("--no-cache-base", action="store_true",
                   help="do NOT cache base models (~16GB) on Drive (default: cache them)")
    g.add_argument("--update", action="store_true", help="git pull ComfyUI and reinstall requirements")
    g = p.add_argument_group("LoRA")
    g.add_argument("--lora-name", default=DEFAULT_LORA)
    g.add_argument("--lora-url", default="", help="download URL if the LoRA is not on Drive yet")
    g.add_argument("--civitai-token", default="", help="or set env CIVITAI_TOKEN")
    g.add_argument("--lora-strength", type=float, default=1.0)
    g = p.add_argument_group("generation")
    g.add_argument("--prompt", default="", help="inline prompt (overrides --prompt-file)")
    g.add_argument("--prompt-file", default="prompts/taws_v13_shower.txt")
    g.add_argument("--width", type=int, default=1024)
    g.add_argument("--height", type=int, default=1024)
    g.add_argument("--steps", type=int, default=20)
    g.add_argument("--cfg", type=float, default=2.5)
    g.add_argument("--seed", type=int, default=80964)
    g = p.add_argument_group("misc")
    g.add_argument("--comfy-args", default="--lowvram --disable-smart-memory --fp32-vae",
                   help="extra ComfyUI launch args (low-memory defaults for a T4)")
    g.add_argument("--setup-only", action="store_true", help="prepare everything, do not generate")
    g.add_argument("--skip-doctor", action="store_true")
    return p.parse_args()


def main() -> int:
    a = parse()
    url = f"http://127.0.0.1:{COMFY_PORT}"
    env = dict(os.environ, COMFY=a.comfy, POSELAB=str(PKG_DIR), COMFYUI_URL=url,
               COMFYUI_INPUT=f"{a.comfy}/input", COMFYUI_OUTPUT=f"{a.comfy}/output")
    os.environ.update(env)

    drive = check_drive(a)
    comfy = setup_comfyui(a)
    fetch_base_models(a, comfy, drive)
    fetch_lora(a, comfy, drive)
    start_comfyui(a, comfy, url)
    if not a.skip_doctor:
        subprocess.run([sys.executable, str(PKG_DIR / "scripts" / "doctor.py")], cwd=PKG_DIR, env=env)
    if a.setup_only:
        log("setup done (--setup-only)")
        return 0
    out = generate(a, comfy, drive, env)
    print(f"OUTPUT: {out}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
