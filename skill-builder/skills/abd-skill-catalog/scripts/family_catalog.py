"""Family package discovery and catalog sections for the AI Garden."""
from __future__ import annotations

import html as html_mod
import re
from collections import defaultdict
from pathlib import Path
from typing import Any, NamedTuple
from urllib.parse import quote

FAMILY_PACKAGES = (
    "delivery",
    "story-driven-delivery",
    "domain-driven-design",
    "architecture-centric-delivery",
    "engineering",
    "user-experience-design",
    "context-to-memory",
    "idea-shaping",
    "skill-builder",
    "skill-helpers",
    "utilities",
)

FAMILY_CATALOG_ALIASES = {"idea-shaping": "Idea Shaping"}

FAMILY_SLOT_ORDER = (
    "agents",
    "skills",
    "content",
    "instructions",
    "prompts",
    "lib",
    "scripts",
)

FAMILY_SLOT_LABELS: dict[str, str] = {
    "agents": "Agents — orchestrators (AGENT.md / AGENTS.md)",
    "skills": "Skills — practice packages (SKILL.md)",
    "content": "Content — shared prose merged on deploy",
    "instructions": "Instructions — .mdc / .instructions.md → rules",
    "prompts": "Prompts — .prompt.md → slash commands",
    "lib": "Lib — shared Python packages",
    "scripts": "Scripts — package-level automation",
}

_SKIP_NAMES = frozenset({".git", "__pycache__", ".pytest_cache", "node_modules", ".cursor"})


class FamilySlotEntry(NamedTuple):
    name: str
    rel_path: str
    entry_kind: str  # agent | skill | file | dir
    entry_file: str = ""
    summary: str = ""


class FamilyPackageEntry(NamedTuple):
    id: str
    label: str
    rel_path: str
    summary: str
    slots: dict[str, list[FamilySlotEntry]]
    skill_dir_names: tuple[str, ...]
    agent_dir_names: tuple[str, ...]


def family_label(family_id: str) -> str:
    return FAMILY_CATALOG_ALIASES.get(family_id, family_id.replace("-", " ").title())


def _read_readme_blurb(readme: Path, max_len: int = 320) -> str:
    if not readme.is_file():
        return ""
    text = readme.read_text(encoding="utf-8-sig", errors="replace")
    m = re.search(r"^##\s+Overview\s*\n(.*?)(?=\n##\s|\Z)", text, re.DOTALL | re.MULTILINE)
    block = m.group(1).strip() if m else ""
    if not block:
        for line in text.splitlines():
            s = line.strip()
            if s and not s.startswith("#") and s != "---":
                block = s
                break
    block = re.sub(r"\s+", " ", block)
    if len(block) <= max_len:
        return block
    return block[: max_len - 1].rsplit(" ", 1)[0] + " …"


def _scan_slot(repo_root: Path, family_id: str, slot: str) -> list[FamilySlotEntry]:
    slot_dir = repo_root / family_id / slot
    if not slot_dir.is_dir():
        return []
    out: list[FamilySlotEntry] = []

    if slot == "agents":
        for child in sorted(slot_dir.iterdir(), key=lambda p: p.name.lower()):
            if not child.is_dir() or child.name.startswith("."):
                continue
            entry = next(
                (f for f in ("AGENT.md", "AGENTS.md") if (child / f).is_file()),
                "",
            )
            if not entry:
                continue
            out.append(
                FamilySlotEntry(
                    name=child.name,
                    rel_path=child.relative_to(repo_root).as_posix(),
                    entry_kind="agent",
                    entry_file=entry,
                )
            )
        return out

    if slot == "skills":
        for child in sorted(slot_dir.iterdir(), key=lambda p: p.name.lower()):
            if not child.is_dir() or child.name.startswith("."):
                continue
            if not (child / "SKILL.md").is_file():
                continue
            out.append(
                FamilySlotEntry(
                    name=child.name,
                    rel_path=child.relative_to(repo_root).as_posix(),
                    entry_kind="skill",
                    entry_file="SKILL.md",
                )
            )
        return out

    for path in sorted(slot_dir.rglob("*"), key=lambda p: p.as_posix().lower()):
        if not path.is_file():
            continue
        if any(part.startswith(".") or part in _SKIP_NAMES for part in path.parts):
            continue
        rel = path.relative_to(repo_root).as_posix()
        out.append(
            FamilySlotEntry(
                name=path.name,
                rel_path=rel,
                entry_kind="file",
                entry_file=path.name,
            )
        )
    return out


def discover_family_packages(repo_root: Path) -> list[FamilyPackageEntry]:
    """One entry per repo-root family package with full slot inventory."""
    out: list[FamilyPackageEntry] = []
    for family_id in FAMILY_PACKAGES:
        pkg = repo_root / family_id
        if not pkg.is_dir():
            continue
        slots: dict[str, list[FamilySlotEntry]] = {}
        for slot in FAMILY_SLOT_ORDER:
            slots[slot] = _scan_slot(repo_root, family_id, slot)
        readme = pkg / "README.md"
        summary = _read_readme_blurb(readme) if readme.is_file() else ""
        if not summary:
            counts = ", ".join(
                f"{len(slots[s])} {s}" for s in FAMILY_SLOT_ORDER if slots[s]
            )
            summary = counts or "Family capability package."
        out.append(
            FamilyPackageEntry(
                id=family_id,
                label=family_label(family_id),
                rel_path=family_id,
                summary=summary,
                slots=slots,
                skill_dir_names=tuple(x.name for x in slots.get("skills", [])),
                agent_dir_names=tuple(x.name for x in slots.get("agents", [])),
            )
        )
    return out


def family_counts_line(fam: FamilyPackageEntry) -> str:
    parts: list[str] = []
    if fam.agent_dir_names:
        parts.append(f"{len(fam.agent_dir_names)} agent{'s' if len(fam.agent_dir_names) != 1 else ''}")
    if fam.skill_dir_names:
        parts.append(f"{len(fam.skill_dir_names)} skill{'s' if len(fam.skill_dir_names) != 1 else ''}")
    for slot in ("instructions", "prompts", "content", "lib", "scripts"):
        n = len(fam.slots.get(slot, []))
        if n:
            parts.append(f"{n} {slot}")
    return " · ".join(parts) if parts else "package slots"


def outline_families_section(
    families: list[FamilyPackageEntry], md_prefix: str
) -> list[str]:
    lines = [
        "## Family packages",
        "",
        "Repo-root capability families (`<family>/agents|skills|content|instructions|prompts|lib|scripts/`).",
        "",
        "| Family | Summary | Open |",
        "| --- | --- | --- |",
    ]
    for fam in families:
        link = f"{md_prefix}{fam.rel_path}/README.md"
        desc = fam.summary.replace("|", "\\|")
        lines.append(f"| **{fam.label}** (`{fam.id}/`) | {desc} | [README.md]({link}) |")
    lines += ["", "### Family package layout (detail)", ""]
    for fam in families:
        lines += [
            f"#### {fam.label} — `{fam.id}/`",
            "",
            fam.summary,
            "",
        ]
        for slot in FAMILY_SLOT_ORDER:
            items = fam.slots.get(slot, [])
            lines.append(f"**{FAMILY_SLOT_LABELS[slot]}**")
            lines.append("")
            if not items:
                lines.append(f"- _(empty `{fam.id}/{slot}/`)_")
            elif slot in ("agents", "skills"):
                for it in items:
                    entry = it.entry_file or "—"
                    lines.append(
                        f"- **{it.name}** — [{entry}]({md_prefix}{it.rel_path}/{entry})"
                    )
            else:
                for it in items:
                    lines.append(f"- [{it.rel_path}]({md_prefix}{it.rel_path})")
            lines.append("")
        lines.append("---")
        lines.append("")
    return lines


def card_block_families(families: list[FamilyPackageEntry]) -> str:
    parts: list[str] = []
    for fam in families:
        href = f"family/{quote(fam.id, safe='')}.html"
        counts = family_counts_line(fam)
        parts.append(
            f"""        <a class="cap-card" href="{html_mod.escape(href)}">
          <p class="cap-card__title"><span class="cap-card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="4" fill="#1a1a1e"/><path d="M4 6h16v12H4z" stroke="currentColor" stroke-width="1.5"/><path d="M4 10h16" stroke="currentColor" stroke-width="1.5"/></svg></span>{html_mod.escape(fam.label)}</p>
          <p class="cap-card__label">{html_mod.escape(fam.id)}/</p>
          <p class="cap-card__summary">{html_mod.escape(fam.summary)}</p>
          <p class="cap-card__meta">{html_mod.escape(counts)}</p>
          <p class="cap-card__more">Open family page →</p>
        </a>"""
        )
    return "\n".join(parts)


def html_family_slot_sections(
    fam: FamilyPackageEntry,
    *,
    href_to_repo: str,
    skill_href: Any,
    agent_href: Any,
) -> str:
    """HTML blocks listing each standard slot with links."""
    sections: list[str] = []
    for slot in FAMILY_SLOT_ORDER:
        items = fam.slots.get(slot, [])
        sections.append(f'<h3 id="slot-{html_mod.escape(slot)}">{html_mod.escape(FAMILY_SLOT_LABELS[slot])}</h3>')
        if not items:
            sections.append(f'<p class="entry-caption">_(empty <code>{html_mod.escape(fam.id)}/{html_mod.escape(slot)}/</code>)_</p>')
            continue
        rows: list[str] = ['<ul class="file-list file-list--root">']
        for it in items:
            if slot == "skills":
                detail = skill_href(it.name)
                rows.append(
                    f'<li><a href="{html_mod.escape(detail)}">{html_mod.escape(it.name)}</a>'
                    f' — <a href="{html_mod.escape(href_to_repo + it.rel_path + "/SKILL.md")}" target="_blank" rel="noopener noreferrer">SKILL.md</a></li>'
                )
            elif slot == "agents":
                detail = agent_href(it.name)
                ef = it.entry_file or "AGENT.md"
                rows.append(
                    f'<li><a href="{html_mod.escape(detail)}">{html_mod.escape(it.name)}</a>'
                    f' — <a href="{html_mod.escape(href_to_repo + it.rel_path + "/" + ef)}" target="_blank" rel="noopener noreferrer">{html_mod.escape(ef)}</a></li>'
                )
            else:
                rows.append(
                    f'<li><a href="{html_mod.escape(href_to_repo + it.rel_path)}" target="_blank" rel="noopener noreferrer">{html_mod.escape(it.rel_path)}</a></li>'
                )
        rows.append("</ul>")
        sections.append("\n".join(rows))
    return "\n".join(sections)
