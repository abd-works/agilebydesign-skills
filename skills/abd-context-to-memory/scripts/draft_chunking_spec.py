"""
Structural scan of markdown sources → draft context_chunking_spec.yaml.

Usage:
  python draft_chunking_spec.py --path <source_folder>

Scans all .md files under <source_folder>/markdown/ (or <source_folder> if no
markdown/ subfolder), analyses heading structure, table density, slide markers,
section patterns, and noise indicators, then writes a draft
context_chunking_spec.yaml beside <source_folder>.

If the YAML already exists it is NOT overwritten — use --force to replace it.

The output spec has four required sections:
  section_boundaries  - regexes that start new major structural units
  splitting           - min/max sizes, table handling, heading split level
  defaults            - fallback evidence_type / modeling_kind
  taxonomy            - closed-world enums for validators

After this script runs, review and edit the YAML before running chunk_markdown.py.
"""

import re
import sys
from collections import Counter
from pathlib import Path

from _config import ROOT, ensure_root

ensure_root()

SPEC_FILENAME = "context_chunking_spec.yaml"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _collect_md_files(src: Path) -> list[Path]:
    """Collect .md sources: prefer <src>/markdown/, fall back to <src> itself."""
    markdown_dir = src / "markdown"
    scan = markdown_dir if markdown_dir.is_dir() else src
    return sorted(
        f for f in scan.rglob("*.md")
        if "images" not in f.parts
        and not re.search(r"__(?:slide|section|page)_\d+\.md$", f.name, re.IGNORECASE)
        and "memory" not in [p.casefold() for p in f.relative_to(scan).parts[:-1]]
    )


def _analyse_file(path: Path) -> dict:
    """Return structural metrics for a single markdown file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return {}

    lines = text.splitlines()

    # Heading levels present
    heading_levels: Counter = Counter()
    for line in lines:
        m = re.match(r"^(#{1,6})\s", line)
        if m:
            heading_levels[len(m.group(1))] += 1

    # Tables (lines starting with |)
    table_lines = sum(1 for l in lines if l.startswith("|"))
    table_count = len(re.findall(r"(?m)^\|", text)) and len(
        re.findall(r"(?m)(?:^\|[^\n]*\n){2,}", text)
    )

    # Slides
    is_slide_deck = bool(re.search(r"<!-- Slide number: \d+ -->", text))

    # Chapter / section markers (bare all-caps lines typical in PDF exports)
    chapter_markers = [
        l.strip() for l in lines
        if re.match(r"^CHAPTER\s+\d+\b", l, re.IGNORECASE)
    ]
    section_markers = [
        l.strip() for l in lines
        if re.match(r"^(?:SECTION|PART|APPENDIX)\s+", l, re.IGNORECASE)
    ]

    # Noise indicators
    noise_patterns = sum(
        1 for l in lines
        if re.match(r"^\d+$", l.strip())          # bare page numbers
        or re.match(r"^page\s+\d+", l, re.IGNORECASE)
    )

    # Code fences
    code_fence_count = len(re.findall(r"^```", text, re.MULTILINE))

    return {
        "line_count": len(lines),
        "heading_levels": dict(heading_levels),
        "table_line_count": table_lines,
        "is_slide_deck": is_slide_deck,
        "chapter_markers": chapter_markers[:5],
        "section_markers": section_markers[:5],
        "noise_lines": noise_patterns,
        "code_fence_count": code_fence_count,
    }


def _build_spec(analyses: list[dict], src: Path) -> dict:
    """Derive sensible defaults from aggregate structural metrics."""
    total_files = len(analyses)
    if total_files == 0:
        return _default_spec()

    any_slides = any(a.get("is_slide_deck") for a in analyses)
    any_chapter = any(a.get("chapter_markers") for a in analyses)
    any_section_marker = any(a.get("section_markers") for a in analyses)
    all_heading_levels: Counter = Counter()
    for a in analyses:
        all_heading_levels.update(a.get("heading_levels", {}))

    has_h1 = all_heading_levels.get(1, 0) > 0
    has_h2 = all_heading_levels.get(2, 0) > 0
    has_h3 = all_heading_levels.get(3, 0) > 0

    total_lines = sum(a.get("line_count", 0) for a in analyses)
    avg_lines = total_lines // max(total_files, 1)

    # --- section_boundaries ---
    chapter_break_regex = ""
    section_break_regex = ""

    if any_chapter:
        chapter_break_regex = r"^CHAPTER\s+\d+"
    elif has_h1:
        chapter_break_regex = r"^#\s+"

    if any_section_marker:
        section_break_regex = r"^(?:SECTION|PART|APPENDIX)\s+"
    elif has_h2:
        section_break_regex = r"^##\s+"
    elif has_h1 and not chapter_break_regex:
        section_break_regex = r"^#\s+"

    all_caps_standalone = any_chapter or any_section_marker

    # --- splitting ---
    # Larger files → allow bigger chunks to preserve coherence
    if avg_lines > 500:
        min_chars, max_chars = 400, 8000
    elif avg_lines > 100:
        min_chars, max_chars = 300, 4000
    else:
        min_chars, max_chars = 150, 2000

    split_on_heading_level = 2
    if has_h3 and all_heading_levels.get(3, 0) > all_heading_levels.get(2, 0):
        split_on_heading_level = 3

    any_tables = any(a.get("table_line_count", 0) > 0 for a in analyses)

    # --- defaults ---
    # Slide decks are typically examples; structured handbooks default to rules
    if any_slides:
        default_evidence_type = "example"
        default_modeling_kind = "example"
    else:
        default_evidence_type = "rule"
        default_modeling_kind = "rule"

    return {
        "section_boundaries": {
            "chapter_break_regex": chapter_break_regex,
            "section_break_regex": section_break_regex,
            "all_caps_standalone": all_caps_standalone,
        },
        "splitting": {
            "min_chunk_chars": min_chars,
            "max_chunk_chars": max_chars,
            "keep_markdown_tables_intact": any_tables,
            "split_on_heading_level": split_on_heading_level,
        },
        "defaults": {
            "evidence_type": default_evidence_type,
            "modeling_kind": default_modeling_kind,
        },
        "taxonomy": {
            "evidence_type": ["definition", "rule", "example", "table", "metadata_noise", "mixed"],
            "modeling_kind": ["definition", "rule", "example", "noise", "structural_only"],
        },
    }


def _default_spec() -> dict:
    return {
        "section_boundaries": {
            "chapter_break_regex": r"^#\s+",
            "section_break_regex": r"^##\s+",
            "all_caps_standalone": False,
        },
        "splitting": {
            "min_chunk_chars": 300,
            "max_chunk_chars": 4000,
            "keep_markdown_tables_intact": True,
            "split_on_heading_level": 2,
        },
        "defaults": {
            "evidence_type": "rule",
            "modeling_kind": "rule",
        },
        "taxonomy": {
            "evidence_type": ["definition", "rule", "example", "table", "metadata_noise", "mixed"],
            "modeling_kind": ["definition", "rule", "example", "noise", "structural_only"],
        },
    }


# ---------------------------------------------------------------------------
# YAML serialiser (no dependency on PyYAML for portability)
# ---------------------------------------------------------------------------

def _to_yaml_str(value, indent: int = 0) -> str:
    pad = "  " * indent
    if isinstance(value, dict):
        lines = []
        for k, v in value.items():
            if isinstance(v, (dict, list)):
                lines.append(f"{pad}{k}:")
                lines.append(_to_yaml_str(v, indent + 1))
            else:
                lines.append(f"{pad}{k}: {_yaml_scalar(v)}")
        return "\n".join(lines)
    elif isinstance(value, list):
        items = ", ".join(_yaml_scalar(i) for i in value)
        return f"{pad}[{items}]"
    else:
        return f"{pad}{_yaml_scalar(value)}"


def _yaml_scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if v == "":
        return '""'
    # Quote strings that look like regexes or contain special YAML chars
    if any(c in str(v) for c in r':{}[]|>&*!,#?-"'):
        escaped = str(v).replace('"', '\\"')
        return f'"{escaped}"'
    return str(v)


def _build_yaml_document(spec: dict, src: Path, files: list[Path]) -> str:
    lines = [
        "# context_chunking_spec.yaml — drafted by draft_chunking_spec.py",
        "# Review and edit before running chunk_markdown.py.",
        f"# Sources scanned: {len(files)} markdown file(s) under {src.name}/",
        "#",
        "# section_boundaries: regexes that start a new major structural unit.",
        "# splitting: size limits and table handling for the chunk emitter.",
        "# defaults: fallback labels applied by the emitter when heuristics don't fire.",
        "# taxonomy: closed-world allowed values — validators enforce these.",
        "",
    ]

    section_b = spec["section_boundaries"]
    splitting = spec["splitting"]
    defaults = spec["defaults"]
    taxonomy = spec["taxonomy"]

    lines.append("section_boundaries:")
    lines.append(f'  chapter_break_regex: "{section_b["chapter_break_regex"]}"')
    lines.append(f'  section_break_regex: "{section_b["section_break_regex"]}"')
    lines.append(f"  all_caps_standalone: {_yaml_scalar(section_b['all_caps_standalone'])}")
    lines.append("")

    lines.append("splitting:")
    lines.append(f"  min_chunk_chars: {splitting['min_chunk_chars']}")
    lines.append(f"  max_chunk_chars: {splitting['max_chunk_chars']}")
    lines.append(f"  keep_markdown_tables_intact: {_yaml_scalar(splitting['keep_markdown_tables_intact'])}")
    lines.append(f"  split_on_heading_level: {splitting['split_on_heading_level']}")
    lines.append("")

    lines.append("defaults:")
    lines.append(f"  evidence_type: {defaults['evidence_type']}")
    lines.append(f"  modeling_kind: {defaults['modeling_kind']}")
    lines.append("")

    lines.append("taxonomy:")
    et = ", ".join(taxonomy["evidence_type"])
    mk = ", ".join(taxonomy["modeling_kind"])
    lines.append(f"  evidence_type: [{et}]")
    lines.append(f"  modeling_kind: [{mk}]")
    lines.append("")

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Structural report (printed to stdout for human review)
# ---------------------------------------------------------------------------

def _print_report(analyses: list[dict], spec: dict, files: list[Path]):
    print(f"\n{'='*60}")
    print("  STRUCTURAL SCAN REPORT")
    print(f"{'='*60}")
    print(f"  Files scanned: {len(files)}")

    slide_files = [f for f, a in zip(files, analyses) if a.get("is_slide_deck")]
    if slide_files:
        print(f"  Slide decks:   {len(slide_files)} ({', '.join(f.name for f in slide_files[:3])}{'...' if len(slide_files) > 3 else ''})")

    all_levels: Counter = Counter()
    for a in analyses:
        all_levels.update(a.get("heading_levels", {}))
    if all_levels:
        level_summary = ", ".join(f"H{k}×{v}" for k, v in sorted(all_levels.items()))
        print(f"  Headings:      {level_summary}")

    chapter_files = [f for f, a in zip(files, analyses) if a.get("chapter_markers")]
    if chapter_files:
        print(f"  Chapter markers found in: {', '.join(f.name for f in chapter_files[:3])}")

    table_files = [(f, a) for f, a in zip(files, analyses) if a.get("table_line_count", 0) > 0]
    if table_files:
        print(f"  Tables present in: {len(table_files)} file(s)")

    noise_files = [(f, a) for f, a in zip(files, analyses) if a.get("noise_lines", 0) > 5]
    if noise_files:
        print(f"  Possible noise (page numbers etc.) in: {len(noise_files)} file(s) — check metadata_noise")

    print(f"\n  DRAFTED SPEC SUMMARY")
    print(f"  chapter_break_regex : {spec['section_boundaries']['chapter_break_regex'] or '(none)'}")
    print(f"  section_break_regex : {spec['section_boundaries']['section_break_regex'] or '(none)'}")
    print(f"  split_on_heading    : H{spec['splitting']['split_on_heading_level']}")
    print(f"  chunk_chars         : {spec['splitting']['min_chunk_chars']}–{spec['splitting']['max_chunk_chars']}")
    print(f"  default labels      : evidence_type={spec['defaults']['evidence_type']}  modeling_kind={spec['defaults']['modeling_kind']}")

    print(f"\n  ASSUMPTIONS / REVIEW POINTS")
    if not spec["section_boundaries"]["chapter_break_regex"]:
        print("  ⚠  No chapter boundary detected — add chapter_break_regex manually if applicable.")
    if not spec["section_boundaries"]["section_break_regex"]:
        print("  ⚠  No section boundary detected — add section_break_regex manually.")
    if not any(a.get("heading_levels") for a in analyses):
        print("  ⚠  No markdown headings found — chunking will use section_markers or whole-file fallback.")
    print("  ✎  Review taxonomy enums; add domain-specific values if needed.")
    print("  ✎  Verify min/max chunk sizes against longest tables and shortest meaningful units.")
    print(f"{'='*60}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def _get_arg(flag: str) -> str | None:
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return None


def draft_spec(src: Path, force: bool = False) -> Path | None:
    """
    Scan markdown under src, draft context_chunking_spec.yaml beside src.
    Returns the spec path if written (or already exists and force=False).
    """
    spec_path = src / SPEC_FILENAME

    if spec_path.exists() and not force:
        print(f"Spec already exists: {spec_path}")
        print("  Use --force to overwrite, or edit it directly.")
        return spec_path

    files = _collect_md_files(src)
    if not files:
        print(f"No markdown files found under {src}.")
        print("Run convert_to_markdown.py first.")
        return None

    print(f"Scanning {len(files)} markdown file(s) in {src.name}/...")
    analyses = []
    for f in files:
        analyses.append(_analyse_file(f))

    spec = _build_spec(analyses, src)
    _print_report(analyses, spec, files)

    yaml_text = _build_yaml_document(spec, src, files)
    spec_path.write_text(yaml_text, encoding="utf-8")
    print(f"Spec written: {spec_path}")
    print("NEXT: Review context_chunking_spec.yaml, then run chunk_markdown.py.")
    return spec_path


def main():
    path_arg = _get_arg("--path")
    force = "--force" in sys.argv

    if not path_arg:
        print("Usage: python draft_chunking_spec.py --path <source_folder> [--force]")
        sys.exit(1)

    src = Path(path_arg)
    if not src.is_absolute():
        src = ROOT / src
    if not src.exists():
        print(f"ERROR: folder not found: {src}")
        sys.exit(1)

    result = draft_spec(src, force=force)
    if result is None:
        sys.exit(1)


if __name__ == "__main__":
    main()
