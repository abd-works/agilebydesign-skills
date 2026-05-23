# CLI Delivery Harness

Durable, observable ABD delivery that survives walk-away, recovers from stalls, and scales run independence as error rates drop.

## Quick start

```bash
pip install -r cli_harness/requirements.txt

# Show engagement status
python -m cli_harness status <workspace-path>

# Start the harness main loop (prompts interactively for new engagements)
export CURSOR_API_KEY=your-key
python -m cli_harness run <workspace-path>
```

## Prerequisites

1. **Cursor SDK** (`pip install cursor-sdk`) — preferred. Falls back to **Cursor CLI** on PATH if SDK is not installed (local mode only).
2. **API key** set via `CURSOR_API_KEY` env var or `cli_harness/cli-config.json`
3. **War room initialized** — delivery lead agent must have run Steps 1-2 and created `delivery-war-room/`

## Agent modes

The harness supports two execution modes, selected by `agent_mode` in config:

### Local (`"agent_mode": "local"`)

Agents run on the operator's machine against the local workspace. Uses the Cursor SDK (`LocalAgentOptions`) when installed, otherwise falls back to `cursor agent` CLI subprocess.

### Cloud (`"agent_mode": "cloud"`)

Agents run on Cursor-hosted VMs against a cloned repo. Requires `repo_url` in config. Walk-away friendly — no open IDE or terminal needed. Uses the Cursor SDK (`CloudAgentOptions`).

Cloud agent IDs are prefixed with `bc-`. The SDK auto-detects runtime on resume.

## Architecture

```
cli_harness/
  harness.py        # Main loop: read manifest → find slot → launch/monitor/recover
  config.py         # Read ~/.cursor/cli-config.json + engagement overrides
  manifest.py       # Parse manifest.md YAML blocks
  slot_state.py     # Slot lifecycle detection from war room files
  agent_launcher.py # Assemble bootstrap prompt, launch via Cursor CLI
  run_log.py        # Append-only run-log.jsonl operations
  notify.py         # Notification dispatch (console, webhook)
```

## Commands

### `status`

Reads manifest, active slot, checklist progress, and last log entry. One-line summary.

### `run`

Main loop that:
1. Reads `manifest.md` and `run_sizing_policy`
2. Finds active slot (smallest NN with start, no finished)
3. On PENDING: assembles bootstrap prompt, launches team member agent
4. On RUNNING: monitors heartbeat, detects stalls, retries once
5. On BLOCKED: notifies operator, waits for answer file
6. On FINISHED: notifies operator, signals delivery lead
7. On FAILED: notifies operator after retry exhaustion

## Configuration

### `~/.cursor/cli-config.json`

```json
{
  "api_key": "your-cursor-api-key",
  "agent_mode": "local",
  "repo_url": null,
  "repo_ref": "main",
  "model": "composer-2.5",
  "stall_timeout_minutes": 15,
  "notification_channel": null,
  "sandbox": false,
  "mcp_allowlist": []
}
```

Set `agent_mode` to `"cloud"` and provide `repo_url` for walk-away execution on Cursor VMs.

### Engagement overrides

Per-engagement overrides are stored in `delivery-war-room/harness-config.json` (written by harness on first run). The manifest's `run_sizing_policy` further adjusts stall timeout and notification detail.

## War room contract

The harness interacts exclusively through war room files:
- Reads: `manifest.md`, `slot-NN-start.md`, `slot-NN-finished.md`, `slot-NN-blocked.md`, `slot-NN-answer.md`
- Writes: `slot-NN-running.json`, `run-log.jsonl`
- Never writes: `manifest.md`, `slot-NN-start.md`, `INSTRUCTIONS.md` (delivery lead's job)
