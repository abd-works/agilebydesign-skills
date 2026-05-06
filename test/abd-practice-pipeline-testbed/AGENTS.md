# abd-practice-pipeline-testbed

> Reference wiring for the **abd-practice-pipeline** skill.
> Demonstrates the 7-step lifecycle on a single sample doc using **VSCode-native** primitives, with a 1-1 Cursor mirror.

## How agents (you) should behave in this folder

You are running inside an **engagement** that uses the **abd-practice-pipeline**. Read these in order:

1. `../../skills/skill-helpers/abd-practice-pipeline/SKILL.md` — the lifecycle
2. `../../skills/skill-helpers/execute-skill-using-skills-rules/SKILL.md` — the rules gate
3. `../../skills/skill-helpers/correct_output/SKILL.md` — the corrections loop
4. The **target** practice skill (e.g. `../../skills/story-driven-delivery/abd-story-mapping/SKILL.md`) — what "good" looks like

### Non-negotiable behavior

- Before producing any deliverable from a practice skill: read **its** `rules/*.md` (rules pass).
- After producing any deliverable: validate against **its** rules (AI pass) **and** run `run_scanners.py` (scanner pass).
- After **any** correction (output mistake or process correction) from the user: append an entry to **`<target-skill>/corrections-log.md`** (the skill being corrected) **on disk in the same turn**. Chat is not the record. See `correct_output/SKILL.md` § *Where the corrections log lives*.
- After producing or editing **`story/*.md`**: respect the y/n/p gates in `pipeline.yaml` (or the doc's frontmatter) before writing `story-graph.json`.
- After `story-graph.json` changes: respect `json_to_drawio` (default **yes**) before re-rendering.
- After **`*.drawio`** is edited by hand: respect `drawio_to_json` (default **prompt**) before writing JSON back.

### How to invoke the pipeline

Three equivalent surfaces — pick whichever is in front of you:

1. **VSCode Copilot Chat** — type `/abd-run-practice`, `/abd-validate-doc`, `/abd-save-graph`, `/abd-render-drawio`, `/abd-sync-back`. They live in `.github/prompts/`.
2. **Cursor Chat** — same names, mirrored in `.cursor/commands/`.
3. **Terminal** — `python scripts/pipeline.py <subcommand> ...`. The VSCode tasks in `.vscode/tasks.json` wrap these.

### Save-time reactivity

- **Cursor:** `.cursor/hooks.json` fires `afterFileEdit` and re-runs the gate. No setup required.
- **VSCode:** run the **`abd: watch docs`** task (auto-starts on folder open via `runOptions.runOn`). It watches `story/**/*.md` and `**/*.drawio` and calls `pipeline.py` when files change.

## Default y/n/p

In `pipeline.yaml`:

| Gate | Default |
| --- | --- |
| `md_to_json` | **prompt** |
| `json_to_drawio` | **yes** |
| `drawio_to_json` | **prompt** |

Per-doc frontmatter overrides the workspace default.

## Layout

```
test/abd-practice-pipeline-testbed/
├── AGENTS.md               # this contract for agents
├── README.md               # human walkthrough
├── pipeline.yaml           # workspace y/n/p defaults
├── story/
│   └── feature-discovery.md  # sample input (story-mapping deliverable)
├── .vscode/
│   ├── tasks.json          # bundle commands + watcher
│   └── settings.json
├── .github/
│   ├── instructions/abd-pipeline.instructions.md   # applyTo: story/**/*.md
│   ├── chatmodes/abd-practice.chatmode.md
│   └── prompts/                                    # 5 slash commands
├── .cursor/
│   ├── commands/           # 1-1 mirror of .github/prompts/
│   └── hooks.json          # afterFileEdit reactivity
└── scripts/
    ├── pipeline.py         # the orchestrator (calls existing engine CLIs)
    ├── pipeline_watch.py   # watchdog over story/ and *.drawio
    └── requirements.txt
```

## Corrections log

This testbed has its **own** `corrections-log.md` only if a correction targets *the testbed wiring*. Corrections against a **practice skill's output** go to `<that-skill>/corrections-log.md` per the always-on workspace rule. Corrections against `pipeline.py` or these files go here.
