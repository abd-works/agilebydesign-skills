#!/usr/bin/env python3
"""Scan repo-root skills/ and agents/; emit Markdown outline + HTML mini-site."""

from __future__ import annotations

import argparse
import html as html_mod
import re
import textwrap
from pathlib import Path
from typing import NamedTuple

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
TEMPLATE_DIR = SKILL_DIR / "templates"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.DOTALL)
YAML_FIELD_RE = re.compile(r"^(\w[\w-]*):\s*(.+)", re.MULTILINE)
YAML_BLOCK_RE = re.compile(
    r"^(\w[\w-]*):\s*>-?\s*\n((?:[ \t]+.*\n?)+)", re.MULTILINE
)

PREAMBLE_RE = re.compile(
    r"^(load this skill|use when|use this skill|any of the following)\b",
    re.IGNORECASE,
)

KNOWN_DIR_SUMMARY: dict[str, str] = {
    "rules": "Practice rules (DO/DON'T) and constraints used with scanners.",
    "templates": "Authoring templates and structural skeletons.",
    "scripts": "Build, catalogue, validation, or packaging automation.",
    "docs": "Human-oriented documentation for the package.",
    "content": "Source parts merged into agent instructions or outputs.",
    "roles": "Persona playbooks for multi-role agents.",
    "test": "Automated tests for the agent or skill package.",
    "skills": "Nested skills shipped inside an agent package.",
    "context": "Optional engagement or corpus context.",
    "images": "Figures referenced by nearby HTML or markdown docs.",
}


class SkillEntry(NamedTuple):
    name: str
    dir_name: str
    challenge: str
    solution: str
    description: str
    rel_skill_md: str


class AgentEntry(NamedTuple):
    name: str
    dir_name: str
    entry_file: str
    challenge: str
    solution: str
    description: str
    rel_entry_md: str


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
    if not m:
        return None
    return m.group(1).strip()


def _strip_md(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    return text


def _truncate(text: str, limit: int = 200) -> str:
    text = text.strip()
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut.rstrip(".,;: ") + " …"


def _first_meaningful_line(text: str) -> str:
    text = _strip_md(text)
    for line in text.splitlines():
        line = line.strip().lstrip("- ").strip()
        if len(line) < 15:
            continue
        if line.startswith("#"):
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
            content = re.sub(r"^[—\-–]\s*", "", content)
            if len(content) > 15:
                return _truncate(content)
    return ""


def _derive_challenge_skill(body: str) -> str:
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


def _derive_solution_skill(fm: dict[str, str], body: str) -> str:
    desc = fm.get("description", "")
    if desc:
        clean = _strip_md(desc)
        return _truncate(clean, 280)
    section = _extract_section(body, "Purpose")
    if section:
        return _first_meaningful_line(section)
    return "See SKILL.md for details."


def _description_skill(fm: dict[str, str], body: str) -> str:
    purpose = _extract_section(body, "Purpose")
    if purpose:
        return _truncate(_strip_md(purpose), 900)
    desc = fm.get("description", "")
    if desc:
        return _truncate(_strip_md(desc), 900)
    return _truncate(_strip_md(body), 500)


def _h1_title(body: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return m.group(1).strip() if m else None


def _non_hr_lines(text: str) -> list[str]:
    lines: list[str] = []
    for ln in text.splitlines():
        s = ln.strip()
        if not s or s == "---":
            continue
        lines.append(s)
    return lines


def _agent_display_name(fm: dict[str, str], body: str, dir_name: str) -> str:
    n = fm.get("name", "").strip()
    if n:
        return n
    h1 = _h1_title(body)
    if h1:
        h1 = re.sub(r"^AGENTS\s+—\s*", "", h1, flags=re.IGNORECASE).strip()
        return h1 or dir_name
    return dir_name


def _opening_blurb_after_h1(body: str, max_len: int = 260) -> str:
    lines = body.splitlines()
    i = 0
    if i < len(lines) and lines[i].lstrip().startswith("#"):
        i += 1
    parts: list[str] = []
    while i < len(lines):
        if lines[i].startswith("##"):
            break
        s = lines[i].strip()
        if s == "---":
            i += 1
            continue
        if not s:
            if parts:
                break
            i += 1
            continue
        parts.append(s)
        i += 1
    joined = _strip_md(" ".join(parts))
    return _truncate(joined, max_len) if joined else ""


def _derive_challenge_agent(body: str) -> str:
    purpose = _extract_section(body, "Purpose")
    if purpose:
        s = _first_meaningful_line(purpose)
        if s:
            return s
    intro = _extract_section(body, "Introduction")
    if intro:
        s = _first_meaningful_line(intro)
        if s:
            return s
    blurb = _opening_blurb_after_h1(body)
    if blurb:
        return blurb
    t = _h1_title(body)
    if t:
        return _truncate(t)
    return "See agent entry file for details."


def _derive_solution_agent(fm: dict[str, str], body: str) -> str:
    desc = fm.get("description", "").strip()
    if desc and desc != "---":
        return _truncate(_strip_md(desc), 280)
    purpose = _extract_section(body, "Purpose")
    if purpose:
        lines = _non_hr_lines(purpose)
        if len(lines) >= 2:
            return _truncate(_strip_md(lines[1]), 280)
        if lines:
            joined = _strip_md(" ".join(lines))
            return _truncate(joined, 280)
        return _truncate(_strip_md(purpose), 280)
    for heading in (
        "Your skills",
        "Team member skills",
        "Orchestration workflow",
        "Default workflow",
        "Role playbooks",
    ):
        sec = _extract_section(body, heading)
        if sec:
            bullet = _first_bullet(sec)
            if bullet:
                return _truncate(bullet, 280)
    blurb = _opening_blurb_after_h1(body, max_len=400)
    if blurb:
        return _truncate(blurb, 280)
    return _truncate(_first_meaningful_line(body), 280)


def _description_agent(fm: dict[str, str], body: str) -> str:
    purpose = _extract_section(body, "Purpose")
    if purpose:
        return _truncate(_strip_md(purpose), 1200)
    desc = fm.get("description", "")
    if desc:
        return _truncate(_strip_md(desc), 1200)
    return _truncate(_strip_md(body), 800)


def discover_skills(skills_dir: Path, repo_root: Path) -> list[SkillEntry]:
    out: list[SkillEntry] = []
    for child in sorted(skills_dir.iterdir()):
        if not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        if not skill_md.exists():
            continue
        text = skill_md.read_text(encoding="utf-8", errors="replace")
        fm = _parse_frontmatter(text)
        body = FRONTMATTER_RE.sub("", text).strip()
        name = fm.get("name", child.name)
        rel = skill_md.relative_to(repo_root).as_posix()
        out.append(
            SkillEntry(
                name=name,
                dir_name=child.name,
                challenge=_derive_challenge_skill(body),
                solution=_derive_solution_skill(fm, body),
                description=_description_skill(fm, body),
                rel_skill_md=rel,
            )
        )
    return out


def discover_agents(agents_dir: Path, repo_root: Path) -> list[AgentEntry]:
    out: list[AgentEntry] = []
    for child in sorted(agents_dir.iterdir()):
        if not child.is_dir():
            continue
        entry_name: str | None = None
        for fname in ("AGENT.md", "AGENTS.md", "SKILL.md"):
            p = child / fname
            if p.exists():
                entry_name = fname
                text = p.read_text(encoding="utf-8", errors="replace")
                break
        if not entry_name:
            continue
        fm = _parse_frontmatter(text)
        body = FRONTMATTER_RE.sub("", text).strip()
        name = _agent_display_name(fm, body, child.name)
        rel = (child / entry_name).relative_to(repo_root).as_posix()
        out.append(
            AgentEntry(
                name=name,
                dir_name=child.name,
                entry_file=entry_name,
                challenge=_derive_challenge_agent(body),
                solution=_derive_solution_agent(fm, body),
                description=_description_agent(fm, body),
                rel_entry_md=rel,
            )
        )
    return out


def _file_blurb(path: Path, max_len: int = 180) -> str:
    try:
        raw = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "Unreadable file."
    for line in raw.splitlines():
        s = line.strip()
        if not s or s == "---":
            continue
        s = re.sub(r"^#+\s*", "", s)
        s = _strip_md(s)
        if len(s) < 8:
            continue
        return _truncate(s, max_len)
    return "No preview available."


def layout_lines(repo_root: Path, package_dir: Path, md_prefix: str) -> list[str]:
    """Markdown bullets: files with blurb+link; directories one summary line."""
    lines: list[str] = []
    if not package_dir.is_dir():
        return lines
    try:
        kids = sorted(package_dir.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except OSError:
        return ["- (could not read directory)"]
    for p in kids:
        rel = p.relative_to(repo_root).as_posix()
        link = f"{md_prefix}{rel}"
        if p.is_dir():
            summary = KNOWN_DIR_SUMMARY.get(
                p.name,
                f"Supporting folder ({len(list(p.iterdir()))} items).",
            )
            lines.append(f"- **[{p.name}/]({link})** — {summary}")
        else:
            blurb = _file_blurb(p)
            lines.append(f"- [{p.name}]({link}) — {blurb}")
    return lines


def generate_outline_md(
    repo_root: Path,
    skills: list[SkillEntry],
    agents: list[AgentEntry],
    md_link_prefix: str,
) -> str:
    lines: list[str] = [
        "# ABD Skills & Agents — Catalogue Outline",
        "",
        "> Auto-generated from repository `skills/` and `agents/`.",
        "> Run `python skills/abd-skill-catalog/scripts/generate_abd_catalog.py` to refresh.",
        "",
        "This outline mirrors the reader-facing style of `process-outline.md`:",
        "each row states the **challenge**, the **solution**, and where to open the source.",
        "",
        "## Summary — Practice skills",
        "",
        "| Skill | Challenge | Solution | Open |",
        "| --- | --- | --- | --- |",
    ]
    for s in skills:
        link = f"{md_link_prefix}{s.rel_skill_md}"
        ch = s.challenge.replace("|", "\\|")
        sol = s.solution.replace("|", "\\|")
        lines.append(f"| **{s.name}** | {ch} | {sol} | [SKILL.md]({link}) |")
    lines += [
        "",
        "## Summary — Agents",
        "",
        "| Agent | Challenge | Solution | Open |",
        "| --- | --- | --- | --- |",
    ]
    for a in agents:
        link = f"{md_link_prefix}{a.rel_entry_md}"
        ch = a.challenge.replace("|", "\\|")
        sol = a.solution.replace("|", "\\|")
        lines.append(f"| **{a.name}** | {ch} | {sol} | [{a.entry_file}]({link}) |")

    lines += ["", "---", "", "## Skills (detail)", ""]
    skills_root = repo_root / "skills"
    for s in skills:
        d = skills_root / s.dir_name
        lines += [
            f"### {s.name}",
            "",
            f"- **Directory:** [`skills/{s.dir_name}/`]({md_link_prefix}skills/{s.dir_name}/)",
            "",
            "**Challenge:**",
            "",
            s.challenge,
            "",
            "**Solution:**",
            "",
            s.solution,
            "",
            "**Description (from Purpose / body):**",
            "",
            s.description,
            "",
            "**Repository layout:**",
            "",
            *layout_lines(repo_root, d, md_link_prefix),
            "",
        ]

    lines += ["---", "", "## Agents (detail)", ""]
    agents_root = repo_root / "agents"
    for a in agents:
        d = agents_root / a.dir_name
        lines += [
            f"### {a.name}",
            "",
            f"- **Directory:** [`agents/{a.dir_name}/`]({md_link_prefix}agents/{a.dir_name}/)",
            f"- **Entry:** [`{a.rel_entry_md}`]({md_link_prefix}{a.rel_entry_md})",
            "",
            "**Challenge:**",
            "",
            a.challenge,
            "",
            "**Solution:**",
            "",
            a.solution,
            "",
            "**Description:**",
            "",
            a.description,
            "",
            "**Repository layout:**",
            "",
            *layout_lines(repo_root, d, md_link_prefix),
            "",
        ]
    return "\n".join(lines)


def _h(text: str) -> str:
    return html_mod.escape(text)


def _card_block_skills(entries: list[SkillEntry], up_to_repo: str) -> str:
    parts: list[str] = []
    for e in entries:
        href = f"{up_to_repo}skills/{_h(e.dir_name)}/"
        parts.append(
            textwrap.dedent(
                f"""\
        <a class="cap-card" href="{href}">
          <p class="cap-card__title"><span class="cap-card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="4" fill="#1a1a1e"/><path d="M7 8h10M7 12h7M7 16h10" stroke="#ff7a00" stroke-width="1.5" stroke-linecap="round"/></svg></span>{_h(e.name)}</p>
          <p class="cap-card__label">Challenge</p>
          <p class="cap-card__problem">{_h(e.challenge)}</p>
          <hr class="cap-card__sep">
          <p class="cap-card__label">Solution</p>
          <p class="cap-card__solution">{_h(e.solution)}</p>
          <p class="cap-card__label" style="margin-top:10px">Description</p>
          <p class="cap-card__solution">{_h(e.description)}</p>
          <p class="cap-card__more">Open skill folder →</p>
        </a>"""
            )
        )
    return "\n".join(parts)


def _card_block_agents(entries: list[AgentEntry], up_to_repo: str) -> str:
    parts: list[str] = []
    for e in entries:
        href = f"{up_to_repo}agents/{_h(e.dir_name)}/"
        parts.append(
            textwrap.dedent(
                f"""\
        <a class="cap-card" href="{href}">
          <p class="cap-card__title"><span class="cap-card__icon"><svg width="24" height="24" viewBox="0 0 24 24" fill="none"><rect width="24" height="24" rx="4" fill="#1a1a1e"/><path d="M6 9h12v10H6z" stroke="#ff7a00" stroke-width="1.5"/><path d="M9 7V5h6v2" stroke="#ff7a00" stroke-width="1.5" stroke-linecap="round"/></svg></span>{_h(e.name)}</p>
          <p class="cap-card__label">Challenge</p>
          <p class="cap-card__problem">{_h(e.challenge)}</p>
          <hr class="cap-card__sep">
          <p class="cap-card__label">Solution</p>
          <p class="cap-card__solution">{_h(e.solution)}</p>
          <p class="cap-card__label" style="margin-top:10px">Description</p>
          <p class="cap-card__solution">{_h(e.description)}</p>
          <p class="cap-card__more">Open agent folder →</p>
        </a>"""
            )
        )
    return "\n".join(parts)


def _load_template(name: str) -> str:
    p = TEMPLATE_DIR / name
    if not p.exists():
        raise FileNotFoundError(f"Missing template: {p}")
    return p.read_text(encoding="utf-8")


def write_html_pages(
    output_catalog_dir: Path,
    skills: list[SkillEntry],
    agents: list[AgentEntry],
) -> None:
    """Write index.html, skills.html, agents.html under output_catalog_dir."""
    # From .../docs/abd-skill-catalog/catalog/foo.html → repo root is ../../../../../
    up_to_repo = "../../../../../"
    idx_tpl = _load_template("page-catalog.html")
    css = _load_template("catalog.css")

    def fill(
        tpl: str,
        *,
        title: str,
        brand: str,
        h1: str,
        tagline: str,
        intro: str,
        nav_current: str,
        body_inner: str,
    ) -> str:
        def nav_cls(which: str) -> str:
            return "nav__link nav__link--current" if nav_current == which else "nav__link"

        return (
            tpl.replace("{{CSS}}", css)
            .replace("{{TITLE}}", title)
            .replace("{{BRAND}}", brand)
            .replace("{{H1}}", h1)
            .replace("{{TAGLINE}}", tagline)
            .replace("{{INTRO}}", intro)
            .replace("{{NAV_HUB}}", nav_cls("hub"))
            .replace("{{NAV_SKILLS}}", nav_cls("skills"))
            .replace("{{NAV_AGENTS}}", nav_cls("agents"))
            .replace("{{BODY_INNER}}", body_inner)
        )

    brand = "<strong>Agile by Design</strong> &middot; abd-skill-catalog"

    outline_href = f"{up_to_repo}agents/abd-skill-builder/docs/abd-skill-catalog/outline.md"
    hub_intro = (
        "<p>Browse practice <a href=\"skills.html\">skills</a> and "
        "<a href=\"agents.html\">agents</a> in this repository. "
        "For a single diffable document, open "
        f"<a href=\"{outline_href}\">outline.md</a>.</p>"
    )
    hub_body = (
        "<h2>Quick links</h2><ul>"
        '<li><a href="skills.html">All skills — card grid</a></li>'
        '<li><a href="agents.html">All agents — card grid</a></li>'
        "</ul>"
        f"<p>{len(skills)} skills, {len(agents)} agents indexed.</p>"
    )
    index_html = fill(
        idx_tpl,
        title="ABD catalogue — Hub",
        brand=brand,
        h1="Skills &amp; agents catalogue",
        tagline="Repository-wide index aligned with abd-skill-builder docs.",
        intro=hub_intro,
        nav_current="hub",
        body_inner=hub_body,
    )
    (output_catalog_dir / "index.html").write_text(index_html, encoding="utf-8")

    skills_intro = (
        "<p>Each card links to the skill folder under "
        f"<code>{_h('skills/')}</code>. Challenge, solution, and description are derived from "
        "<code>SKILL.md</code>.</p>"
    )
    skills_body = f'<h2>Skills ({len(skills)})</h2><div class="cap-grid">{_card_block_skills(skills, up_to_repo)}</div>'
    (output_catalog_dir / "skills.html").write_text(
        fill(
            idx_tpl,
            title="ABD catalogue — Skills",
            brand=brand,
            h1="Practice skills",
            tagline=f"{len(skills)} entries.",
            intro=skills_intro,
            nav_current="skills",
            body_inner=skills_body,
        ),
        encoding="utf-8",
    )

    agents_intro = (
        "<p>Each card links to the agent folder under "
        f"<code>{_h('agents/')}</code>. The generator prefers <code>AGENT.md</code>, then "
        "<code>AGENTS.md</code>, then <code>SKILL.md</code>.</p>"
    )
    agents_body = f'<h2>Agents ({len(agents)})</h2><div class="cap-grid">{_card_block_agents(agents, up_to_repo)}</div>'
    (output_catalog_dir / "agents.html").write_text(
        fill(
            idx_tpl,
            title="ABD catalogue — Agents",
            brand=brand,
            h1="Agents",
            tagline=f"{len(agents)} entries.",
            intro=agents_intro,
            nav_current="agents",
            body_inner=agents_body,
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate ABD skill + agent catalogue.")
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Repository root (contains skills/ and agents/). "
        "Defaults to ../../../.. from this script (agilebydesign-skills root).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory for outline.md and catalog/. "
        "Default: agents/abd-skill-builder/docs/abd-skill-catalog under repo root.",
    )
    args = parser.parse_args()

    repo_root = (args.repo_root or SKILL_DIR.parent.parent).resolve()
    skills_dir = repo_root / "skills"
    agents_dir = repo_root / "agents"
    output_dir = (
        args.output_dir
        or (repo_root / "agents" / "abd-skill-builder" / "docs" / "abd-skill-catalog")
    ).resolve()

    if not skills_dir.is_dir():
        raise SystemExit(f"skills/ not found: {skills_dir}")
    if not agents_dir.is_dir():
        raise SystemExit(f"agents/ not found: {agents_dir}")

    skills = discover_skills(skills_dir, repo_root)
    agents = discover_agents(agents_dir, repo_root)
    if not skills and not agents:
        raise SystemExit("No skills or agents discovered.")

    output_dir.mkdir(parents=True, exist_ok=True)
    catalog_dir = output_dir / "catalog"
    catalog_dir.mkdir(parents=True, exist_ok=True)

    # outline.md lives in output_dir; links are relative to that file
    outline_path = output_dir / "outline.md"
    md_prefix = "../../../"
    outline_path.write_text(
        generate_outline_md(repo_root, skills, agents, md_prefix),
        encoding="utf-8",
    )
    print(f"  wrote {outline_path}")

    write_html_pages(catalog_dir, skills, agents)
    print(f"  wrote {catalog_dir / 'index.html'}")
    print(f"  wrote {catalog_dir / 'skills.html'}")
    print(f"  wrote {catalog_dir / 'agents.html'}")
    print(f"  ({len(skills)} skills, {len(agents)} agents)")


if __name__ == "__main__":
    main()
