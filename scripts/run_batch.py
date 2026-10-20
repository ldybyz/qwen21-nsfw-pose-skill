#!/usr/bin/env python3
"""run_batch: Execute batch workflows — matrix sweep, A/B comparison, character tour.

Reads a workflow YAML file that defines fixed elements and sweep/compare axes,
expands them into individual compose_prompt invocations, and runs them sequentially.

Usage:
  # Dry run — preview all combinations without executing
  python scripts/run_batch.py --workflow workflows/batch_pose_matrix.yaml --dry-run

  # Execute all combinations
  python scripts/run_batch.py --workflow workflows/batch_pose_matrix.yaml

  # Resume from a specific index (e.g. after interruption)
  python scripts/run_batch.py --workflow workflows/batch_pose_matrix.yaml --start-from 5
"""
from __future__ import annotations

import argparse
import itertools
import json
import sys
import time
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Error: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

_PKG_DIR = Path(__file__).resolve().parent.parent

# Import compose engine
sys.path.insert(0, str(_PKG_DIR / "scripts"))
from compose_prompt import (
    ELEMENT_ORDER,
    ElementLoader,
    compose_from_elements,
    check_compatibility,
    _run_generation,
)


def load_workflow(path: Path) -> dict[str, Any]:
    """Load a workflow YAML file."""
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def expand_character_glob(pattern: str) -> list[str]:
    """Expand a glob pattern like 'characters/east_asian/*.md' to element ids."""
    from compose_prompt import extract_sections_from_markdown

    results = []
    base = _PKG_DIR / pattern
    # Use the parent directory and glob pattern
    parent = _PKG_DIR / Path(pattern).parent
    glob_pattern = Path(pattern).name

    for fpath in sorted(parent.glob(glob_pattern)):
        if fpath.suffix == ".md":
            results.append(str(fpath.relative_to(_PKG_DIR)))
    return results


def expand_sweep(workflow: dict[str, Any]) -> list[dict[str, Any]]:
    """Expand sweep axes into a list of element-id combinations (Cartesian product)."""
    fixed = dict(workflow.get("fixed", {}))
    sweep = workflow.get("sweep", {})

    # Build sweep axes
    axes: list[tuple[str, list[Any]]] = []
    for key, values in sweep.items():
        if isinstance(values, dict) and values.get("source") == "character_glob":
            # Expand glob pattern
            pattern = values.get("pattern", "")
            expanded = expand_character_glob(pattern)
            axes.append((key, expanded))
        elif isinstance(values, list):
            axes.append((key, values))
        else:
            axes.append((key, [values]))

    if not axes:
        # No sweep — just return fixed
        return [fixed]

    # Cartesian product of all sweep axes
    axis_names = [a[0] for a in axes]
    axis_values = [a[1] for a in axes]

    combinations = []
    for combo in itertools.product(*axis_values):
        element_ids = dict(fixed)
        for name, value in zip(axis_names, combo):
            element_ids[name] = value
        combinations.append(element_ids)

    return combinations


def expand_compare(workflow: dict[str, Any]) -> list[tuple[dict[str, Any], str]]:
    """Expand compare variations into a list of (element_ids, label) tuples."""
    base = dict(workflow.get("base", {}))
    compare = workflow.get("compare", [])

    result = []
    for variation in compare:
        element_ids = dict(base)
        label = variation.pop("label", "")
        element_ids.update(variation)
        result.append((element_ids, label))
        # Restore label
        variation["label"] = label

    return result


def format_output_path(pattern: str, element_ids: dict[str, Any], index: int) -> str:
    """Format an output path from a pattern and element ids."""
    path = pattern
    for key, value in element_ids.items():
        if isinstance(value, str):
            # Extract the last meaningful part
            val_id = Path(value).stem if "/" in value or "\\" in value else value
        elif isinstance(value, dict):
            val_id = value.get("id", value.get("path", "").split("/")[-1].replace(".md", ""))
        else:
            val_id = str(value)
        path = path.replace(f"{{{key}.id}}", val_id)
        path = path.replace(f"{{{key}}}", val_id)

    # Replace any remaining template vars
    path = path.replace("{index}", str(index))
    return path


def main() -> int:
    parser = argparse.ArgumentParser(description="Execute batch workflows.")
    parser.add_argument("--workflow", "-w", required=True, help="Path to workflow YAML file")
    parser.add_argument("--dry-run", action="store_true", help="Preview combinations without executing")
    parser.add_argument("--start-from", type=int, default=0, help="Resume from this index (0-based)")
    args = parser.parse_args()

    workflow_path = Path(args.workflow)
    if not workflow_path.is_file():
        workflow_path = _PKG_DIR / args.workflow
    if not workflow_path.is_file():
        print(f"Error: Workflow file not found: {args.workflow}", file=sys.stderr)
        return 1

    wf = load_workflow(workflow_path)
    wf_type = wf.get("workflow", "batch")
    wf_name = wf.get("name_zh", wf.get("description", workflow_path.stem))
    output_pattern = wf.get("output_pattern", "outputs/batch/{index}_{pose}.png")
    params = wf.get("params", {})

    # Expand combinations
    if "compare" in wf:
        items = expand_compare(wf)
        labeled = True
    else:
        combos = expand_sweep(wf)
        items = [(c, "") for c in combos]
        labeled = False

    total = len(items)
    print(f"\n{'═' * 60}")
    print(f"  Workflow: {wf_name}")
    print(f"  Type: {wf_type}")
    print(f"  Total combinations: {total}")
    print(f"{'═' * 60}\n")

    loader = ElementLoader()
    results: list[dict[str, Any]] = []

    for idx, (element_ids, label) in enumerate(items):
        if idx < args.start_from:
            continue

        out_path = format_output_path(output_pattern, element_ids, idx)
        prompt = compose_from_elements(loader, element_ids)

        label_str = f" [{label}]" if label else ""
        print(f"\n[{idx + 1}/{total}]{label_str}")
        print(f"  Elements: {element_ids}")
        print(f"  Output: {out_path}")

        if args.dry_run:
            print(f"  Prompt ({len(prompt)} chars): {prompt[:120]}...")
            results.append({"index": idx, "label": label, "output": out_path, "prompt": prompt})
            continue

        # Compose and run
        neg = params.get("negative_prompt", "")
        print(f"  Prompt: {prompt[:100]}...")
        print(f"  Running...")

        t0 = time.time()
        ret = _run_generation(prompt, neg, params, out_path, element_ids)
        elapsed = time.time() - t0

        status = "ok" if ret == 0 else f"error (code {ret})"
        print(f"  → {status} ({elapsed:.0f}s)")

        results.append({
            "index": idx,
            "label": label,
            "output": out_path,
            "status": status,
            "elapsed_s": round(elapsed, 1),
        })

    # Summary
    print(f"\n{'═' * 60}")
    print(f"  BATCH COMPLETE: {len(results)}/{total} runs")
    if not args.dry_run:
        ok_count = sum(1 for r in results if r.get("status") == "ok")
        print(f"  Success: {ok_count}, Errors: {len(results) - ok_count}")
    print(f"{'═' * 60}\n")

    # Write results manifest
    if results:
        manifest_path = _PKG_DIR / "outputs" / "batch" / f"{workflow_path.stem}_results.json"
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Results manifest: {manifest_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
