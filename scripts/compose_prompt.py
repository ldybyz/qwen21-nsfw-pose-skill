#!/usr/bin/env python3
"""compose_prompt: Compose prompts from modular seven-element YAML files.

Supports three modes:
  1. LEGACY: --character + --scene (original workflow, fully backward-compatible)
  2. RECIPE: --recipe <yaml>  (load a preset combination)
  3. ELEMENTS: --camera / --subject / --pose / --setting / --skin / --anatomy / --finish

Usage examples:
  # ── Legacy mode (backward-compatible) ──
  python scripts/compose_prompt.py \\
    --character characters/east_asian/lin_yuting.md \\
    --scene prompts/scene_chinese_tearoom.txt

  # ── Recipe mode ──
  python scripts/compose_prompt.py --recipe prompts/recipes/chinese_tearoom_lin.yaml

  # ── Element mode (free combination) ──
  python scripts/compose_prompt.py \\
    --camera low_angle_floor \\
    --subject lin_yuting \\
    --pose L1_kneeling_open \\
    --setting chinese_tearoom \\
    --skin dewy_porcelain \\
    --anatomy full_reveal_explicit \\
    --finish 8k_cinematic

  # ── Recipe + override individual elements ──
  python scripts/compose_prompt.py \\
    --recipe prompts/recipes/chinese_tearoom_lin.yaml \\
    --pose L2_prone_hips_lifted --camera overhead_topdown

  # ── List available elements ──
  python scripts/compose_prompt.py --list camera
  python scripts/compose_prompt.py --list pose --tier L2
  python scripts/compose_prompt.py --list all

  # ── Compatibility check ──
  python scripts/compose_prompt.py --check-compat \\
    --camera overhead_topdown --pose L2_seated_wide_elbows
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# ---------------------------------------------------------------------------
# Try to import PyYAML; provide a helpful error if missing
# ---------------------------------------------------------------------------
try:
    import yaml
except ImportError:
    print(
        "Error: PyYAML is required for element/recipe mode.\n"
        "Install it with: pip install pyyaml",
        file=sys.stderr,
    )
    # Allow legacy mode to continue without YAML
    yaml = None  # type: ignore[assignment]

_PKG_DIR = Path(__file__).resolve().parent.parent
_ELEMENTS_DIR = _PKG_DIR / "prompts" / "elements"
_RECIPES_DIR = _PKG_DIR / "prompts" / "recipes"

# The seven element types, in prompt assembly order
ELEMENT_ORDER = ["camera", "subject", "pose", "setting", "skin", "anatomy", "finish"]


# ═══════════════════════════════════════════════════════════════════════════
# Data classes
# ═══════════════════════════════════════════════════════════════════════════

@dataclass
class Element:
    """A single prompt element loaded from YAML."""
    element: str
    id: str
    name_zh: str = ""
    name_en: str = ""
    tags: list[str] = field(default_factory=list)
    prompt: str = ""
    # Extra fields stored as-is
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def tier(self) -> str:
        return self.extra.get("tier", "")

    @property
    def lighting(self) -> str:
        return self.extra.get("lighting", "")

    @property
    def compatibility(self) -> dict:
        return self.extra.get("compatibility", {})


@dataclass
class Recipe:
    """A preset combination referencing element ids + params."""
    recipe: str
    name_zh: str
    description: str = ""
    elements: dict[str, Any] = field(default_factory=dict)
    overrides: dict[str, str] = field(default_factory=dict)
    params: dict[str, Any] = field(default_factory=dict)
    negative_prompt: str = ""


# ═══════════════════════════════════════════════════════════════════════════
# Element Loader
# ═══════════════════════════════════════════════════════════════════════════

class ElementLoader:
    """Discover and load element YAML files from the elements/ directory."""

    def __init__(self, elements_dir: Path | None = None):
        self._dir = elements_dir or _ELEMENTS_DIR
        self._cache: dict[str, dict[str, Element]] = {}  # {element_type: {id: Element}}

    def _scan_type(self, element_type: str) -> dict[str, Element]:
        """Scan a single element type directory."""
        if element_type in self._cache:
            return self._cache[element_type]

        type_dir = self._dir / element_type
        elements: dict[str, Element] = {}
        if not type_dir.is_dir():
            self._cache[element_type] = elements
            return elements

        for fpath in sorted(type_dir.glob("*.yaml")):
            try:
                data = yaml.safe_load(fpath.read_text(encoding="utf-8"))
                if not isinstance(data, dict) or data.get("element") != element_type:
                    continue
                el_id = data.get("id", fpath.stem)
                known_keys = {"element", "id", "name_zh", "name_en", "tags", "prompt"}
                extra = {k: v for k, v in data.items() if k not in known_keys}
                el = Element(
                    element=element_type,
                    id=el_id,
                    name_zh=data.get("name_zh", ""),
                    name_en=data.get("name_en", ""),
                    tags=data.get("tags", []),
                    prompt=data.get("prompt", ""),
                    extra=extra,
                )
                elements[el_id] = el
            except Exception as exc:
                print(f"Warning: failed to load {fpath}: {exc}", file=sys.stderr)

        self._cache[element_type] = elements
        return elements

    def get(self, element_type: str, element_id: str) -> Element | None:
        """Get a specific element by type and id."""
        elements = self._scan_type(element_type)
        return elements.get(element_id)

    def list_type(self, element_type: str, tier: str = "", tags: list[str] | None = None) -> list[Element]:
        """List elements of a type, optionally filtered by tier or tags."""
        elements = self._scan_type(element_type)
        result = list(elements.values())
        if tier:
            result = [e for e in result if e.tier == tier or tier in e.tags]
        if tags:
            result = [e for e in result if any(t in e.tags for t in tags)]
        return result

    def list_all(self) -> dict[str, list[Element]]:
        """List all elements grouped by type."""
        return {et: self.list_type(et) for et in ELEMENT_ORDER}


# ═══════════════════════════════════════════════════════════════════════════
# Recipe Loader
# ═══════════════════════════════════════════════════════════════════════════

def load_recipe(recipe_path: Path) -> Recipe:
    """Load a recipe YAML file."""
    data = yaml.safe_load(recipe_path.read_text(encoding="utf-8"))
    return Recipe(
        recipe=data.get("recipe", recipe_path.stem),
        name_zh=data.get("name_zh", ""),
        description=data.get("description", ""),
        elements=data.get("elements", {}),
        overrides=data.get("overrides", {}),
        params=data.get("params", {}),
        negative_prompt=data.get("negative_prompt", ""),
    )


# ═══════════════════════════════════════════════════════════════════════════
# Character card extraction (legacy support)
# ═══════════════════════════════════════════════════════════════════════════

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


# ═══════════════════════════════════════════════════════════════════════════
# Prompt Composer (element-based)
# ═══════════════════════════════════════════════════════════════════════════

def resolve_subject_prompt(
    loader: ElementLoader,
    subject_spec: str | dict,
) -> str:
    """Resolve the subject element to a prompt string.

    subject_spec can be:
      - a string id (looked up in elements/subject/)
      - a dict with {source: "character", path: "..."}
      - a dict with {source: "element", id: "..."}
      - a dict with {source: "inline", prompt: "..."}
    """
    if isinstance(subject_spec, str):
        # Try as element id first
        el = loader.get("subject", subject_spec)
        if el:
            # If it references a character card, load the modular block
            source = el.extra.get("source", "inline")
            if source == "character":
                char_path = el.extra.get("character_path", "")
                if char_path:
                    full_path = _PKG_DIR / char_path
                    if full_path.is_file():
                        md = full_path.read_text(encoding="utf-8")
                        data = extract_sections_from_markdown(md)
                        if data["modular_block"]:
                            return data["modular_block"]
            return el.prompt
        # Try as a character card path
        char_path = Path(subject_spec)
        if not char_path.is_file():
            char_path = _PKG_DIR / subject_spec
        if char_path.is_file() and char_path.suffix == ".md":
            md = char_path.read_text(encoding="utf-8")
            data = extract_sections_from_markdown(md)
            return data["modular_block"] or data["benchmark_prompt"]
        return subject_spec  # Use as literal text

    if isinstance(subject_spec, dict):
        source = subject_spec.get("source", "inline")
        if source == "character":
            path = subject_spec.get("path", "")
            full_path = _PKG_DIR / path if path else None
            if full_path and full_path.is_file():
                md = full_path.read_text(encoding="utf-8")
                data = extract_sections_from_markdown(md)
                return data["modular_block"] or data["benchmark_prompt"]
        elif source == "element":
            el_id = subject_spec.get("id", "")
            el = loader.get("subject", el_id)
            return el.prompt if el else ""
        else:  # inline
            return subject_spec.get("prompt", "")

    return ""


def compose_from_elements(
    loader: ElementLoader,
    element_ids: dict[str, Any],
    overrides: dict[str, str] | None = None,
) -> str:
    """Compose a full prompt from element ids in seven-segment order.

    Args:
        loader: Element loader instance
        element_ids: {element_type: element_id_or_spec}
        overrides: Optional {element_type.field: value} overrides

    Returns:
        The composed prompt string.
    """
    overrides = overrides or {}
    parts: list[str] = []

    for etype in ELEMENT_ORDER:
        spec = element_ids.get(etype)
        if not spec:
            continue

        if etype == "subject":
            prompt_text = resolve_subject_prompt(loader, spec)
        else:
            el = loader.get(etype, spec) if isinstance(spec, str) else None
            if el:
                prompt_text = el.prompt
            else:
                prompt_text = str(spec) if spec else ""

        # Apply overrides
        override_key = f"{etype}.prompt"
        if override_key in overrides:
            prompt_text = overrides[override_key]

        # For setting elements, also append lighting
        if etype == "setting" and isinstance(spec, str):
            el = loader.get("setting", spec)
            if el and el.lighting:
                lighting_override = overrides.get("setting.lighting")
                lighting = lighting_override if lighting_override else el.lighting
                prompt_text = f"{prompt_text.rstrip('.')}. {lighting}"

        if prompt_text:
            parts.append(prompt_text.strip().rstrip(",").rstrip("."))

    # Join with ". " separator for natural flow
    composed = ". ".join(parts)
    if composed and not composed.endswith("."):
        composed += "."
    return composed


# ═══════════════════════════════════════════════════════════════════════════
# Compatibility Checker
# ═══════════════════════════════════════════════════════════════════════════

def check_compatibility(loader: ElementLoader, element_ids: dict[str, str]) -> list[str]:
    """Check compatibility between selected elements. Returns warnings."""
    warnings: list[str] = []

    for etype, eid in element_ids.items():
        if not eid:
            continue
        el = loader.get(etype, eid)
        if not el:
            continue

        compat = el.compatibility
        if not compat:
            continue

        # Check avoid_with
        avoid = compat.get("avoid_with", [])
        for other_type, other_id in element_ids.items():
            if other_type == etype or not other_id:
                continue
            if other_id in avoid:
                warnings.append(
                    f"⚠ {etype}/{eid} declares avoid_with: {other_id} "
                    f"(used as {other_type})"
                )

        # Check best_with recommendations
        for bw_key, bw_list in compat.items():
            if not bw_key.startswith("best_with_"):
                continue
            target_type = bw_key.replace("best_with_", "").rstrip("s")  # best_with_poses -> pose
            # Map plural to singular
            type_map = {"camera": "camera", "pose": "pose", "setting": "setting"}
            target_type = type_map.get(target_type, target_type)
            if target_type in element_ids and element_ids[target_type]:
                selected = element_ids[target_type]
                if isinstance(bw_list, list) and selected not in bw_list and bw_list:
                    warnings.append(
                        f"ℹ {etype}/{eid} recommends {target_type} in "
                        f"{bw_list}, but '{selected}' is selected"
                    )

    return warnings


# ═══════════════════════════════════════════════════════════════════════════
# List / Display
# ═══════════════════════════════════════════════════════════════════════════

def print_element_list(loader: ElementLoader, element_type: str, tier: str = "", tags: list[str] | None = None):
    """Print a formatted list of elements."""
    if element_type == "all":
        for et in ELEMENT_ORDER:
            print(f"\n{'─' * 60}")
            print(f"  {et.upper()}")
            print(f"{'─' * 60}")
            print_element_list(loader, et, tier, tags)
        return

    elements = loader.list_type(element_type, tier, tags)
    if not elements:
        print(f"  (no {element_type} elements found)")
        return

    for el in elements:
        tier_str = f" [{el.tier}]" if el.tier else ""
        tags_str = f"  tags: {', '.join(el.tags)}" if el.tags else ""
        print(f"  {el.id:<30s} {el.name_zh}{tier_str}")
        if tags_str:
            print(f"    {tags_str}")


# ═══════════════════════════════════════════════════════════════════════════
# CLI
# ═══════════════════════════════════════════════════════════════════════════

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compose prompts from modular seven-element YAML files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    # ── Legacy mode ──
    legacy = parser.add_argument_group("Legacy mode (backward-compatible)")
    legacy.add_argument("--character", "-c", default="", help="Path to character card markdown file")
    legacy.add_argument("--scene", "-s", default="", help="Path to scene prompt text file")
    legacy.add_argument("--show-char", action="store_true", help="Display extracted character card info and exit")

    # ── Recipe mode ──
    recipe_group = parser.add_argument_group("Recipe mode")
    recipe_group.add_argument("--recipe", "-r", default="", help="Path to recipe YAML file")

    # ── Element mode ──
    elem_group = parser.add_argument_group("Element mode (seven elements)")
    elem_group.add_argument("--camera", default="", help="Camera element id")
    elem_group.add_argument("--subject", default="", help="Subject element id or character card path")
    elem_group.add_argument("--pose", default="", help="Pose element id")
    elem_group.add_argument("--setting", default="", help="Setting element id")
    elem_group.add_argument("--skin", default="", help="Skin element id")
    elem_group.add_argument("--anatomy", default="", help="Anatomy element id")
    elem_group.add_argument("--finish", default="", help="Finish element id")

    # ── List / check ──
    util_group = parser.add_argument_group("Utilities")
    util_group.add_argument("--list", default="", metavar="TYPE",
                            help="List available elements (camera|pose|setting|skin|anatomy|finish|subject|all)")
    util_group.add_argument("--tier", default="", help="Filter by tier (L0/L1/L2/L3) when listing")
    util_group.add_argument("--tags", default="", help="Filter by tags (comma-separated) when listing")
    util_group.add_argument("--check-compat", action="store_true", help="Check compatibility of selected elements")

    # ── Execution ──
    exec_group = parser.add_argument_group("Execution options")
    exec_group.add_argument("--run", action="store_true", help="Directly invoke scripts/qwen_pose_test.py")
    exec_group.add_argument("--out", default="", help="Output image file path if --run is specified")
    exec_group.add_argument("--seed", type=int, default=None, help="Random seed (overrides recipe)")
    exec_group.add_argument("--steps", type=int, default=None, help="Sampling steps (overrides recipe)")
    exec_group.add_argument("--cfg", type=float, default=None, help="CFG scale (overrides recipe)")
    exec_group.add_argument("--lora", default="", help="LoRA model name (overrides recipe)")
    exec_group.add_argument("--lora-strength", type=float, default=None, help="LoRA weight (overrides recipe)")

    args = parser.parse_args()

    # ── Utility: --list ──
    if args.list:
        if yaml is None:
            print("Error: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
            return 1
        loader = ElementLoader()
        tag_list = [t.strip() for t in args.tags.split(",") if t.strip()] if args.tags else None
        print_element_list(loader, args.list, args.tier, tag_list)
        return 0

    # ── Utility: --check-compat ──
    if args.check_compat:
        if yaml is None:
            print("Error: PyYAML required. Install with: pip install pyyaml", file=sys.stderr)
            return 1
        loader = ElementLoader()
        ids = {
            "camera": args.camera, "subject": args.subject, "pose": args.pose,
            "setting": args.setting, "skin": args.skin, "anatomy": args.anatomy,
            "finish": args.finish,
        }
        ids = {k: v for k, v in ids.items() if v}
        warnings = check_compatibility(loader, ids)
        if warnings:
            print("Compatibility warnings:")
            for w in warnings:
                print(f"  {w}")
        else:
            print("✓ All selected elements are compatible.")
        return 0

    # ── Determine mode ──
    has_legacy = bool(args.character)
    has_recipe = bool(args.recipe)
    has_elements = any([args.camera, args.subject, args.pose, args.setting,
                        args.skin, args.anatomy, args.finish])

    # ╔═══════════════════════════════════════════════════════════════════╗
    # ║  MODE 1: Legacy (--character + --scene)                         ║
    # ╚═══════════════════════════════════════════════════════════════════╝
    if has_legacy and not has_recipe and not has_elements:
        return _legacy_mode(args)

    # ╔═══════════════════════════════════════════════════════════════════╗
    # ║  MODE 2 & 3: Recipe and/or Element mode                         ║
    # ╚═══════════════════════════════════════════════════════════════════╝
    if yaml is None:
        print("Error: PyYAML required for recipe/element mode.\n"
              "Install with: pip install pyyaml", file=sys.stderr)
        return 1

    loader = ElementLoader()

    # Start with recipe defaults if provided
    recipe: Recipe | None = None
    element_ids: dict[str, Any] = {}
    overrides: dict[str, str] = {}
    params: dict[str, Any] = {
        "steps": 45, "cfg": 2.5, "sampler": "er_sde", "scheduler": "beta",
        "seed": 80964, "size": "1152x1728",
        "lora": "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors",
        "lora_strength": 1.0,
    }
    negative_prompt = ""

    if has_recipe:
        recipe_path = Path(args.recipe)
        if not recipe_path.is_file():
            recipe_path = _PKG_DIR / args.recipe
        if not recipe_path.is_file():
            print(f"Error: Recipe file not found: {args.recipe}", file=sys.stderr)
            return 1
        recipe = load_recipe(recipe_path)
        element_ids = dict(recipe.elements)
        overrides = dict(recipe.overrides)
        if recipe.params:
            params.update(recipe.params)
        negative_prompt = recipe.negative_prompt

    # CLI element flags override recipe elements
    cli_elements = {
        "camera": args.camera, "subject": args.subject, "pose": args.pose,
        "setting": args.setting, "skin": args.skin, "anatomy": args.anatomy,
        "finish": args.finish,
    }
    for k, v in cli_elements.items():
        if v:
            element_ids[k] = v

    # CLI params override recipe params
    if args.seed is not None:
        params["seed"] = args.seed
    if args.steps is not None:
        params["steps"] = args.steps
    if args.cfg is not None:
        params["cfg"] = args.cfg
    if args.lora:
        params["lora"] = args.lora
    if args.lora_strength is not None:
        params["lora_strength"] = args.lora_strength

    if not element_ids:
        parser.print_help()
        return 1

    # Compose the prompt
    final_prompt = compose_from_elements(loader, element_ids, overrides)

    # Compatibility check (non-fatal)
    str_ids = {k: v for k, v in element_ids.items() if isinstance(v, str)}
    compat_warnings = check_compatibility(loader, str_ids)

    # Display
    print("\n" + "=" * 60)
    if recipe:
        print(f"RECIPE: {recipe.name_zh} ({recipe.recipe})")
    print("COMPOSED PROMPT:")
    print("=" * 60)
    print(final_prompt)
    if negative_prompt:
        print("\nNEGATIVE PROMPT:")
        print(negative_prompt)
    if compat_warnings:
        print("\nCOMPATIBILITY NOTES:")
        for w in compat_warnings:
            print(f"  {w}")
    print("\nPARAMS:")
    for pk, pv in params.items():
        print(f"  {pk}: {pv}")
    print("=" * 60 + "\n")

    # Execute if --run
    if args.run:
        return _run_generation(final_prompt, negative_prompt, params, args.out, element_ids)

    return 0


def _legacy_mode(args) -> int:
    """Original --character + --scene workflow."""
    char_path = Path(args.character)
    if not char_path.is_file():
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
        params = {
            "steps": args.steps or 45,
            "cfg": args.cfg or 2.5,
            "sampler": "er_sde",
            "scheduler": "beta",
            "seed": args.seed or 80964,
            "size": "1152x1728",
            "lora": args.lora or "qwen2_1-femaledVaginus-nsfw-v1_3-fine_L22-31.safetensors",
            "lora_strength": args.lora_strength if args.lora_strength is not None else 1.0,
        }
        return _run_generation(final_prompt, final_neg, params, args.out,
                               {"subject": char_path.stem, "setting": scene_path.stem if args.scene else ""})

    return 0


def _run_generation(
    prompt: str,
    negative: str,
    params: dict[str, Any],
    out_path: str,
    element_ids: dict[str, Any],
) -> int:
    """Invoke qwen_pose_test.py with the composed prompt."""
    size = str(params.get("size", "1152x1728"))
    width, height = size.split("x")

    # Build a name from element ids
    name_parts = []
    for k in ["subject", "setting", "pose"]:
        v = element_ids.get(k)
        if isinstance(v, str) and v:
            name_parts.append(v)
        elif isinstance(v, dict):
            name_parts.append(v.get("id", v.get("path", "").split("/")[-1].replace(".md", "")))
    name = "_".join(name_parts) if name_parts else "composed"

    if not out_path:
        out_path = f"outputs/composed/{name}.png"

    cmd = [
        sys.executable,
        str(_PKG_DIR / "scripts" / "qwen_pose_test.py"),
        "--mode", "t2i",
        "--name", f"compose_{name}",
        "--prompt", prompt,
        "--seed", str(params.get("seed", 80964)),
        "--steps", str(params.get("steps", 45)),
        "--cfg", str(params.get("cfg", 2.5)),
        "--sampler", str(params.get("sampler", "er_sde")),
        "--scheduler", str(params.get("scheduler", "beta")),
        "--width", width,
        "--height", height,
        "--lora", str(params.get("lora", "")),
        "--lora-strength", str(params.get("lora_strength", 1.0)),
        "--out", out_path,
    ]
    if negative:
        cmd.extend(["--negative", negative])

    print(f"Running command:\n{' '.join(cmd)}\n")
    return subprocess.call(cmd)


if __name__ == "__main__":
    sys.exit(main())
