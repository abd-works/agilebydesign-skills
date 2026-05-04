#!/usr/bin/env python3
"""Scan the skills tree and generate a categorised Markdown inventory + HTML catalogue.

Categories are the top-level folders directly under skills/.  Every SKILL.md
found at any depth beneath a category folder becomes an entry in that category.
Skills sitting at the top level (no parent folder) land in an "Other" bucket.
"""

from __future__ import annotations

import argparse
import html as html_mod
import re
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import NamedTuple

SCRIPT_DIR   = Path(__file__).resolve().parent
SKILL_ROOT   = SCRIPT_DIR.parent
TEMPLATE_DIR = SKILL_ROOT / "templates"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
YAML_FIELD_RE  = re.compile(r"^(\w[\w-]*):\s*(.+)", re.MULTILINE)
YAML_BLOCK_RE  = re.compile(r"^(\w[\w-]*):\s*>-?\s*\n((?:[ \t]+.*\n?)+)", re.MULTILINE)


class SkillEntry(NamedTuple):
    name:     str
    category: str        # top-level folder name, or "" for root-level skills
    rel_path: str        # path from skills_dir to skill folder  e.g. delivery/abd-delivery-planning
    challenge: str
    solution:  str


# ---------------------------------------------------------------------------
# Lightweight frontmatter parser
# ---------------------------------------------------------------------------

def _parse_frontmatter(text: str) -> dict[str, str]:
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}
    block = m.group(1)
    fields: dict[str, str] = {}
    for bm in YAML_BLOCK_RE.finditer(block):
        fields[bm.group(1)] = " ".join(bm.group(2).split())
    for lm in YAML_FIELD_RE.finditer(block):
        key = lm.group(1)
        if key not in fields:
            fields[key] = lm.group(2).strip().strip('"').strip("'")
    return fields


def _extract_section(body: str, heading: str) -> str | None:
    pattern = re.compile(
        rf"^##\s+{re.escape(heading)}\s*\n(.*?)(?=\n##\s|\Z)",
        re.DOTALL | re.MULTILINE,
    )
    m = pattern.search(body)
    return m.group(1).strip() if m else None


def _strip_md(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*",     r"\1", text)
    text = re.sub(r"`[^`]+`",         "",    text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def _truncate(text: str, limit: int = 200) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;: ") + " …"


PREAMBLE_RE = re.compile(
    r"^(load this skill|use when|use this skill|any of the following)\b",
    re.IGNORECASE,
)


def _first_meaningful_line(text: str) -> str:
    text = _strip_md(text)
    for line in text.splitlines():
        line = line.strip().lstrip("- ").strip()
        if len(line) < 15:
            continue
        if PREAMBLE_RE.match(line):
            continue
        sent = re.split(r"(?<=[.!?])\s", line, maxsplit=1)[0]
        return _truncate(sent)
    return _truncate(text.strip())


def _first_bullet(text: str) -> str:
    text = _strip_md(text)
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("- "):
            content = stripped[2:].strip()
            if len(content) > 15:
                return _truncate(content)
    return ""


def _derive_challenge(body: str) -> str:
    purpose = _extract_section(body, "Purpose")
    if purpose:
        result = _first_meaningful_line(purpose)
        if result and not PREAMBLE_RE.match(result):
            return result
    for heading in ("When to use this skill", "When to use", "When to Apply"):
        section = _extract_section(body, heading)
        if section:
            bullet = _first_bullet(section)
            if bullet:
                return bullet
            result = _first_meaningful_line(section)
            if result and not PREAMBLE_RE.match(result):
                return result
    h1_match = re.search(r"^#\s+(.+)", body, re.MULTILINE)
    if h1_match:
        return _truncate(h1_match.group(1).strip())
    return "See SKILL.md for details."


def _derive_solution(fm: dict[str, str], body: str) -> str:
    one = (fm.get("catalogue_one_liner") or "").strip()
    if one and one != "---":
        return _truncate(_strip_md(one), 250)
    desc = fm.get("description", "")
    if desc:
        return _truncate(_strip_md(desc), 250)
    section = _extract_section(body, "Purpose")
    if section:
        return _first_meaningful_line(section)
    return "See SKILL.md for details."


# ---------------------------------------------------------------------------
# Discovery  —  recursive, category = top-level folder
# ---------------------------------------------------------------------------

def discover_skills(skills_dir: Path) -> dict[str, list[SkillEntry]]:
    """Return {category: [SkillEntry, ...]} sorted by category then skill name."""
    by_category: dict[str, list[SkillEntry]] = defaultdict(list)

    for skill_md in sorted(skills_dir.rglob("SKILL.md")):
        skill_folder = skill_md.parent
        rel          = skill_folder.relative_to(skills_dir)
        parts        = rel.parts

        # category = top-level folder; "" for root-level skills
        category = parts[0] if len(parts) > 1 else ""

        text      = skill_md.read_text(encoding="utf-8", errors="replace")
        fm        = _parse_frontmatter(text)
        body      = FRONTMATTER_RE.sub("", text).strip()
        name      = fm.get("name", skill_folder.name)
        challenge = _derive_challenge(body)
        solution  = _derive_solution(fm, body)

        by_category[category].append(
            SkillEntry(
                name=name,
                category=category,
                rel_path=str(rel).replace("\\", "/"),
                challenge=challenge,
                solution=solution,
            )
        )

    # sort entries within each category
    for cat in by_category:
        by_category[cat].sort(key=lambda e: e.name.lower())

    return dict(sorted(by_category.items(), key=lambda kv: kv[0].lower()))


# ---------------------------------------------------------------------------
# Markdown generation
# ---------------------------------------------------------------------------

_CATEGORY_LABELS: dict[str, str] = {
    "":               "General",
    "delivery":       "Delivery",
    "domain-driven-design": "Domain-Driven Design",
    "engineering":    "Engineering",
    "idea shaping":   "Idea Shaping",
    "skill-helpers":  "Skill Helpers",
    "story-analysis": "Story Analysis",
    "utilities":      "Utilities",
}


def _category_label(cat: str) -> str:
    return _CATEGORY_LABELS.get(cat, cat.replace("-", " ").title())


def generate_markdown(by_category: dict[str, list[SkillEntry]]) -> str:
    total = sum(len(v) for v in by_category.values())
    lines = [
        "# Skill Garden — Inventory",
        "",
        f"> Auto-generated catalogue of **{total}** deployed skills.",
        "> Re-run `generate_catalogue.py` to refresh.",
        "",
    ]
    for cat, entries in by_category.items():
        lines += [f"## {_category_label(cat)}", "", "| Skill | Challenge | Solution |", "| --- | --- | --- |"]
        for e in entries:
            link      = f"[{e.name}]({e.rel_path}/)"
            challenge = e.challenge.replace("|", "\\|")
            solution  = e.solution.replace("|", "\\|")
            lines.append(f"| {link} | {challenge} | {solution} |")
        lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# HTML generation
# ---------------------------------------------------------------------------

def _h(text: str) -> str:
    return html_mod.escape(text)


_CARD_ICON = (
    '<svg width="24" height="24" viewBox="0 0 24 24" fill="none">'
    '<rect width="24" height="24" rx="4" fill="#1a1a1e"/>'
    '<path d="M7 8h10M7 12h7M7 16h10" stroke="#ff7a00" stroke-width="1.5" stroke-linecap="round"/>'
    '</svg>'
)


def _render_card(e: SkillEntry) -> str:
    return textwrap.dedent(f"""\
  <a class="cap-card" href="../{_h(e.rel_path)}/">
    <p class="cap-card__title">
      <span class="cap-card__icon">{_CARD_ICON}</span>
      {_h(e.name)}
    </p>
    <div class="cap-card__row">
      <div>
        <p class="cap-card__label">Challenge</p>
        <p class="cap-card__problem">{_h(e.challenge)}</p>
      </div>
      <hr class="cap-card__sep">
      <div>
        <p class="cap-card__label">Solution</p>
        <p class="cap-card__solution">{_h(e.solution)}</p>
      </div>
    </div>
    <p class="cap-card__more">Open skill →</p>
  </a>
""")


def generate_html(by_category: dict[str, list[SkillEntry]]) -> str:
    total    = sum(len(v) for v in by_category.values())
    sections: list[str] = []

    for cat, entries in by_category.items():
        label = _category_label(cat)
        cards = "\n".join(_render_card(e) for e in entries)
        sections.append(
            f'<h2>{_h(label)}</h2>\n<div class="cap-grid">\n{cards}\n</div>'
        )

    skill_sections = "\n\n".join(sections)

    template_path = TEMPLATE_DIR / "catalog-index.html"
    template = (
        template_path.read_text(encoding="utf-8")
        if template_path.exists()
        else _default_html_template()
    )

    return (
        template
        .replace("{{SKILL_COUNT}}", str(total))
        .replace("{{SKILL_SECTIONS}}", skill_sections)
    )


def _default_html_template() -> str:
    return textwrap.dedent("""\
        <!DOCTYPE html><html><head><meta charset="utf-8">
        <title>Skill Catalogue</title></head><body>
        <h1>Skill Catalogue ({{SKILL_COUNT}} skills)</h1>
        {{SKILL_SECTIONS}}
        </body></html>""")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="Generate categorised skill catalogue.")
    parser.add_argument(
        "--skills-dir", type=Path, required=True,
        help="Root skills folder (top-level subfolders become categories).",
    )
    parser.add_argument(
        "--output-dir", type=Path, default=None,
        help="Where to write outputs. Defaults to --skills-dir.",
    )
    args = parser.parse_args()

    skills_dir: Path = args.skills_dir.resolve()
    output_dir: Path = (args.output_dir or skills_dir).resolve()

    if not skills_dir.is_dir():
        raise SystemExit(f"Skills directory not found: {skills_dir}")

    by_category = discover_skills(skills_dir)
    total = sum(len(v) for v in by_category.values())
    if not total:
        raise SystemExit(f"No SKILL.md files found under {skills_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)

    md_path = output_dir / "skill-inventory.md"
    md_path.write_text(generate_markdown(by_category), encoding="utf-8")
    print(f"  wrote {md_path}  ({total} skills across {len(by_category)} categories)")

    html_path = output_dir / "index.html"
    html_path.write_text(generate_html(by_category), encoding="utf-8")
    print(f"  wrote {html_path}")


if __name__ == "__main__":
    main()
