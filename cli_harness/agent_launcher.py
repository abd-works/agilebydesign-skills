"""Launch and manage Cursor agents via SDK — local or cloud."""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any


def assemble_bootstrap_prompt(
    war_room: Path,
    slot_start_path: Path,
    agent_md: Path,
    instructions_path: Path | None = None,
) -> str:
    parts: list[str] = []

    if instructions_path and instructions_path.exists():
        parts.append(instructions_path.read_text(encoding="utf-8"))

    parts.append(slot_start_path.read_text(encoding="utf-8"))
    parts.append(agent_md.read_text(encoding="utf-8"))

    return "\n\n---\n\n".join(parts)


def launch_agent(
    prompt: str,
    workspace: Path,
    config: dict[str, Any],
    agent_type: str = "team-member",
) -> dict[str, Any]:
    """Launch an agent via Cursor SDK. Uses cloud when configured, local otherwise."""
    api_key = config.get("api_key") or os.environ.get("CURSOR_API_KEY")
    if not api_key:
        return {"agent_id": None, "run_id": None, "error": "No API key configured"}

    mode = config.get("agent_mode", "local")
    repo_url = config.get("repo_url")
    repo_ref = config.get("repo_ref", "main")
    model = config.get("model", "composer-2.5")

    try:
        from cursor_sdk import Agent, AgentOptions, LocalAgentOptions, CloudAgentOptions
    except ImportError:
        return _launch_cli_fallback(prompt, workspace, api_key)

    try:
        if mode == "cloud" and repo_url:
            agent = Agent.create(
                model=model,
                api_key=api_key,
                cloud=CloudAgentOptions(repos=[{"url": repo_url, "ref": repo_ref}]),
            )
        else:
            agent = Agent.create(
                model=model,
                api_key=api_key,
                local=LocalAgentOptions(cwd=str(workspace)),
            )

        run = agent.send(prompt)

        return {
            "agent_id": agent.id,
            "run_id": run.id,
            "agent": agent,
            "run": run,
            "mode": mode if mode == "cloud" and repo_url else "local",
        }

    except Exception as e:
        error_msg = str(e)
        print(f"[Harness] SDK launch failed: {error_msg}", file=sys.stderr)
        if mode == "local":
            return _launch_cli_fallback(prompt, workspace, api_key)
        return {"agent_id": None, "run_id": None, "error": error_msg}


def _launch_cli_fallback(
    prompt: str, workspace: Path, api_key: str,
) -> dict[str, Any]:
    """Fall back to cursor CLI subprocess when SDK is not installed."""
    import subprocess
    import uuid

    agent_id = str(uuid.uuid4())
    run_id = str(uuid.uuid4())

    env = dict(os.environ)
    env["CURSOR_API_KEY"] = api_key

    cmd = [
        "cursor", "agent",
        "-p", prompt,
        "--trust", "--force",
        "--output-format", "stream-json",
    ]

    try:
        process = subprocess.Popen(
            cmd,
            cwd=str(workspace),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
    except FileNotFoundError:
        return {
            "agent_id": agent_id,
            "run_id": run_id,
            "process": None,
            "error": "cursor CLI not found and cursor-sdk not installed — install one of them",
        }

    return {
        "agent_id": agent_id,
        "run_id": run_id,
        "process": process,
        "pid": process.pid,
        "mode": "cli-local",
    }


def cancel_agent(agent_or_process: Any) -> None:
    if agent_or_process is None:
        return

    if hasattr(agent_or_process, "terminate"):
        try:
            agent_or_process.terminate()
            agent_or_process.wait(timeout=10)
        except Exception:
            try:
                agent_or_process.kill()
            except Exception:
                pass
    elif hasattr(agent_or_process, "__exit__"):
        try:
            agent_or_process.__exit__(None, None, None)
        except Exception:
            pass


def resume_agent(agent_id: str, config: dict[str, Any]) -> dict[str, Any]:
    """Resume an existing agent by ID. Cloud agents have bc- prefix."""
    api_key = config.get("api_key") or os.environ.get("CURSOR_API_KEY")
    if not api_key:
        return {"error": "No API key configured"}

    try:
        from cursor_sdk import Agent, AgentOptions
    except ImportError:
        return {"error": "cursor-sdk not installed — cannot resume agents"}

    try:
        agent = Agent.resume(agent_id, AgentOptions(api_key=api_key))
        return {"agent_id": agent.id, "agent": agent}
    except Exception as e:
        return {"error": str(e)}
