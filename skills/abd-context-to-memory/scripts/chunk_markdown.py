"""
Chunk converted markdown into smaller pieces for agent memory.

Usage:
  python chunk_markdown.py --path <source_folder> [--memory <memory_name>]
  python chunk_markdown.py --path <source_folder> --output <output_dir>

Run from workspace root. Reads .md from source folder, writes chunked output to:
  --output <dir>   : exact directory (absolute or relative to cwd)
  --memory <name>  : memory/<name>/ under workspace root (default)
Run convert_to_markdown.py first. Excludes chunked output (__slide_, __section_) from input.

**Sources:** For each logical document (same folder + stem), prefer ``<topic>/markdown/.../<stem>.md``
(parallel tree), then legacy ``.../markdown/<stem>.md`` beside originals, then sibling ``.../<stem>.md``.
Never duplicate chunks. **Output:** Chunks go under ``memory/`` mirroring the source tree **without**
a ``markdown`` path segment (e.g. ``markdown/notes/foo.md`` -> ``memory/notes/foo__slide_01.md``).

**Layout:** With ``--output <source>/memory``, markdown under ``<source>/memory/`` is never input
(output only).

**Folder named ``context``:** Pass ``--path`` as the **project root** (parent of ``context``) and
``--output`` to ``<project>/memory/context`` so converted markdown under ``<project>/markdown/`` is
found. (``index_memory`` does this automatically.)

**Chunking spec:** If ``context_chunking_spec.yaml`` exists beside ``--path``, its ``section_boundaries``,
``splitting``, ``defaults``, and ``taxonomy`` override built-in heuristics. Chunks written when the spec
is active include YAML front matter with ``evidence_type`` and ``modeling_kind`` labels.
Run ``draft_chunking_spec.py --path <folder>`` to generate the spec before chunking.
"""

import re
import sys
from pathlib import Path
from typing import Any

from _config import ROOT, MEMORY, ASSETS, ensure_root

ensure_root()
MIN_CHUNK_LINES = 5
SPEC_FILENAME = "context_chunking_spec.yaml"


# ---------------------------------------------------------------------------
# Chunking spec loading
# ---------------------------------------------------------------------------

def _load_spec(src_root: Path) -> dict[str, Any] | None:
    """Load context_chunking_spec.yaml from src_root if present. Returns parsed dict or None."""
    spec_path = src_root / SPEC_FILENAME
    if not spec_path.exists():
        return None
    try:
        return _parse_yaml(spec_path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  Warning: could not parse {SPEC_FILENAME}: {e}")
        return None


def _parse_yaml(text: str) -> dict[str, Any]:
    """Minimal YAML parser for the spec structure (avoids PyYAML dependency)."""
    result: dict[str, Any] = {}
    current_section: str | None = None
    current_dict: dict[str, Any] = {}

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue

        # Top-level key (no leading space)
        if not raw_line.startswith(" ") and ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "" or val.startswith("#"):
                if current_section:
                    result[current_section] = current_dict
                current_section = key
                current_dict = {}
            else:
                if current_section:
                    result[current_section] = current_dict
                    current_section = None
                    current_dict = {}
                result[key] = _parse_scalar(val)
            continue

        # Indented key under current section
        if current_section and line.lstrip():
            stripped = line.lstrip()
            if ":" in stripped:
                k, _, v = stripped.partition(":")
                k = k.strip()
                v = v.strip()
                if v == "" or v.startswith("#"):
                    continue
                current_dict[k] = _parse_scalar(v)

    if current_section:
        result[current_section] = current_dict

    return result


def _parse_scalar(val: str) -> Any:
    """Parse a YAML scalar: bool, int, list, or string."""
    val = val.split("#")[0].strip()  # strip inline comments
    if val.lower() == "true":
        return True
    if val.lower() == "false":
        return False
    try:
        return int(val)
    except ValueError:
        pass
    if val.startswith("[") and val.endswith("]"):
        inner = val[1:-1]
        return [item.strip().strip('"').strip("'") for item in inner.split(",") if item.strip()]
    # Strip surrounding quotes
    if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
        return val[1:-1]
    return val


def _spec_section_break_regex(spec: dict) -> re.Pattern | None:
    sb = spec.get("section_boundaries", {})
    chapter = sb.get("chapter_break_regex", "")
    section = sb.get("section_break_regex", "")
    patterns = [p for p in [chapter, section] if p]
    if not patterns:
        return None
    combined = "|".join(f"(?:{p})" for p in patterns)
    try:
        return re.compile(combined, re.IGNORECASE)
    except re.error:
        return None


def _spec_min_lines(spec: dict) -> int:
    splitting = spec.get("splitting", {})
    min_chars = splitting.get("min_chunk_chars", 150)
    return max(3, min_chars // 80)  # rough chars-to-lines conversion


def _spec_max_lines(spec: dict) -> int:
    splitting = spec.get("splitting", {})
    max_chars = splitting.get("max_chunk_chars", 4000)
    return max_chars // 60


def _spec_split_heading_level(spec: dict) -> int:
    return spec.get("splitting", {}).get("split_on_heading_level", 2)


def _spec_defaults(spec: dict) -> tuple[str, str]:
    d = spec.get("defaults", {})
    return d.get("evidence_type", "rule"), d.get("modeling_kind", "rule")


def _find_image_refs(text: str) -> list[str]:
    return re.findall(r"!\[[^\]]*\]\(<?([^)>]+)>?\)", text)


def _copy_images(refs: list[str], src_base: Path, dst_base: Path):
    import shutil
    for ref in refs:
        src = src_base / ref
        if not src.exists():
            continue
        dst = dst_base / ref
        dst.parent.mkdir(parents=True, exist_ok=True)
        if not dst.exists():
            shutil.copy2(str(src), str(dst))


def _chunk_by_slides(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"(<!-- Slide number: \d+ -->)", text)
    chunks, current_label, current_lines = [], "preamble", []

    for part in parts:
        m = re.match(r"<!-- Slide number: (\d+) -->", part)
        if m:
            if current_lines and "".join(current_lines).strip():
                chunks.append((current_label, "".join(current_lines)))
            current_label = f"slide_{int(m.group(1)):02d}"
            current_lines = [part]
        else:
            current_lines.append(part)

    if current_lines and "".join(current_lines).strip():
        chunks.append((current_label, "".join(current_lines)))
    return chunks


def _chunk_by_headings(text: str, heading_level: int = 2) -> list[tuple[str, str]]:
    pat = re.compile(r"^#{1," + str(heading_level) + r"}\s", re.MULTILINE)
    lines = text.split("\n")
    chunks, current_lines, chunk_idx = [], [], 0

    for line in lines:
        if pat.match(line) and len(current_lines) >= MIN_CHUNK_LINES:
            chunks.append((f"section_{chunk_idx:02d}", "\n".join(current_lines)))
            current_lines, chunk_idx = [], chunk_idx + 1
        current_lines.append(line)

    if current_lines:
        chunks.append((f"section_{chunk_idx:02d}", "\n".join(current_lines)))
    return chunks


def _chunk_by_section_markers(text: str, section_pat: re.Pattern | None = None) -> list[tuple[str, str]]:
    """Split on CHAPTER, INTRODUCTION, or similar section markers (for PDFs without # headers)."""
    lines = text.split("\n")
    chunks, current_lines, chunk_idx = [], [], 0
    if section_pat is None:
        section_pat = re.compile(r"^CHAPTER\s+\d+\b", re.IGNORECASE)

    for line in lines:
        if section_pat.search(line) and len(current_lines) >= MIN_CHUNK_LINES:
            chunks.append((f"section_{chunk_idx:02d}", "\n".join(current_lines)))
            current_lines, chunk_idx = [], chunk_idx + 1
        current_lines.append(line)

    if current_lines:
        chunks.append((f"section_{chunk_idx:02d}", "\n".join(current_lines)))
    return chunks


def _has_markdown_headings(text: str) -> bool:
    return bool(re.search(r"^#{1,2}\s", text, re.MULTILINE))


def _is_slide_deck(text: str) -> bool:
    return bool(re.search(r"<!-- Slide number: \d+ -->", text))


def _is_chunked_output(path: Path) -> bool:
    """True if file is chunked output (__slide_NN, __section_NN)."""
    return bool(re.search(r"__(?:slide|section|page)_\d+\.md$", path.name, re.IGNORECASE))


def _is_under_source_memory_tree(md_path: Path, src_root: Path) -> bool:
    """True if md_path is inside <src_root>/memory/ (chunk output tree — not convert input)."""
    try:
        rel = md_path.relative_to(src_root.resolve())
    except ValueError:
        return False
    if not rel.parts:
        return False
    return rel.parts[0].casefold() == "memory"


def _is_under_assets_rag_tree(md_path: Path, src_root: Path) -> bool:
    """True if under <src_root>/assets/rag/ (vector index sidecar — not source content)."""
    try:
        rel = md_path.relative_to(src_root.resolve())
    except ValueError:
        return False
    parts = [p.casefold() for p in rel.parts]
    return len(parts) >= 2 and parts[0] == "assets" and parts[1] == "rag"


def _rel_has_markdown_dir(rel: Path) -> bool:
    """True if any directory segment (not the filename) is named markdown."""
    parts = rel.parts
    return len(parts) > 1 and any(p.casefold() == "markdown" for p in parts[:-1])


def _source_pick_priority(p: Path, src_root: Path) -> int:
    """Lower = preferred: parallel ``<root>/markdown/...`` first, then legacy nested ``.../markdown/``, then sibling."""
    rel = p.relative_to(src_root.resolve())
    parts = rel.parts
    if len(parts) >= 2 and parts[0].casefold() == "markdown":
        return 0
    if _rel_has_markdown_dir(rel):
        return 1
    return 2


def _logical_chunk_key(md_path: Path, src_root: Path) -> tuple[tuple[str, ...], str]:
    """(logical parent path under topic, stem) — same key for sibling .md and markdown/stem.md."""
    rel = md_path.relative_to(src_root.resolve())
    parts = list(rel.parts)
    stem = Path(parts[-1]).stem.casefold()
    dir_parts = parts[:-1]
    if dir_parts and dir_parts[0].casefold() == "markdown":
        dir_parts = dir_parts[1:]
    dir_parts = [p for p in dir_parts if p.casefold() != "markdown"]
    return (tuple(dir_parts), stem)


def _memory_output_parent(md_path: Path, src_root: Path) -> Path:
    """Parent path under chunk_base: mirror source but drop leading ``markdown`` and other ``markdown`` segments."""
    rel = md_path.relative_to(src_root.resolve())
    parts = list(rel.parts[:-1])
    if parts and parts[0].casefold() == "markdown":
        parts = parts[1:]
    parts = [p for p in parts if p.casefold() != "markdown"]
    return Path(*parts) if parts else Path(".")


def _select_chunk_sources(src_root: Path) -> list[Path]:
    """One .md per logical doc: prefer ``<root>/markdown/...``, then legacy ``.../markdown/``, else sibling."""
    src = src_root.resolve()
    candidates = sorted(
        f
        for f in src.rglob("*.md")
        if "images" not in f.parts
        and not _is_chunked_output(f)
        and not _is_under_source_memory_tree(f, src)
        and not _is_under_assets_rag_tree(f, src)
    )
    by_key: dict[tuple[tuple[str, ...], str], Path] = {}
    for f in candidates:
        k = _logical_chunk_key(f, src)
        old = by_key.get(k)
        if old is None or _source_pick_priority(f, src) < _source_pick_priority(old, src):
            by_key[k] = f
    return sorted(by_key.values(), key=lambda p: str(p.as_posix().lower()))


def _extract_source_ref(text: str) -> tuple[str | None, str | None]:
    m = re.search(r"<!--\s*Source:\s*([^|]+)\s*\|\s*([^>]+)\s*-->", text)
    return (m.group(1).strip(), m.group(2).strip()) if m else (None, None)


def _add_chunk_source_ref(content: str, source_path: str | None, source_url: str | None, location: str) -> str:
    if not source_path:
        return content
    loc = f", {location}" if location else ""
    url = f" | {source_url}" if source_url else ""
    return f"<!-- Source: {source_path}{loc}{url} -->\n\n" + content


def _build_front_matter(
    chunk_id: str,
    source_path: str | None,
    evidence_type: str,
    modeling_kind: str,
    section_path: list[str],
) -> str:
    """Produce YAML front matter block for a chunk when a spec is active."""
    lines = ["---"]
    lines.append(f"chunk_id: {chunk_id}")
    if source_path:
        lines.append("source:")
        lines.append(f"  canonical_path: {source_path}")
    lines.append(f"evidence_type: {evidence_type}")
    lines.append(f"modeling_kind: {modeling_kind}")
    if section_path:
        sections_yaml = ", ".join(f'"{s}"' for s in section_path)
        lines.append(f"section_path: [{sections_yaml}]")
    lines.append("---")
    return "\n".join(lines) + "\n\n"


def _extract_section_path(content: str) -> list[str]:
    """Extract heading breadcrumb from chunk content (first few headings)."""
    headings = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
    return [h.strip() for h in headings[:3]]


def chunk_file(
    md_path: Path,
    conv_root: Path,
    chunk_root: Path,
    spec: dict | None = None,
) -> int:
    text = md_path.read_text(encoding="utf-8")
    stem, source_path, source_url = md_path.stem, *_extract_source_ref(text)
    out_dir = chunk_root
    out_dir.mkdir(parents=True, exist_ok=True)

    use_spec = spec is not None
    if use_spec:
        section_pat = _spec_section_break_regex(spec)
        heading_level = _spec_split_heading_level(spec)
        default_et, default_mk = _spec_defaults(spec)
    else:
        section_pat = None
        heading_level = 2
        default_et = default_mk = ""

    if _is_slide_deck(text):
        chunks = _chunk_by_slides(text)
    elif text.count("\n") > 200:
        if _has_markdown_headings(text):
            chunks = _chunk_by_headings(text, heading_level=heading_level)
        elif section_pat:
            chunks = _chunk_by_section_markers(text, section_pat=section_pat)
        else:
            chunks = _chunk_by_section_markers(text)
    else:
        chunks = [(stem, text)]

    def _loc(label: str) -> str:
        if label.startswith("slide_"):
            return f"slide {int(label.split('_')[1])}"
        if label.startswith("section_"):
            return f"section {int(label.split('_')[1]) + 1}"
        return ""

    written = 0
    for label, content in chunks:
        if not content.strip():
            continue
        out_name = f"{stem}__{label}.md" if len(chunks) > 1 else f"{stem}.md"
        chunk_id = Path(out_name).stem  # filename stem without .md

        if use_spec:
            section_path = _extract_section_path(content)
            front = _build_front_matter(chunk_id, source_path, default_et, default_mk, section_path)
            # Strip any existing source comment to avoid duplication
            content_body = re.sub(r"<!--\s*Source:[^>]*-->\s*\n*", "", content).lstrip()
            final_content = front + content_body
        else:
            final_content = _add_chunk_source_ref(content, source_path, source_url, _loc(label))

        out = out_dir / out_name
        out.write_text(final_content, encoding="utf-8")
        for ref in _find_image_refs(final_content):
            _copy_images([ref], conv_root, chunk_root)
        written += 1
    return written


def _run_path_mode(source_path: str, memory_name_override: str | None = None, output_override: str | None = None) -> None:
    p = Path(source_path)
    if p.is_absolute():
        src_root = p
    else:
        under_assets = ASSETS / source_path
        under_root = ROOT / source_path
        if under_assets.exists():
            src_root = under_assets
        elif under_root.exists():
            src_root = under_root
        else:
            print(f"Path not found: {source_path}")
            return

    # When originals live in ``.../context/``, converted md is under ``../markdown/`` — scan project root.
    scan_root = src_root.parent if src_root.name.casefold() == "context" else src_root

    if output_override:
        chunk_base = Path(output_override)
        if not chunk_base.is_absolute():
            chunk_base = Path.cwd() / chunk_base
        dest = str(chunk_base)
    else:
        memory_name = memory_name_override or src_root.name
        chunk_base = MEMORY / memory_name
        dest = f"memory/{memory_name}/"

    # Load chunking spec if present
    spec = _load_spec(src_root)
    if spec:
        print(f"  Using chunking spec: {src_root / SPEC_FILENAME}")
        default_et, default_mk = _spec_defaults(spec)
        print(f"  Defaults: evidence_type={default_et}  modeling_kind={default_mk}")

    md_files = _select_chunk_sources(scan_root)
    if not md_files:
        print(f"No markdown in {scan_root}")
        print("Run convert_to_markdown.py --memory <path> first.")
        return

    print(f"Source: {scan_root}  ({len(md_files)} logical docs) -> {dest}\n")
    total = 0
    for i, f in enumerate(md_files, 1):
        conv_root = f.parent
        mem_parent = _memory_output_parent(f, scan_root)
        chunk_root = chunk_base / mem_parent
        rel = f.relative_to(scan_root)
        label = str(rel) if rel != Path(".") else f.name
        print(f"  [{i}/{len(md_files)}] {label} ... ", end="", flush=True)
        try:
            n = chunk_file(f, conv_root, chunk_root, spec=spec)
            total += n
            print(f"OK  ({n} chunks)")
        except Exception as e:
            print(f"FAIL  {e}")
    print(f"\nDone: {total} chunks.")


def _get_arg(flag: str) -> str | None:
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return None


def main():
    path_arg   = _get_arg("--path")
    memory_arg = _get_arg("--memory")
    output_arg = _get_arg("--output")
    if path_arg:
        _run_path_mode(path_arg, memory_name_override=memory_arg, output_override=output_arg)
        return
    if memory_arg:
        _run_path_mode(memory_arg)
        return
    print("Usage: python chunk_markdown.py --path <source_folder> [--memory <name> | --output <dir>]")


if __name__ == "__main__":
    main()
