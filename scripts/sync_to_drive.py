#!/usr/bin/env python3
"""sync_to_drive.py: One-click utility to migrate/copy all local outputs to Google Drive.

Scans:
  - outputs/ (within the repository)
  - /content/qwen21-nsfw-pose-skill/outputs/
  - /content/ComfyUI/output/
  - ~/ComfyUI/output/

Copies all generated images, dolls, UI screenshots, and metadata into the target Google Drive directory.
"""
from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

_PKG_DIR = Path(__file__).resolve().parent.parent


def get_default_target() -> Path:
    target_env = os.environ.get("DRIVE_OUTPUT")
    if target_env:
        return Path(target_env)
    return Path("/content/drive/MyDrive/qwen21_pose/outputs")


def migrate_outputs(target_dir: Path, dry_run: bool = False, move: bool = False) -> list[Path]:
    try:
        from google.colab import drive  # noqa: F401
        if not Path("/content/drive/MyDrive").is_dir():
            print("📦 检测到 Google Colab 环境，正在挂载 Google Drive...")
            drive.mount("/content/drive")
    except Exception:
        pass

    target_dir = target_dir.expanduser().resolve()
    print(f"\n🚀 开始迁移本地成果至 Google Drive 目标目录:\n   -> {target_dir}\n")

    if not dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    search_roots = [
        _PKG_DIR / "outputs",
        Path("/content/qwen21-nsfw-pose-skill/outputs"),
        Path("/content/ComfyUI/output"),
        Path("/root/ComfyUI/output"),
        Path.home() / "ComfyUI" / "output",
    ]

    valid_roots = []
    seen_roots = set()
    for r in search_roots:
        if r.is_dir() and r.resolve() not in seen_roots:
            seen_roots.add(r.resolve())
            valid_roots.append(r.resolve())

    migrated: list[Path] = []
    seen_files = set()

    for root in valid_roots:
        for file_path in root.rglob("*"):
            if not file_path.is_file():
                continue
            # Only migrate image and meta files
            if file_path.suffix.lower() not in [".png", ".jpg", ".jpeg", ".webp", ".json", ".txt"]:
                continue
            if file_path.resolve() in seen_files:
                continue

            rel = file_path.relative_to(root)
            dst_file = target_dir / rel

            seen_files.add(file_path.resolve())

            # Skip copying to itself
            if file_path.resolve() == dst_file.resolve():
                continue

            # Check if target exists and matches
            if dst_file.exists() and dst_file.stat().st_size == file_path.stat().st_size:
                continue

            action_name = "移动" if move else "复制"
            if dry_run:
                print(f"  [预览] 将{action_name}: {rel} ({file_path.stat().st_size / 1024:.1f} KB)")
            else:
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                if move:
                    shutil.move(str(file_path), str(dst_file))
                else:
                    shutil.copy2(file_path, dst_file)
                print(f"  ✅ 已{action_name}: {rel} -> {dst_file.parent.name}/{dst_file.name}")
            migrated.append(dst_file)

    print(f"\n✨ 迁移完毕！共同步 {len(migrated)} 个文件至 {target_dir}")
    return migrated


def main():
    parser = argparse.ArgumentParser(description="Migrate local Colab outputs to Google Drive.")
    parser.add_argument(
        "--target",
        "-t",
        default=str(get_default_target()),
        help="Target directory in Google Drive (default: /content/drive/MyDrive/output)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="List files that would be copied without actually copying",
    )
    parser.add_argument(
        "--move",
        action="store_true",
        help="Move files instead of copying (deletes local copies)",
    )

    args = parser.parse_args()
    migrate_outputs(target_dir=Path(args.target), dry_run=args.dry_run, move=args.move)


if __name__ == "__main__":
    main()

