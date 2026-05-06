# abd-practice-pipeline-testbed

A **walkable** reference for the seven-step lifecycle every ABD practice skill follows.

## What this proves

You can run any practice skill (`abd-story-mapping`, `abd-domain-language`, `abd-cost-of-delay`, …) through one consistent flow — generate, validate, scan, save graph, render diagram, log corrections — using **VSCode-native primitives** for everything except save-time reactivity, which is added once via a small Python watcher (and a Cursor `hooks.json` for Cursor users).

## Quick start

### 1. Install runtime deps (one-time)

```powershell
cd test\abd-practice-pipeline-testbed
pip install -r scripts\requirements.txt
```

### 2. Open the folder in VSCode (or Cursor)

```powershell
code test\abd-practice-pipeline-testbed
# or
cursor test\abd-practice-pipeline-testbed
```

The watcher starts automatically (`abd: watch docs` task, `runOn: folderOpen`).

### 3. Try the lifecycle

| You do | What fires |
| --- | --- |
| Edit `story/feature-discovery.md` and save | Watcher → `pipeline.py validate` → AI rules pass + `run_scanners.py` |
| Type `/abd-save-graph story/feature-discovery.md` in chat | `pipeline.py save-graph` → asks (`md_to_json: prompt`) → writes `story-graph.json` and validates with `story_graph_cli.py read` |
| `story-graph.json` appears | `json_to_drawio: yes` triggers `drawio_story_sync_cli.py render` → `story/feature-discovery.drawio` |
| You hand-edit the `.drawio` and save | Watcher asks (`drawio_to_json: prompt`) → on yes runs `drawio_story_sync_cli.py sync` |
| Chat says "actually that epic name is wrong" | Always-on rule: agent appends to `skills/story-driven-delivery/abd-story-mapping/corrections-log.md` **before** re-generating |

## Slash commands available

| VSCode (Copilot Chat) | Cursor | What it does |
| --- | --- | --- |
| `/abd-run-practice <skill> <doc>` | same | Full 7-step run for a doc |
| `/abd-validate-doc <doc>` | same | Step 2 + 3 — rules pass + scanner pass |
| `/abd-save-graph <doc>` | same | Step 4 — write `story-graph.json` |
| `/abd-render-drawio <graph>` | same | Step 5 — render `.drawio` |
| `/abd-sync-back <drawio>` | same | Step 6 — drawio → JSON |

## VSCode tasks (Cmd/Ctrl-Shift-P → "Run Task")

- `abd: validate doc` — prompt for path, runs step 2 + 3
- `abd: save graph` — prompt for path, runs step 4
- `abd: render drawio` — prompt for graph path, runs step 5
- `abd: sync drawio back to graph` — runs step 6
- `abd: run pipeline` — runs full 7-step flow
- `abd: watch docs` — long-running watcher (auto-starts on folder open)

## What is **not** here on purpose

- **No new scanners or rules.** The composer skill `abd-practice-pipeline` reuses the four existing engines verbatim.
- **No re-implementation of CLIs.** `pipeline.py` shells out to `run_scanners.py`, `story_graph_cli.py`, `drawio_story_sync_cli.py`. If the engines change, the pipeline picks it up for free.
- **No Cursor-specific UI.** Cursor's `commands/` and `hooks.json` are kept to a strict 1-1 mirror of the VSCode-native surface. The hooks are the **only** Cursor-only feature, and only because VSCode lacks a chat-side save hook.

## Layout

See `AGENTS.md` for the full tree and per-file purpose.
