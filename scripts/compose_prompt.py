#!/usr/bin/env python3
"""compose_prompt: Compose character cards from characters/ with scenes from prompts/.

Usage:
  # View standalone prompt or modular block of a character
  python scripts/compose_prompt.py --character characters/east_asian/lin_yuting.md --show-char

  # Blend character into a scene and print the combined prompt
  python scripts/compose_prompt.py \
    --character characters/east_asian/lin_yuting.md \
    --scene prompts/scene_chinese_tearoom.txt

  # Blend character into a scene and directly run qwen_pose_test.py
  python scripts/compose_prompt.py \
    --character characters/east_asian/lin_yuting.md \
    --scene prompts/scene_chinese_tearoom.txt \
    --run --out outputs/composed_lin_tearoom.png
"""
from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent.parent


def extract_sections_from_markdown(md_content: str) -> dict[str, str]:
    """Extract code blocks and sections from a character card markdown."""
    data: dict[str, str] = {
        "benchmark_prompt": "",
        "modular_block": "",
        "negative_prompt": "",
    }

    # Extract Standalone Benchmark Prompt from ## 4
    m_bench = re.search(r"## 4\.[^\n]*\n.*?```(?:text)?\n(.*?)```", md_content, re.DOTALL)
    if m_bench:
        raw_bench = m_bench.group(1).strip()
        if "[negative]" in raw_bench:
            parts = raw_bench.split("[negative]")
            data["benchmark_prompt"] = parts[0].strip()
            data["negative_prompt"] = parts[1].strip()
        else:
            data["benchmark_prompt"] = raw_bench

    # Extract Modular Insertion Block from ## 5
    m_mod = re.search(r"## 5\.[^\n]*\n.*?```(?:text)?\n(.*?)```", md_content, re.DOTALL)
    if m_mod:
        data["modular_block"] = m_mod.group(1).strip()

    return data


def blend_character_into_scene(character_block: str, scene_prompt: str) -> tuple[str, str]:
    """Replace subject description in scene prompt with character modular block."""
    negative = ""
    if "[negative]" in scene_prompt:
        parts = scene_prompt.split("[negative]")
        scene_prompt = parts[0].strip()
        negative = parts[1].strip()

    # Pattern targeting typical subject phrases in prompts/
    # e.g., "of a graceful young Chinese woman (23 years old)" or "a gorgeous woman"
    subject_patterns = [
        r"(?:of\s+)?(?:a|an)\s+[^,\.\n]+?\b(?:woman|female|model|lady|maiden)(?:\s*\([^)]+\))?",
        r"(?:of\s+)?(?:a|an)\s+(?:[a-zA-Z-]+\s+)*(?:woman|female|model|lady|maiden)",
    ]

    replaced = False
    merged_prompt = scene_prompt
    for pat in subject_patterns:
        m = re.search(pat, merged_prompt, flags=re.IGNORECASE)
        if m:
            matched_text = m.group(0)
            prefix = "of " if matched_text.lower().startswith("of ") else ""
            char_text = character_block.strip()
            # If char_text already starts with a/an, handle prefix smoothly
            if prefix and re.match(r"^(?:a|an)\s+", char_text, flags=re.IGNORECASE):
                replacement = f"of {char_text}"
            else:
                replacement = f"{prefix}{char_text}"
            start, end = m.span()
            merged_prompt = merged_prompt[:start] + replacement + merged_prompt[end:]
            # Clean up accidental double articles if any
            merged_prompt = re.sub(r"\b(of\s+)(?:a|an)\s+(a|an)\b", r"\1\2", merged_prompt, flags=re.IGNORECASE)
            merged_prompt = re.sub(r"\b(a|an)\s+(a|an)\b", r"\1", merged_prompt, flags=re.IGNORECASE)
            replaced = True
            break

    if not replaced:
        # Fallback: Prepend character description right after the initial framing if possible
        merged_prompt = f"{character_block}, {scene_prompt}"

    return merged_prompt, negative


def main() -> int:
    parser = argparse.ArgumentParser(description="Compose character cards with scene prompts.")
    parser.add_argument("--character", "-c", required=True, help="Path to character card markdown file")
    parser.add_argument("--scene", "-s", default="", help="Path to scene prompt text file (optional)")
    parser.add_argument("--show-char", action="store_true", help="Display extracted character card info and exit")
    parser.add_argument("--run", action="store_true", help="Directly invoke scripts/qwen_pose_test.py")
    parser.add_argument("--out", default="", help="Output image file path if --run is specified")
    parser.add_argument("--seed", type=int, default=80964, help="Random seed (default: 80964)")
    parser.add_argument("--steps", type=int, default=45, help="Sampling steps (default: 45)")
    parser.add_argument("--cfg", type=float, default=2.5, help="CFG scale (default: 2.5)")
    parser.add_argument("--lora", default="qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors", help="LoRA model name")
    parser.add_argument("--lora-strength", type=float, default=1.0, help="LoRA weight (default: 1.0)")

    args = parser.parse_args()

    char_path = Path(args.character)
    if not char_path.is_file():
        # Try relative to _PKG_DIR
        char_path = _PKG_DIR / args.character
        if not char_path.is_file():
            print(f"Error: Character card file not found: {args.character}", file=sys.stderr)
            return 1

    md_content = char_path.read_text(encoding="utf-8")
    char_data = extract_sections_from_markdown(md_content)

    if args.show_char or not args.scene:
        print(f"=== Character Card: {char_path.name} ===")
        print(f"\n[Modular Block]:\n{char_data['modular_block']}")
        print(f"\n[Benchmark Prompt]:\n{char_data['benchmark_prompt']}")
        if char_data["negative_prompt"]:
            print(f"\n[Negative Prompt]:\n{char_data['negative_prompt']}")
        if not args.scene:
            return 0

    scene_path = Path(args.scene)
    if not scene_path.is_file():
        scene_path = _PKG_DIR / args.scene
        if not scene_path.is_file():
            print(f"Error: Scene prompt file not found: {args.scene}", file=sys.stderr)
            return 1

    scene_text = scene_path.read_text(encoding="utf-8")
    final_prompt, scene_neg = blend_character_into_scene(char_data["modular_block"], scene_text)
    final_neg = char_data["negative_prompt"] or scene_neg

    print("\n" + "=" * 60)
    print("COMPOSED PROMPT:")
    print("=" * 60)
    print(final_prompt)
    if final_neg:
        print("\nNEGATIVE PROMPT:")
        print(final_neg)
    print("=" * 60 + "\n")

    if args.run:
        out_path = args.out or f"outputs/composed_{char_path.stem}_{scene_path.stem}.png"
        cmd = [
            sys.executable,
            str(_PKG_DIR / "scripts" / "qwen_pose_test.py"),
            "--mode", "t2i",
            "--name", f"compose_{char_path.stem}",
            "--prompt", final_prompt,
            "--seed", str(args.seed),
            "--steps", str(args.steps),
            "--cfg", str(args.cfg),
            "--sampler", "er_sde",
            "--scheduler", "beta",
            "--width", "1152",
            "--height", "1728",
            "--lora", args.lora,
            "--lora-strength", str(args.lora_strength),
            "--out", out_path,
        ]
        if final_neg:
            cmd.extend(["--negative", final_neg])

        print(f"Running command:\n{' '.join(cmd)}\n")
        return subprocess.call(cmd)

    return 0


if __name__ == "__main__":
    sys.exit(main())
