#!/usr/bin/env python3
"""Generate and sync delivery-lead delivery-plan-checklist.md.

The narrative plan (`agile-delivery-plan.md`) defines structure. Slot execution
truth is `slot-NN-finished.md` + `run-log.jsonl`. This script:

  1. **generate** — rebuild checklist structure from the plan (merge prior `- [x]`).
  2. **sync** — tick run/stage lines from `run-log.jsonl` stage_exit_gate / run_complete.

Delivery-lead MUST run sync after every stage exit gate and run complete (see
delivery/agents/delivery-lead/AGENT.md).

Usage (from agilebydesign-skills repo root):

    python skill-helpers/skills/track_task/scripts/generate_delivery_checklist.py
    python skill-helpers/skills/track_task/scripts/generate_delivery_checklist.py --workspace C:\\dev\\my-engagement
    python skill-helpers/skills/track_task/scripts/generate_delivery_checklist.py --sync-only --workspace C:\\dev\\my-engagement
    python skill-helpers/skills/track_task/scripts/generate_delivery_checklist.py --dry-run

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

# skill-helpers/skills/track_task/scripts -> repo root is four levels up
AGENT_ROOT = Path(__file__).resolve().parents[4]
CONFIG = AGENT_ROOT / "skill-config.json"

PLANNING_DIR = Path("docs") / "planning"
DELIVERY_LEAD_DIR = PLANNING_DIR / "abd-delivery-lead"
WAR_ROOM_DIR = PLANNING_DIR / "delivery-war-room"
CHECKLIST_NAME = "delivery-plan-checklist.md"
PLAN_NAME = "agile-delivery-plan.md"
RUN_LOG_NAME = "run-log.jsonl"
SLOT_FINISHED_GLOB = "slot-*-finished.md"


def _resolve_plan_path(workspace: Path) -> Path:
    return workspace / DELIVERY_LEAD_DIR / PLAN_NAME


def _resolve_war_room_path(workspace: Path) -> Path:
    return workspace / WAR_ROOM_DIR


def _resolve_run_log_path(workspace: Path) -> Path:
    return _resolve_war_room_path(workspace) / RUN_LOG_NAME


def _workspace_from_plan(plan_path: Path) -> Path:
    """`.../docs/planning/abd-delivery-lead/agile-delivery-plan.md` → engagement root."""
    if plan_path.parent.name == "abd-delivery-lead" and len(plan_path.parents) >= 4:
        return plan_path.parents[3]
    return plan_path.parent


def _resolve_checklist_path(workspace: Path) -> Path:
    return _resolve_war_room_path(workspace) / CHECKLIST_NAME


CANONICAL_STAGES = [
    "shaping",
    "discovery",
    "exploration",
    "specification",
    "engineering",
]

# Map plan text to canonical stage slugs (bootcamp five stages).
STAGE_ALIASES = {
    "shaping": "shaping",
    "discovery": "discovery",
    "prioritization": "discovery",
    "prioritisation": "discovery",
    "exploration": "exploration",
    "specification": "specification",
    "scenarios": "specification",
    "story definition": "specification",
    "story-definition": "specification",
    "spec by example": "specification",
    "specification by example": "specification",
    "engineering": "engineering",
    "clean code": "engineering",
    "implementation": "engineering",
    "atdd": "engineering",
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
    ("Step 5 — Validate stage exit", "reviewer scanned + reviewed; fixes incorporated; exit gate at CHECKPOINT"),
    ("Step 6 — Handoff to next stage", "artifacts, decisions, corrections passed forward"),
    ("Step 7 — Run complete, revise plan", "run summary + revised plan presented at CHECKPOINT"),
    ("Step 8 — Plan complete", "final summary, open items, strategy save proposal at CHECKPOINT"),
]


def _stage_checklist_lines(stage: str) -> list[str]:
    """Granular per-stage lines: executor slot → reviewer slot → rework → lead gate."""
    return [
        f"- [ ] **{stage}** — entry verified",
        "  - [ ] **Executor** — slot authored and `delivery-team-member` bootstrapped (role + workspace + scope + corrections)",
        "  - [ ] **Executor** — draft stage artifacts produced",
        "  - [ ] **Executor** — self-review against skill rules complete",
        "  - [ ] **Executor CHECKPOINT** — operator confirms drafts",
        "  - [ ] **Executor** — story-graph updated via story-graph-ops (if stage produces graph content)",
        "  - [ ] **Executor** — scanners green (all practice skills)",
        "  - [ ] **Executor** — slot finished (`slot-NN-finished.md` on disk)",
        "  - [ ] **Reviewer** — slot authored (`team-role: reviewer`; scope = executor artifacts only)",
        "  - [ ] **Reviewer** — bootstrapped; read executor `slot-NN-finished.md` + artifact paths",
        "  - [ ] **Reviewer** — scanners run (`execute-skill-using-skills-rules`); pass/fail in reviewer finished file",
        "  - [ ] **Reviewer** — exit-gate review complete; findings in reviewer `slot-MM-finished.md`",
        "  - [ ] **Reviewer CHECKPOINT** — delivery lead reads findings",
        "  - [ ] **Rework** — corrections logged for reviewer findings (or N/A if clean pass)",
        "  - [ ] **Rework** — team member incorporated suggested fixes (rework slot complete)",
        "  - [ ] **Rework** — scanners green after fix incorporation",
        f"  - [ ] **Delivery lead** — exit gate verified against `stages/{stage}.md`",
        "  - [ ] **CHECKPOINT** — user confirms stage complete",
    ]


def render_checklist(runs: list[Run], plan_path: Path, now_iso: str) -> str:
    out: list[str] = []
    out.append("# ABD Delivery Plan — Checklist")
    out.append("")
    out.append(f"<!-- generated-by: skill-helpers/skills/track_task/scripts/generate_delivery_checklist.py -->")
    out.append(f"<!-- generated-at: {now_iso} -->")
    out.append(f"<!-- source-plan: {plan_path} -->")
    out.append("")
    out.append("**Sub-bullets** under a stage are ticked when that **run's** stage exit gate is in `run-log.jsonl`.")
    out.append("**Synced:** stage header + sub-bullets (per run), **Run N CHECKPOINT**, orchestration Steps, **Progress at a glance**.")
    out.append("")
    out.append("**Per-stage tracking:** each stage is executor slot -> **reviewer slot** (scan + gate review as separate checkboxes) -> **rework** (fixes incorporated) -> delivery-lead exit gate. Tick each line; do not skip reviewer or rework steps.")
    out.append("")
    out.append("## Orchestration (delivery-lead AGENT.md)")
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
            out.extend(_stage_checklist_lines(stage))
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


# --------------------------- war-room sync (run-log) ---------------------------- #

_RUN_HEADING_RE = re.compile(r"^### Run (\d+)\b")
_STAGE_HEADING_RE = re.compile(r"^(- \[ \]|- \[x\]) \*\*(\w+)\*\* — entry verified")
_RUN_CKPT_RE = re.compile(r"^(- \[ \]|- \[x\]) \*\*Run (\d+) CHECKPOINT\*\*")
_ORCH_STEP_RE = re.compile(r"^(- \[ \]|- \[x\]) \*\*(Step \d+ — [^*]+)\*\*")
_SLOT_NUM_RE = re.compile(r"slot-(\d+)")
_RESUME_RE = re.compile(r"^<!-- resume:.*-->$")
_GLANCE_HEADING = "## Progress at a glance (from run-log — authoritative)"


def _strip_glance_and_resume(lines: list[str]) -> list[str]:
    out: list[str] = []
    skipping = False
    for line in lines:
        if _RESUME_RE.match(line.strip()):
            continue
        if line.strip() == _GLANCE_HEADING:
            skipping = True
            continue
        if skipping:
            if line.startswith("## ") or line.startswith("**Per-stage"):
                skipping = False
                out.append(line)
            continue
        out.append(line)
    return out


@dataclass
class WarRoomProgress:
    completed_stages: dict[int, set[str]]
    completed_runs: set[int]
    run_slots: dict[int, list[int]]
    has_any_slot: bool
    has_stage_gate: bool
    has_run_complete: bool
    next_slot: int | None


def _normalize_log_stage(raw: str) -> str | None:
    return _normalize_stage(raw) if raw else None


def parse_run_log(run_log_path: Path) -> WarRoomProgress:
    completed_stages: dict[int, set[str]] = {}
    completed_runs: set[int] = set()
    run_slots: dict[int, list[int]] = {}
    has_any_slot = False
    has_stage_gate = False
    has_run_complete = False

    if not run_log_path.is_file():
        return WarRoomProgress(
            completed_stages, completed_runs, run_slots, False, False, False, None
        )

    for line in run_log_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        kind = event.get("event")
        if kind == "slot_complete":
            has_any_slot = True
        elif kind == "stage_exit_gate":
            has_stage_gate = True
            stage = _normalize_log_stage(str(event.get("stage", "")))
            if not stage:
                continue
            run_raw = event.get("run")
            run_num = int(run_raw) if run_raw is not None else (1 if stage == "discovery" else None)
            if run_num is None:
                continue
            completed_stages.setdefault(run_num, set()).add(stage)
        elif kind == "run_complete":
            has_run_complete = True
            run_raw = event.get("run")
            if run_raw is None:
                continue
            run_num = int(run_raw)
            completed_runs.add(run_num)
            slots_raw = event.get("slots_completed") or []
            if isinstance(slots_raw, list) and slots_raw:
                run_slots[run_num] = sorted(int(s) for s in slots_raw)
            for stage_token in event.get("stages") or []:
                stage = _normalize_log_stage(str(stage_token))
                if stage:
                    completed_stages.setdefault(run_num, set()).add(stage)

    return WarRoomProgress(
        completed_stages=completed_stages,
        completed_runs=completed_runs,
        run_slots=run_slots,
        has_any_slot=has_any_slot,
        has_stage_gate=has_stage_gate,
        has_run_complete=has_run_complete,
        next_slot=None,
    )


def _format_slot_span(slots: list[int]) -> str:
    if not slots:
        return "—"
    if len(slots) == 1:
        return str(slots[0])
    if slots == list(range(slots[0], slots[-1] + 1)):
        return f"{slots[0]}–{slots[-1]}"
    return ", ".join(str(s) for s in slots)


def _stage_done(progress: WarRoomProgress, run_num: int | None, stage: str | None) -> bool:
    return (
        run_num is not None
        and stage is not None
        and stage in progress.completed_stages.get(run_num, set())
    )


def _max_finished_slot(war_room: Path) -> int | None:
    highest: int | None = None
    for path in war_room.glob(SLOT_FINISHED_GLOB):
        m = _SLOT_NUM_RE.search(path.name)
        if not m:
            continue
        num = int(m.group(1))
        if highest is None or num > highest:
            highest = num
    return highest


def _tick_unchecked(line: str) -> str:
    m = _UNCHECKED_RE.match(line)
    if m:
        return f"{m.group(1)}x{m.group(2)} {m.group(3)}"
    return line


def sync_checklist_from_war_room(
    checklist_text: str,
    progress: WarRoomProgress,
    *,
    synced_at: str,
    next_slot: int | None,
) -> str:
    """Tick stage headers, sub-bullets (within completed stages only), run checkpoints, orchestration."""
    lines = _strip_glance_and_resume(checklist_text.splitlines())
    current_run: int | None = None
    current_stage: str | None = None
    out: list[str] = []

    for line in lines:
        if _RESUME_RE.match(line.strip()):
            continue

        m_run = _RUN_HEADING_RE.match(line)
        if m_run:
            current_run = int(m_run.group(1))
            current_stage = None
            out.append(line)
            continue

        m_stage = _STAGE_HEADING_RE.match(line)
        if m_stage:
            current_stage = m_stage.group(2)
            if _stage_done(progress, current_run, current_stage):
                out.append(_tick_unchecked(line))
            else:
                out.append(re.sub(r"^(- \[)x(\])", r"\1 \2", line) if "- [x]" in line[:5] else line)
            continue

        m_ckpt = _RUN_CKPT_RE.match(line)
        if m_ckpt:
            run_num = int(m_ckpt.group(2))
            if run_num in progress.completed_runs:
                out.append(_tick_unchecked(line))
            else:
                out.append(re.sub(r"^(- \[)x(\])", r"\1 \2", line) if "- [x]" in line[:5] else line)
            continue

        m_orch = _ORCH_STEP_RE.match(line)
        if m_orch:
            title = m_orch.group(2)
            tick = False
            if title.startswith("Step 1") or title.startswith("Step 2"):
                tick = progress.has_any_slot or progress.has_stage_gate
            elif title.startswith("Step 3") or title.startswith("Step 4"):
                tick = progress.has_any_slot
            elif title.startswith("Step 5") or title.startswith("Step 6"):
                tick = progress.has_stage_gate
            elif title.startswith("Step 7"):
                tick = progress.has_run_complete
            elif title.startswith("Step 8"):
                tick = 10 in progress.completed_runs
            if tick:
                out.append(_tick_unchecked(line))
            else:
                out.append(re.sub(r"^(- \[)x(\])", r"\1 \2", line) if "- [x]" in line[:5] else line)
            continue

        # Sub-bullets: tick only when this run's stage exit gate passed (run-scoped — no cross-run bleed)
        if current_stage is not None and line.startswith("  - ["):
            if _stage_done(progress, current_run, current_stage):
                out.append(_tick_unchecked(line))
            else:
                out.append(re.sub(r"^(\s*-\s*\[)x(\])", r"\1 \2", line))
            continue

        out.append(line)

    status_lines = [
        "",
        _GLANCE_HEADING,
        "",
        f"- **Next slot:** {next_slot if next_slot is not None else '—'}",
        f"- **Runs complete:** {', '.join(str(r) for r in sorted(progress.completed_runs)) or 'none'}",
    ]
    for run_num in sorted(progress.completed_stages):
        stages = ", ".join(sorted(progress.completed_stages[run_num]))
        slots = progress.run_slots.get(run_num)
        slot_note = f"; slots {_format_slot_span(slots)}" if slots else ""
        status_lines.append(f"- **Run {run_num} stages done:** {stages}{slot_note}")
    status_lines.append("")

    resume = f"<!-- resume: slot {next_slot} next; synced-at: {synced_at} -->"

    insert_at = 0
    for i, line in enumerate(out):
        if line.startswith("**Per-stage tracking:**"):
            insert_at = i
            break
    for j, sl in enumerate(status_lines):
        out.insert(insert_at + j, sl)
    out.insert(insert_at, resume)
    out.insert(insert_at, "")

    return "\n".join(out)


def sync_war_room_checklist(workspace: Path, *, dry_run: bool = False) -> tuple[Path, WarRoomProgress, str]:
    war_room = _resolve_war_room_path(workspace)
    out_path = _resolve_checklist_path(workspace)
    run_log = _resolve_run_log_path(workspace)

    if not out_path.is_file():
        raise FileNotFoundError(f"checklist not found: {out_path} — run generate first")

    progress = parse_run_log(run_log)
    max_slot = _max_finished_slot(war_room)
    progress.next_slot = (max_slot + 1) if max_slot is not None else None

    now_iso = datetime.now(timezone.utc).isoformat(timespec="seconds")
    synced = sync_checklist_from_war_room(
        out_path.read_text(encoding="utf-8"),
        progress,
        synced_at=now_iso,
        next_slot=progress.next_slot,
    )

    if not dry_run:
        out_path.write_text(synced + "\n", encoding="utf-8")

    return out_path, progress, synced


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
    ap.add_argument(
        "--sync-only",
        action="store_true",
        help="Sync checkboxes from run-log.jsonl without regenerating structure.",
    )
    ap.add_argument(
        "--no-sync",
        action="store_true",
        help="After generate, skip run-log sync (not recommended for delivery-lead).",
    )
    ns = ap.parse_args(argv)

    if ns.plan:
        plan_path = Path(ns.plan).expanduser().resolve()
        workspace = _workspace_from_plan(plan_path)
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
        plan_path = _resolve_plan_path(workspace)

    if ns.sync_only:
        try:
            out_path, progress, synced = sync_war_room_checklist(workspace, dry_run=ns.dry_run)
        except FileNotFoundError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        if ns.dry_run:
            sys.stdout.write(synced)
            if not synced.endswith("\n"):
                sys.stdout.write("\n")
            return 0
        stages = sum(len(v) for v in progress.completed_stages.values())
        print(
            f"synced {out_path} — {len(progress.completed_runs)} run(s), "
            f"{stages} stage gate(s), next slot {progress.next_slot}"
        )
        return 0

    if not plan_path.is_file():
        print(f"error: plan file not found: {plan_path}", file=sys.stderr)
        return 1

    plan_text = plan_path.read_text(encoding="utf-8")
    runs = parse_plan(plan_text)

    if ns.out:
        out_path = Path(ns.out).expanduser().resolve()
    else:
        out_path = _resolve_checklist_path(workspace)

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

    if not ns.no_sync:
        _, progress, _ = sync_war_room_checklist(workspace)
        stages = sum(len(v) for v in progress.completed_stages.values())
        print(
            f"synced from run-log — {len(progress.completed_runs)} run(s), "
            f"{stages} stage(s), next slot {progress.next_slot}"
        )

    return 0 if runs else 2


if __name__ == "__main__":
    raise SystemExit(main())
