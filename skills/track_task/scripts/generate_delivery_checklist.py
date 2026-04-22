#!/usr/bin/env python3
"""Generate abd-delivery-lead delivery-plan-checklist.md from agile-delivery-plan.md.

Single source of truth is the narrative plan. The checklist is regenerated from it
so the two cannot drift. Intended to be run by abd-delivery-lead after it writes or
revises <workspace>/agile-delivery-plan.md.

Usage (from agent root, parent of skills/):

    python skills/track_task/scripts/generate_delivery_checklist.py
    python skills/track_task/scripts/generate_delivery_checklist.py --workspace C:\\dev\\my-engagement
    python skills/track_task/scripts/generate_delivery_checklist.py --plan path/to/agile-delivery-plan.md --out path/to/checklist.md
    python skills/track_task/scripts/generate_delivery_checklist.py --dry-run

Resolution order for the workspace, when --workspace / --plan is not given:
  1. skill-config.json -> workspace.active_skill_workspace on the agent root
  2. error

Exit codes: 0 on success, 1 on resolution or parse failure, 2 on no runs found.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# skills/track_task/scripts -> agent root is three levels up
AGENT_ROOT = Path(__file__).resolve().parents[3]
CONFIG = AGENT_ROOT / "skill-config.json"

CANONICAL_STAGES = [
    "discovery",
    "prioritization",
    "exploration",
    "scenarios",
    "acceptance-tests",
    "engineering",
]

# Aliases observed in the ABD docs (strategies, stage files). Map everything to canonical.
STAGE_ALIASES = {
    "discovery": "discovery",
    "prioritization": "prioritization",
    "prioritisation": "prioritization",
    "exploration": "exploration",
    "scenarios": "scenarios",
    "story definition": "scenarios",
    "story-definition": "scenarios",
    "specification by example": "scenarios",
    "spec by example": "scenarios",
    "acceptance tests": "acceptance-tests",
    "acceptance-tests": "acceptance-tests",
    "acceptance test": "acceptance-tests",
    "atdd": "acceptance-tests",
    "engineering": "engineering",
    "clean code": "engineering",
    "implementation": "engineering",
}


@dataclass
class Run:
    label: str           # e.g. "1" or "3a"
    stages: list[str]    # canonical stage slugs, ordered
    scope: str = ""
    checkpoint_policy: str = ""
    rationale: str = ""
    raw: dict[str, str] = field(default_factory=dict)


# ----------------------------- workspace / config ----------------------------- #

def _load_workspace_from_config() -> Path | None:
    if not CONFIG.is_file():
        return None
    try:
        data = json.loads(CONFIG.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    ws = data.get("workspace") if isinstance(data.get("workspace"), dict) else {}
    raw = ws.get("active_skill_workspace")
    if not raw or not isinstance(raw, str):
        return None
    p = Path(raw).expanduser()
    if not p.is_absolute():
        p = (AGENT_ROOT / p).resolve()
    return p


# ----------------------------- plan file parsing ------------------------------ #

_TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?(\s*\|\s*:?-{3,}:?)+\s*\|?\s*$")

def _split_row(line: str) -> list[str]:
    """Split a markdown table row into trimmed cells, dropping the leading/trailing empty."""
    # remove optional outer pipes
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def _iter_tables(lines: list[str]) -> Iterable[tuple[list[str], list[list[str]]]]:
    """Yield (headers, rows) for every markdown table in the file."""
    i = 0
    n = len(lines)
    while i < n - 1:
        line = lines[i]
        nxt = lines[i + 1]
        if "|" in line and _TABLE_SEP_RE.match(nxt):
            headers = _split_row(line)
            # collect rows until blank line or non-row
            j = i + 2
            rows: list[list[str]] = []
            while j < n:
                row = lines[j]
                if not row.strip() or "|" not in row:
                    break
                cells = _split_row(row)
                # skip accidental separator rows
                if _TABLE_SEP_RE.match(row):
                    j += 1
                    continue
                # normalize to header width
                if len(cells) < len(headers):
                    cells = cells + [""] * (len(headers) - len(cells))
                elif len(cells) > len(headers):
                    cells = cells[: len(headers)]
                rows.append(cells)
                j += 1
            yield headers, rows
            i = j
        else:
            i += 1


def _header_index(headers: list[str], candidates: Iterable[str]) -> int | None:
    low = [h.strip().lower() for h in headers]
    for cand in candidates:
        cand_l = cand.lower()
        for idx, h in enumerate(low):
            if h == cand_l:
                return idx
    # fuzzy contains
    for cand in candidates:
        cand_l = cand.lower()
        for idx, h in enumerate(low):
            if cand_l in h:
                return idx
    return None


def _normalize_stage(token: str) -> str | None:
    t = token.strip().lower()
    t = t.strip("*_` ")
    if not t:
        return None
    # drop trailing notes like "(optional)"
    t = re.sub(r"\(.*?\)", "", t).strip()
    return STAGE_ALIASES.get(t, STAGE_ALIASES.get(t.replace(" ", "-"), None))


def _parse_stages(cell: str) -> list[str]:
    # split on arrows, commas, slashes, ampersands, " then ", " and "
    tokens = re.split(r"(?:->|→|,|/|&|\bthen\b|\band\b)", cell, flags=re.IGNORECASE)
    result: list[str] = []
    for t in tokens:
        s = _normalize_stage(t)
        if s and s not in result:
            result.append(s)
    return result


def parse_plan(plan_text: str) -> list[Run]:
    """Extract runs from an agile-delivery-plan.md.

    Recognizes either a runs table (columns include Stages, typically Run/Step, Scope,
    Checkpoint Policy, Rationale) or ## Run headings followed by fielded bullets.
    """
    lines = plan_text.splitlines()
    runs: list[Run] = []

    # Primary: tables that look like run tables
    for headers, rows in _iter_tables(lines):
        stages_idx = _header_index(headers, ["Stages", "Stage"])
        if stages_idx is None:
            continue
        run_idx = _header_index(headers, ["Run", "Step", "#"])
        scope_idx = _header_index(headers, ["Scope"])
        ck_idx = _header_index(headers, ["Checkpoint Policy", "Checkpoints", "Checkpoint"])
        why_idx = _header_index(headers, ["Rationale", "Why", "Outcome"])
        for row in rows:
            if not row or all(not c for c in row):
                continue
            stages_cell = row[stages_idx]
            stages = _parse_stages(stages_cell)
            if not stages:
                continue
            label = row[run_idx] if run_idx is not None else str(len(runs) + 1)
            runs.append(
                Run(
                    label=label or str(len(runs) + 1),
                    stages=stages,
                    scope=row[scope_idx] if scope_idx is not None else "",
                    checkpoint_policy=row[ck_idx] if ck_idx is not None else "",
                    rationale=row[why_idx] if why_idx is not None else "",
                    raw={h: c for h, c in zip(headers, row)},
                )
            )

    if runs:
        return runs

    # Fallback: ## Run N ... followed by lines like "- Stages: ..."
    run_heading_re = re.compile(r"^#{2,4}\s*Run\s+([0-9a-z.\-]+)", re.IGNORECASE)
    i = 0
    current: Run | None = None
    while i < len(lines):
        line = lines[i]
        m = run_heading_re.match(line)
        if m:
            if current and current.stages:
                runs.append(current)
            current = Run(label=m.group(1), stages=[])
        elif current is not None:
            s_match = re.match(r"\s*[-*]\s*\*{0,2}(Stages?)\*{0,2}\s*:\s*(.+)", line, re.IGNORECASE)
            sc_match = re.match(r"\s*[-*]\s*\*{0,2}(Scope)\*{0,2}\s*:\s*(.+)", line, re.IGNORECASE)
            ck_match = re.match(r"\s*[-*]\s*\*{0,2}(Checkpoint[s]?(?:\s+Policy)?)\*{0,2}\s*:\s*(.+)", line, re.IGNORECASE)
            ra_match = re.match(r"\s*[-*]\s*\*{0,2}(Rationale|Outcome|Why)\*{0,2}\s*:\s*(.+)", line, re.IGNORECASE)
            if s_match:
                current.stages = _parse_stages(s_match.group(2))
            elif sc_match:
                current.scope = sc_match.group(2).strip()
            elif ck_match:
                current.checkpoint_policy = ck_match.group(2).strip()
            elif ra_match:
                current.rationale = ra_match.group(2).strip()
        i += 1
    if current and current.stages:
        runs.append(current)
    return runs


# ----------------------------- checklist emission ----------------------------- #

ORCHESTRATION_STEPS = [
    ("Step 1 — Establish workspace", "workspace path confirmed and existing artifacts noted"),
    ("Step 2 — Build the plan", "plan presented at CHECKPOINT and `agile-delivery-plan.md` written"),
    ("Step 3 — Open first stage of first run", "entry conditions verified for the current stage"),
    ("Step 4 — Bootstrap team member", "team-role, workspace, scope, corrections handed off"),
    ("Step 5 — Validate stage exit", "exit gate + cross-stage checks pass at CHECKPOINT"),
    ("Step 6 — Handoff to next stage", "artifacts, decisions, corrections passed forward"),
    ("Step 7 — Run complete, revise plan", "run summary + revised plan presented at CHECKPOINT"),
    ("Step 8 — Plan complete", "final summary, open items, strategy save proposal at CHECKPOINT"),
]


def render_checklist(runs: list[Run], plan_path: Path, now_iso: str) -> str:
    out: list[str] = []
    out.append("# ABD Delivery Plan — Checklist")
    out.append("")
    out.append(f"<!-- generated-by: skills/track_task/scripts/generate_delivery_checklist.py -->")
    out.append(f"<!-- generated-at: {now_iso} -->")
    out.append(f"<!-- source-plan: {plan_path} -->")
    out.append("")
    out.append("**Do not edit by hand.** This file is regenerated from `agile-delivery-plan.md`.")
    out.append("To change it, edit the plan and re-run the generator. Tick boxes freely —")
    out.append("re-generation preserves your check state by re-reading the plan only; checked")
    out.append("boxes are written as `- [x]` below once you flip them and save, and the next")
    out.append("generator run will merge them (see `--merge` flag).")
    out.append("")
    out.append("## Orchestration (abd-delivery-lead AGENT.md)")
    out.append("")
    for title, desc in ORCHESTRATION_STEPS:
        out.append(f"- [ ] **{title}** — {desc}")
    out.append("")
    out.append("## Runs")
    out.append("")
    if not runs:
        out.append("_(no runs parsed from plan)_")
        out.append("")
        return "\n".join(out)

    for r in runs:
        header = f"### Run {r.label}"
        if r.rationale:
            header += f" — {r.rationale}"
        out.append(header)
        if r.scope:
            out.append(f"- **Scope:** {r.scope}")
        if r.checkpoint_policy:
            out.append(f"- **Checkpoint policy:** {r.checkpoint_policy}")
        out.append("")
        for stage in r.stages:
            out.append(f"- [ ] **{stage}** — entry verified")
            out.append(f"  - [ ] `abd-team-member` bootstrapped (role + workspace + scope + corrections)")
            out.append(f"  - [ ] stage artifacts produced and scanners green")
            out.append(f"  - [ ] exit gate verified against `stages/{stage}.md`")
            out.append(f"  - [ ] **CHECKPOINT** — user confirms stage complete")
        out.append(f"- [ ] **Run {r.label} CHECKPOINT** — run summary + plan revision presented")
        out.append("")
    return "\n".join(out)


# ------------------------------- merge behavior ------------------------------- #

_CHECKED_RE = re.compile(r"^(\s*-\s*\[)x(\])\s*(.*)$")
_UNCHECKED_RE = re.compile(r"^(\s*-\s*\[)\s(\])\s*(.*)$")


def _existing_checked_labels(path: Path) -> set[str]:
    """Collect the trailing text of every `- [x]` line in an existing checklist."""
    if not path.is_file():
        return set()
    checked: set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        m = _CHECKED_RE.match(line)
        if m:
            label = m.group(3).strip()
            if label:
                checked.add(label)
    return checked


def _reapply_checks(rendered: str, checked_labels: set[str]) -> str:
    if not checked_labels:
        return rendered
    out_lines: list[str] = []
    for line in rendered.splitlines():
        m = _UNCHECKED_RE.match(line)
        if m and m.group(3).strip() in checked_labels:
            out_lines.append(f"{m.group(1)}x{m.group(2)} {m.group(3)}")
        else:
            out_lines.append(line)
    return "\n".join(out_lines)


# ------------------------------------ cli ------------------------------------ #

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--workspace", help="Engagement workspace root (where agile-delivery-plan.md lives).")
    ap.add_argument("--plan", help="Explicit path to the plan file (overrides --workspace lookup).")
    ap.add_argument("--out", help="Explicit path for the checklist file to write.")
    ap.add_argument("--dry-run", action="store_true", help="Print the checklist to stdout; do not write.")
    ap.add_argument(
        "--no-merge",
        action="store_true",
        help="Do not preserve existing checked boxes when overwriting the checklist.",
    )
    ns = ap.parse_args(argv)

    if ns.plan:
        plan_path = Path(ns.plan).expanduser().resolve()
        workspace = plan_path.parent
    else:
        if ns.workspace:
            workspace = Path(ns.workspace).expanduser().resolve()
        else:
            ws = _load_workspace_from_config()
            if ws is None:
                print(
                    "error: no --workspace or --plan given, and "
                    "skill-config.json workspace.active_skill_workspace is unset.",
                    file=sys.stderr,
                )
                return 1
            workspace = ws
        plan_path = workspace / "agile-delivery-plan.md"

    if not plan_path.is_file():
        print(f"error: plan file not found: {plan_path}", file=sys.stderr)
        return 1

    plan_text = plan_path.read_text(encoding="utf-8")
    runs = parse_plan(plan_text)

    if ns.out:
        out_path = Path(ns.out).expanduser().resolve()
    else:
        out_path = workspace / "abd-delivery-lead" / "progress" / "delivery-plan-checklist.md"

    now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
    rendered = render_checklist(runs, plan_path, now_iso)

    if not ns.no_merge and out_path.is_file():
        previously_checked = _existing_checked_labels(out_path)
        rendered = _reapply_checks(rendered, previously_checked)

    if ns.dry_run:
        sys.stdout.write(rendered)
        if not rendered.endswith("\n"):
            sys.stdout.write("\n")
        return 0 if runs else 2

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(rendered + "\n", encoding="utf-8")
    print(f"wrote {out_path} ({len(runs)} run(s) parsed from {plan_path})")
    return 0 if runs else 2


if __name__ == "__main__":
    raise SystemExit(main())
