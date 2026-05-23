#!/usr/bin/env python3
"""CLI Delivery Harness — main loop.

Reads the war room, launches agents, monitors heartbeats,
recovers from stalls, and notifies operators.

Usage:
    python -m cli_harness.harness run   <workspace>  [--config <path>]
    python -m cli_harness.harness status <workspace>
"""

from __future__ import annotations

import argparse
import os
import sys
import time
from pathlib import Path
from typing import Any

from . import run_log, notify
from .config import load_config, load_engagement_config, merge_engagement_overrides, save_engagement_config
from .manifest import read_manifest, get_sizing_policy, get_checkpoint_policy
from .slot_state import (
    SlotState,
    find_active_slot,
    get_slot_state,
    is_heartbeat_stale,
    write_running_file,
    update_heartbeat,
)
from .agent_launcher import assemble_bootstrap_prompt, launch_agent, cancel_agent, resume_agent

POLL_INTERVAL_SECONDS = 30
MAX_RETRIES_PER_SLOT = 1


def resolve_war_room(workspace: Path) -> Path:
    return workspace / "delivery-war-room"


def cmd_status(workspace: Path) -> None:
    war_room = resolve_war_room(workspace)
    if not war_room.exists():
        print("No war room found. Engagement not initialized.")
        return

    try:
        manifest = read_manifest(war_room)
    except FileNotFoundError:
        print("War room exists but manifest.md is missing.")
        return

    goal = manifest.get("goal", "<no goal>")
    profile = manifest.get("profile", "?")
    autonomy = manifest.get("autonomy", "?")
    policy = get_sizing_policy(manifest)

    active = find_active_slot(war_room)
    active_str = f"slot-{active.slot_id} ({active.state.value})" if active else "none"

    checklist = workspace / "abd-delivery-lead" / "progress" / "delivery-plan-checklist.md"
    checklist_progress = _checklist_summary(checklist)

    last = run_log.last_entry(war_room)
    last_str = f"{last['event']} at {last['timestamp']}" if last else "no entries"

    print(f"Goal: {goal}")
    print(f"Profile: {profile} | Autonomy: {autonomy}")
    print(f"Active slot: {active_str}")
    print(f"Checklist: {checklist_progress}")
    print(f"Last log: {last_str}")
    print(f"Sizing: {policy.get('stories_per_slot', '?')} stories/slot, "
          f"{policy.get('stages_per_run', '?')} stages/run, "
          f"stall timeout {policy.get('stall_timeout_minutes', '?')}m")


def _checklist_summary(checklist_path: Path) -> str:
    if not checklist_path.exists():
        return "not found"
    text = checklist_path.read_text(encoding="utf-8")
    done = text.count("- [x]") + text.count("- [X]")
    total = done + text.count("- [ ]")
    if total == 0:
        return "empty"
    return f"{done}/{total} done"


def cmd_run(workspace: Path, config: dict[str, Any]) -> None:
    if not config.get("api_key"):
        print("Error: No API key. Set CURSOR_API_KEY or configure cli_harness/cli-config.json", file=sys.stderr)
        sys.exit(1)

    if config.get("agent_mode") == "cloud" and not config.get("repo_url"):
        print("Error: agent_mode is 'cloud' but repo_url is not set in config.", file=sys.stderr)
        sys.exit(1)

    if not workspace.exists():
        print(f"Error: Workspace path does not exist: {workspace}", file=sys.stderr)
        sys.exit(1)
    if not os.access(workspace, os.W_OK):
        print(f"Error: Workspace path is not writable: {workspace}", file=sys.stderr)
        sys.exit(1)

    war_room = resolve_war_room(workspace)
    if not war_room.exists():
        print(f"[Harness] New engagement — prompting for required parameters.")
        params = _prompt_engagement_params(workspace)
        config = merge_engagement_overrides(config, params)

        workspace.mkdir(parents=True, exist_ok=True)
        war_room.mkdir(parents=True, exist_ok=True)

        context_line = f"context: {params['context']}" if params.get("context") else ""
        _launch_delivery_lead(
            workspace, config,
            f"workspace: {workspace}\n"
            f"profile: {params.get('profile', 'bespoke')}\n"
            f"autonomy: {params.get('autonomy', 'tight')}\n"
            f"{context_line}\n\n"
            f"Initialize engagement: build plan (Step 2) and set up war room (Step 2b).",
        )
        print(f"[Harness] Waiting for delivery lead to create manifest...")
        _wait_for_war_room(war_room)

    engagement_config = load_engagement_config(war_room)
    if engagement_config:
        config = merge_engagement_overrides(config, engagement_config)
    else:
        save_engagement_config(war_room, config)

    print(f"[Harness] Starting loop for {workspace}")
    print(f"[Harness] War room: {war_room}")

    retry_counts: dict[str, int] = {}
    active_processes: dict[str, Any] = {}
    notified_finished: set[str] = set()

    try:
        _main_loop(workspace, war_room, config, retry_counts, active_processes, notified_finished)
    except KeyboardInterrupt:
        print("\n[Harness] Interrupted by operator. Exiting.")
        for proc in active_processes.values():
            cancel_agent(proc)


def _launch_delivery_lead(workspace: Path, config: dict[str, Any], context: str) -> dict[str, Any]:
    agent_md = workspace / "agents" / "abd-delivery-lead" / "AGENT.md"
    prompt_parts = [context]
    prompt_parts.append(f"workspace: {workspace}")
    if agent_md.exists():
        prompt_parts.append(agent_md.read_text(encoding="utf-8"))
    prompt = "\n\n---\n\n".join(prompt_parts)
    return launch_agent(prompt, workspace, config, agent_type="delivery-lead")


def _wait_for_war_room(war_room: Path, timeout_seconds: int = 600) -> None:
    elapsed = 0
    while elapsed < timeout_seconds:
        if war_room.exists() and (war_room / "manifest.md").exists():
            return
        time.sleep(10)
        elapsed += 10
    print(f"[Harness] Timed out waiting for war room at {war_room}", file=sys.stderr)
    sys.exit(1)


def _main_loop(
    workspace: Path,
    war_room: Path,
    config: dict[str, Any],
    retry_counts: dict[str, int],
    active_processes: dict[str, Any],
    notified_finished: set[str],
) -> None:
    notification_channel = config.get("notification_channel")

    while True:
        try:
            manifest = read_manifest(war_room)
        except FileNotFoundError:
            print("[Harness] Waiting for manifest.md...")
            time.sleep(POLL_INTERVAL_SECONDS)
            continue

        policy = get_sizing_policy(manifest)
        stall_timeout = policy.get("stall_timeout_minutes", config.get("stall_timeout_minutes", 15))
        detail_level = policy.get("notification_detail", "normal")

        active = find_active_slot(war_room)
        if active is None:
            print("[Harness] No pending work. Idling.")
            time.sleep(POLL_INTERVAL_SECONDS)
            continue

        sid = active.slot_id

        if active.state == SlotState.FINISHED:
            if sid not in notified_finished:
                _handle_finished(war_room, sid, notification_channel, detail_level, workspace, config)
                notified_finished.add(sid)
            else:
                pass  # waiting for delivery lead to chain next slot

        elif active.state == SlotState.BLOCKED:
            _handle_blocked(war_room, sid, notification_channel, active_processes)

        elif active.state == SlotState.RUNNING:
            _handle_running(
                war_room, sid, stall_timeout, notification_channel,
                detail_level, retry_counts, active_processes, workspace, config,
            )

        elif active.state == SlotState.PENDING:
            _handle_pending(war_room, sid, workspace, config, active_processes)

        time.sleep(POLL_INTERVAL_SECONDS)


def _handle_finished(
    war_room: Path, slot_id: str, channel: str | None, detail: str,
    workspace: Path, config: dict[str, Any],
) -> None:
    finished_path = war_room / f"slot-{slot_id}-finished.md"
    summary = _extract_summary(finished_path)

    notify.send(channel, "SLOT_FINISHED", detail_level=detail,
                slot_id=slot_id, summary=summary)
    run_log.append(war_room, "FINISHED", slot_id=slot_id, summary=summary)

    print(f"[Harness] Slot {slot_id} finished. Launching delivery lead for gate validation.")
    _launch_delivery_lead(
        workspace, config,
        f"Slot {slot_id} finished. Read delivery-war-room/slot-{slot_id}-finished.md "
        f"and validate exit gates per Step 5. Then chain to next slot per Step 6.",
    )


def _handle_blocked(
    war_room: Path, slot_id: str, channel: str | None, active_processes: dict,
) -> None:
    answer_path = war_room / f"slot-{slot_id}-answer.md"
    if answer_path.exists():
        print(f"[Harness] Slot {slot_id} has answer — resuming agent.")
        run_log.append(war_room, "RESUMED", slot_id=slot_id)
        return

    blocked_path = war_room / f"slot-{slot_id}-blocked.md"
    question = _extract_question(blocked_path)
    notify.send(channel, "SLOT_BLOCKED", detail_level="high",
                slot_id=slot_id, question=question)
    print(f"[Harness] Slot {slot_id} blocked. Waiting for answer file.")


def _handle_running(
    war_room: Path, slot_id: str, stall_timeout: int,
    channel: str | None, detail: str,
    retry_counts: dict[str, int], active_processes: dict,
    workspace: Path, config: dict,
) -> None:
    info = get_slot_state(war_room, slot_id)
    if not info.running_data:
        return

    if is_heartbeat_stale(info.running_data, stall_timeout):
        agent_id = info.running_data.get("agent_id", "unknown")
        agent_mode = info.running_data.get("mode", "local")

        if agent_mode == "cloud" and agent_id.startswith("bc-"):
            print(f"[Harness] Cloud agent {agent_id} heartbeat stale — attempting SDK resume.")
            resume_result = resume_agent(agent_id, config)
            if not resume_result.get("error"):
                run_log.append(war_room, "RESUMED_CLOUD", slot_id=slot_id, agent_id=agent_id)
                update_heartbeat(war_room, slot_id)
                return
            print(f"[Harness] Cloud resume failed: {resume_result['error']}. Falling through to stall recovery.")

        retries = retry_counts.get(slot_id, 0)
        prior_agent_ids = retry_counts.get(f"{slot_id}_agents", [])
        prior_agent_ids.append(agent_id)
        retry_counts[f"{slot_id}_agents"] = prior_agent_ids

        if retries < MAX_RETRIES_PER_SLOT:
            print(f"[Harness] Slot {slot_id} stalled (agent {agent_id}). Retrying.")
            cancel_agent(active_processes.get(slot_id))
            run_log.append(war_room, "STALLED", slot_id=slot_id, agent_id=agent_id)
            retry_counts[slot_id] = retries + 1
            _handle_pending(war_room, slot_id, workspace, config, active_processes)
        else:
            print(f"[Harness] Slot {slot_id} FAILED after retry.")
            cancel_agent(active_processes.get(slot_id))
            all_agent_ids = prior_agent_ids
            run_log.append(war_room, "FAILED", slot_id=slot_id,
                           agent_ids=all_agent_ids,
                           reason="repeated stall after retry")
            notify.send(channel, "SLOT_FAILED", detail_level="high",
                        slot_id=slot_id,
                        agent_ids=", ".join(all_agent_ids),
                        reason="Stall timeout exceeded after one retry")

            blocked_path = war_room / f"slot-{slot_id}-blocked.md"
            blocked_path.write_text(
                f"# Slot {slot_id} — Blocked\n\n"
                f"**Reason:** Repeated stall. Agents {', '.join(all_agent_ids)} timed out.\n"
                f"Manual investigation required.\n",
                encoding="utf-8",
            )
    else:
        update_heartbeat(war_room, slot_id)


def _handle_pending(
    war_room: Path, slot_id: str, workspace: Path,
    config: dict, active_processes: dict,
) -> None:
    slot_start = war_room / f"slot-{slot_id}-start.md"
    if not slot_start.exists():
        return

    agent_md = workspace / "agents" / "abd-team-member" / "AGENT.md"
    instructions = war_room / "INSTRUCTIONS.md"

    prompt = assemble_bootstrap_prompt(
        war_room, slot_start, agent_md,
        instructions if instructions.exists() else None,
    )

    result = launch_agent(prompt, workspace, config)
    if result.get("error"):
        print(f"[Harness] Launch failed: {result['error']}", file=sys.stderr)
        run_log.append(war_room, "LAUNCH_FAILED", slot_id=slot_id, error=result["error"])
        return

    agent_id = result["agent_id"]
    run_id = result["run_id"]
    active_processes[slot_id] = result.get("process")

    agent_mode = result.get("mode", "local")
    write_running_file(war_room, slot_id, agent_id, run_id, mode=agent_mode)
    run_log.append(war_room, "RUNNING", slot_id=slot_id, agent_id=agent_id, run_id=run_id, mode=agent_mode)
    print(f"[Harness] Launched slot {slot_id} — agent {agent_id}")


def _extract_summary(finished_path: Path) -> str:
    if not finished_path.exists():
        return "no summary"
    text = finished_path.read_text(encoding="utf-8")
    for line in text.splitlines():
        if line.startswith("##") and "artifact" in line.lower():
            return line.strip("# ").strip()
    return text[:200]


def _extract_question(blocked_path: Path) -> str:
    if not blocked_path.exists():
        return "no question"
    text = blocked_path.read_text(encoding="utf-8")
    in_question = False
    for line in text.splitlines():
        if line.startswith("## Question"):
            in_question = True
            continue
        if in_question and line.startswith("##"):
            break
        if in_question and line.strip():
            return line.strip()
    return text[:200]


def _prompt_engagement_params(workspace: Path) -> dict[str, Any]:
    """Interactively prompt for missing required engagement parameters."""
    params: dict[str, Any] = {"workspace": str(workspace)}

    context = input("[Harness] Context brief (path to docs or inline description): ").strip()
    if not context:
        print("Error: Context brief is required.", file=sys.stderr)
        sys.exit(1)
    params["context"] = context

    profile = input("[Harness] Profile (greenfield/brownfield/small-build/feature/bespoke): ").strip().lower()
    if profile not in ("greenfield", "brownfield", "small-build", "feature", "bespoke"):
        print(f"Error: Invalid profile '{profile}'.", file=sys.stderr)
        sys.exit(1)
    params["profile"] = profile

    autonomy = input("[Harness] Autonomy level (tight/moderate/full): ").strip().lower()
    if autonomy not in ("tight", "moderate", "full"):
        print(f"Error: Invalid autonomy level '{autonomy}'.", file=sys.stderr)
        sys.exit(1)
    params["autonomy"] = autonomy

    channel = input("[Harness] Notification channel (URL or blank for console): ").strip()
    if channel:
        params["notification_channel"] = channel

    timeout = input("[Harness] Stall timeout override in minutes (blank for default): ").strip()
    if timeout:
        try:
            params["stall_timeout_minutes"] = int(timeout)
        except ValueError:
            print(f"Warning: Invalid timeout '{timeout}', using default.", file=sys.stderr)

    return params


def main() -> None:
    parser = argparse.ArgumentParser(description="ABD CLI Delivery Harness")
    subparsers = parser.add_subparsers(dest="command")

    run_parser = subparsers.add_parser("run", help="Start the harness main loop")
    run_parser.add_argument("workspace", type=Path)
    run_parser.add_argument("--config", type=Path, default=None)

    status_parser = subparsers.add_parser("status", help="Show engagement status")
    status_parser.add_argument("workspace", type=Path)

    args = parser.parse_args()

    if args.command == "status":
        cmd_status(args.workspace)
    elif args.command == "run":
        config = load_config(args.config)
        cmd_run(args.workspace, config)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
