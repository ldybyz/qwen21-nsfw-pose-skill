#!/usr/bin/env python3
"""run_photobook.py: General-purpose Reusable Photobook / Gravure Suite.

Allows taking ANY character card from characters/ and applying ANY photobook
template from templates/photobooks/*.yaml, with automatic prompt slot-filling,
prompt txt export, and batch execution.

Usage examples:
    # 1. List all available photobook templates:
    python scripts/run_photobook.py --list-templates

    # 2. Preview prompts for Su Mei'er with default canopy bed template:
    python scripts/run_photobook.py --character characters/chinese/su_meier.md --dry-run

    # 3. Export prompt txts to a custom directory:
    python scripts/run_photobook.py --character characters/chinese/su_meier.md --export-dir photobooks/su_meier

    # 4. Use another template (e.g. onsen_hotspring) for Su Mei'er:
    python scripts/run_photobook.py --character su_meier --template onsen_hotspring --dry-run

    # 5. Reuse the canopy bed photobook for Yang Yuyao (盛唐杨玉瑶):
    python scripts/run_photobook.py --character cn02_yang_yuyao --template chinese_canopy_bed --dry-run

    # 6. Directly run generation against ComfyUI:
    python scripts/run_photobook.py --character su_meier --template chinese_canopy_bed --run
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
except ImportError:
    print("Error: PyYAML is required. Please install it with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

_PKG_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = _PKG_DIR / "templates" / "photobooks"


def list_available_templates() -> Dict[str, Path]:
    """Scan and return all template files in templates/photobooks/."""
    templates = {}
    if not TEMPLATE_DIR.is_dir():
        return templates

    for f in TEMPLATE_DIR.glob("*.yaml"):
        templates[f.stem] = f
    return templates


def load_template(identifier: str) -> Dict[str, Any]:
    """Load a photobook template by ID or file path."""
    p = Path(identifier)
    if p.is_file():
        data = yaml.safe_load(p.read_text(encoding="utf-8"))
        data["_file_path"] = p
        return data

    cand = TEMPLATE_DIR / f"{identifier}.yaml"
    if cand.is_file():
        data = yaml.safe_load(cand.read_text(encoding="utf-8"))
        data["_file_path"] = cand
        return data

    # Check without extension
    cand2 = TEMPLATE_DIR / identifier
    if cand2.is_file():
        data = yaml.safe_load(cand2.read_text(encoding="utf-8"))
        data["_file_path"] = cand2
        return data

    available = list(list_available_templates().keys())
    raise FileNotFoundError(
        f"Photobook template '{identifier}' not found in {TEMPLATE_DIR}.\nAvailable templates: {available}"
    )


def find_character_file(identifier: str) -> Path:
    """Resolve character markdown file by path or name."""
    p = Path(identifier)
    if p.is_file():
        return p

    cand = _PKG_DIR / identifier
    if cand.is_file():
        return cand

    # Search in characters/
    for root, _, files in os.walk(_PKG_DIR / "characters"):
        for f in files:
            if f.endswith(".md"):
                stem = Path(f).stem
                if identifier.lower() in stem.lower():
                    return Path(root) / f

    raise FileNotFoundError(f"Cannot find character card for: {identifier}")


def parse_character_card(path: Path) -> Dict[str, Any]:
    """Parse character card markdown to extract name, modular prompt, and recommended params."""
    text = path.read_text(encoding="utf-8")

    # 1. Extract Character ID / Name
    char_id = path.stem.replace("cn", "").replace("ea", "").replace("ca", "").strip("_")
    name_match = re.search(r"#\s*人物卡[:：]?\s*(?:\[[^\]]+\])?\s*([^\s(（]+)", text)
    char_name = name_match.group(1).strip() if name_match else char_id

    # 2. Extract Modular Insertion Block (Section 5)
    mod_match = re.search(
        r"##\s*5[^\n]*\n(?:[^\n]*\n)*?```(?:text)?\s*\n([\s\S]*?)\n```",
        text,
    )
    if not mod_match:
        mod_match = re.search(r"##\s*5[\s\S]*?```(?:text)?\s*\n([\s\S]*?)\n```", text)

    if not mod_match:
        raise ValueError(f"Could not find Section 5 (Modular Insertion Block) in {path}")

    subject_prompt = mod_match.group(1).strip()

    # 3. Extract Recommended Parameters (Section 3)
    seed = 80964
    seed_match = re.search(r"Seed[^\n|]*\|\s*`?(\d+)`?", text, re.IGNORECASE)
    if seed_match:
        seed = int(seed_match.group(1))

    cfg = 4.0
    cfg_match = re.search(r"CFG[^\n|]*\|\s*`?([0-9.]+)`?", text, re.IGNORECASE)
    if cfg_match:
        try:
            cfg = float(cfg_match.group(1))
        except ValueError:
            pass

    lora = "thesealpacas-nsfw-v2.safetensors"
    lora_match = re.search(r"LoRA[^\n|]*\|\s*`?([a-zA-Z0-9_\-\.]+safetensors)`?", text, re.IGNORECASE)
    if lora_match:
        lora = lora_match.group(1)

    lora_strength = 0.85
    wt_match = re.search(r"权重\s*`?([0-9.]+)`?", text)
    if wt_match:
        try:
            lora_strength = float(wt_match.group(1))
        except ValueError:
            pass

    return {
        "char_id": path.stem,
        "char_name": char_name,
        "subject_prompt": subject_prompt,
        "seed": seed,
        "cfg": cfg,
        "lora": lora,
        "lora_strength": lora_strength,
        "steps": 45,
        "sampler": "er_sde",
        "scheduler": "beta",
        "width": 1152,
        "height": 1728,
    }


def main():
    parser = argparse.ArgumentParser(
        description="General-purpose reusable photobook engine powered by external YAML templates."
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List all available photobook templates in templates/photobooks/",
    )
    parser.add_argument(
        "--character",
        "-c",
        help="Path or name of the character card (e.g. characters/chinese/su_meier.md or su_meier)",
    )
    parser.add_argument(
        "--template",
        "-t",
        default="chinese_canopy_bed",
        help="Photobook scene template ID or YAML file path (default: chinese_canopy_bed)",
    )
    parser.add_argument(
        "--export-dir",
        "-e",
        help="Directory to export individual prompt .txt and .params.json files (e.g. photobooks/su_meier)",
    )
    parser.add_argument(
        "--output-dir",
        "-o",
        help="Directory to save rendered PNG images (default: outputs/photobooks/<character_id>)",
    )
    parser.add_argument(
        "--run",
        action="store_true",
        help="Execute generation against ComfyUI via scripts/qwen_pose_test.py",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print out all generated prompts without saving or rendering",
    )
    parser.add_argument("--seed", type=int, help="Override random seed")
    parser.add_argument("--cfg", type=float, help="Override CFG scale")
    parser.add_argument("--lora", type=str, help="Override LoRA filename")
    parser.add_argument("--lora-strength", type=float, help="Override LoRA strength")

    args = parser.parse_args()

    # 1. Handle --list-templates
    if args.list_templates:
        templates = list_available_templates()
        print("\n📚 已发现的写真套图模板 (templates/photobooks/):")
        print("=" * 60)
        for tid, tpath in templates.items():
            try:
                tdata = yaml.safe_load(tpath.read_text(encoding="utf-8"))
                name_zh = tdata.get("name_zh", tid)
                shot_cnt = len(tdata.get("shots", []))
                desc = tdata.get("description", "")
                print(f"  • {tid:20s} | {name_zh} ({shot_cnt} 幕分镜)")
                if desc:
                    print(f"    说明: {desc}")
            except Exception as e:
                print(f"  • {tid:20s} (解析失败: {e})")
        print("=" * 60)
        print("使用方式: python scripts/run_photobook.py --character <name> --template <template_id>\n")
        return

    if not args.character:
        parser.error("必须通过 --character / -c 指定角色卡，或使用 --list-templates 查看可用模板。")

    # 2. Load template YAML
    template_data = load_template(args.template)
    template_id = template_data.get("id", Path(args.template).stem)
    template_name = template_data.get("name_zh", template_id)
    template_shots = template_data.get("shots", [])
    default_params = template_data.get("default_params", {})

    if not template_shots:
        raise ValueError(f"Template '{template_id}' does not contain any 'shots' definition.")

    # 3. Load Character Card
    char_path = find_character_file(args.character)
    char_info = parse_character_card(char_path)

    # Blend character params with template default params
    # Priority: CLI argument > Character card params > Template default params
    lora = args.lora or char_info.get("lora") or default_params.get("lora", "thesealpacas-nsfw-v2.safetensors")
    lora_strength = (
        args.lora_strength
        if args.lora_strength is not None
        else char_info.get("lora_strength", default_params.get("lora_strength", 0.85))
    )
    cfg = args.cfg if args.cfg is not None else char_info.get("cfg", default_params.get("cfg", 4.0))
    seed = args.seed if args.seed is not None else char_info.get("seed", 80964)
    sampler = char_info.get("sampler") or default_params.get("sampler", "er_sde")
    scheduler = char_info.get("scheduler") or default_params.get("scheduler", "beta")
    width = char_info.get("width") or default_params.get("width", 1152)
    height = char_info.get("height") or default_params.get("height", 1728)

    out_img_dir = Path(args.output_dir or f"outputs/photobooks/{char_info['char_id']}_{template_id}")

    print(f"\n🎭 ========================================================")
    print(f" 角色写真集引擎: [{char_info['char_name']}] ({char_info['char_id']})")
    print(f" 套用模板: {template_name} [{template_id}] ({len(template_shots)} 幕分镜)")
    print(f" 参数基准: Seed={seed}, CFG={cfg}, LoRA={lora}@{lora_strength}")
    print(f"========================================================\n")

    export_path = Path(args.export_dir) if args.export_dir else None
    if export_path:
        export_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 导出提示词目录: {export_path.resolve()}\n")

    for i, shot in enumerate(template_shots, start=1):
        # Slot filling: replace {SUBJECT} with character's Section 5 modular block
        raw_prompt = shot["prompt"]
        pos_prompt = raw_prompt.replace("{SUBJECT}", char_info["subject_prompt"]).strip()
        neg_prompt = shot.get("negative") or default_params.get(
            "negative",
            "blurry, deformed, bad anatomy, bad hands, plastic skin, cartoon, 3d render, doll, extra limbs, watermark, text"
        )
        shot_id = shot["id"]
        shot_name = shot.get("name_zh", shot_id)
        shot_type = shot.get("shot_type", "")
        steps = shot.get("steps", default_params.get("steps", 45))

        print(f"[{i}/{len(template_shots)}] 分镜: {shot_name} ({shot_type})")
        print(f"    标识: {shot_id}")

        if args.dry_run:
            print(f"    Positive Prompt:\n    {pos_prompt[:180]}...")
            print(f"    Negative Prompt:\n    {neg_prompt}\n")

        # Export txt & params.json
        if export_path:
            txt_file = export_path / f"{shot_id}.txt"
            full_txt = f"{pos_prompt}\n\n[negative] {neg_prompt}\n"
            txt_file.write_text(full_txt, encoding="utf-8")

            param_file = export_path / f"{shot_id}.params.json"
            param_data = {
                "steps": steps,
                "cfg": cfg,
                "sampler": sampler,
                "scheduler": scheduler,
                "seed": seed,
                "width": width,
                "height": height,
                "lora": lora,
                "lora_strength": lora_strength,
                "description": f"{char_info['char_name']}写真第{i}幕：{shot_name}",
            }
            param_file.write_text(json.dumps(param_data, indent=2, ensure_ascii=False), encoding="utf-8")
            print(f"    -> 已保存: {txt_file.name} & {param_file.name}")

        # Run ComfyUI execution if requested
        if args.run:
            out_img_dir.mkdir(parents=True, exist_ok=True)
            out_img_file = out_img_dir / f"{shot_id}.png"
            cmd = [
                sys.executable,
                str(_PKG_DIR / "scripts" / "qwen_pose_test.py"),
                "--mode", "t2i",
                "--name", f"{char_info['char_id']}_{template_id}_{shot_id}",
                "--prompt", pos_prompt,
                "--negative", neg_prompt,
                "--seed", str(seed),
                "--steps", str(steps),
                "--cfg", str(cfg),
                "--sampler", sampler,
                "--scheduler", scheduler,
                "--width", str(width),
                "--height", str(height),
                "--lora", lora,
                "--lora-strength", str(lora_strength),
                "--out", str(out_img_file),
            ]
            print(f"    🚀 正在提交 ComfyUI 推理...")
            res = subprocess.run(cmd)
            if res.returncode == 0:
                print(f"    ✅ 完成: {out_img_file}")
            else:
                print(f"    ❌ 失败，返回码: {res.returncode}")

    print("\n✨ 全部处理完毕！")


if __name__ == "__main__":
    main()
