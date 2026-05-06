---
name: abd-practice-pipeline
catalog_garden_tier: foundational
catalogue_one_liner: >-
  Uniform 7-step lifecycle for any ABD practice skill: rules-guided generate, validate, scan, save graph, render drawio, corrections.
description: >-
  Composes the four engine skills (execute-skill-using-skills-rules, correct_output,
  story-graph-ops, drawio-story-sync) into one repeatable lifecycle for every practice
  skill in idea shaping/, domain-driven-design/, and story-driven-delivery/. Use whenever a
  practice skill produces a markdown deliverable that should also live as story-graph.json
  and a draw.io diagram, with corrections logged into the skill being corrected.
---

# abd-practice-pipeline

This skill is **pure composition**. It owns no rules, no scanners, no templates of its own. Its job is to **wire the four engines** into one consistent flow so every practice skill behaves the same way.

| Engine | Owns |
| --- | --- |
| **execute-skill-using-skills-rules** | Rules pass + scanner pass; the gate before and after work |
| **correct_output** | The corrections loop, ledger on disk |
| **story-graph-ops** | `story-graph.json` lifecycle on disk (CLI + Python) |
| **drawio-story-sync** | `.drawio` render + sync from JSON, and JSON write-back from drawio |

## When to use

Load **abd-practice-pipeline** whenever you (or a user prompt) start work on a deliverable produced by a practice skill from one of these families:

- **idea shaping/** — `abd-cost-of-delay`, `abd-impact-mapping`, `abd-opportunity-generation`, `abd-simple-validated-learning`
- **domain-driven-design/** — `abd-domain-language`, `abd-key-abstractions`, `abd-domain-sketch`, `abd-class-responsibility-collaborator`, `abd-module-partition`, `abd-object-model`, `abd-scenario-walkthrough`
- **story-driven-delivery/** — `abd-story-mapping`, `abd-thin-slicing`, `abd-acceptance-criteria`, `abd-acceptance-test-driven-development`, `abd-specification-by-example`

If the deliverable does not need a story graph or a diagram (rare), still run steps **1–3 and 7** — they are the always-on quality contract.

## The 7 steps

| # | Step | Driver | Trigger |
| --- | --- | --- | --- |
| 1 | **Generate MD** with rules as guidance | execute-skill-using-skills-rules — *rules pass, before work* | Skill invocation (chat, prompt, or CLI) |
| 2 | **Validate MD** against rules (AI pass) | execute-skill-using-skills-rules — *rules pass, after work* | After step 1, and again after every chat-driven edit |
| 3 | **Scan & fix** | execute-skill-using-skills-rules — `scripts/run_scanners.py` | After step 2 |
| 4 | **Save to `story-graph.json`** | story-graph-ops — `story_graph_cli.py write` then `read` | On MD finalize, gated by **`md_to_json`** |
| 5 | **Render `.drawio`** | drawio-story-sync — `drawio_story_sync_cli.py render` (or `sync` if outline already exists) | On JSON change, gated by **`json_to_drawio`** |
| 6 | **Save JSON on drawio edit** | drawio-story-sync — `sync` → story-graph-ops `read` | On `.drawio` save, gated by **`drawio_to_json`** |
| 7 | **Corrections** | correct_output | Whenever chat or a reviewer corrects MD output — **always** |

Steps **2 → 7** re-fire on every subsequent chat edit to the MD: the gate runs *before* (rules pass on the new state), the work happens, then *after* (validate + scan + save policy + corrections if anything was wrong).

## y/n/p decision points (the three gates)

Three places ask the user before mutating a sibling artifact. Each is a tri-state with a documented default:

| Gate | Default | Yes | No | Prompt |
| --- | --- | --- | --- | --- |
| **`md_to_json`** — write `story-graph.json` after MD finalize | **prompt** | always save | never save | ask once per file |
| **`json_to_drawio`** — render `.drawio` after JSON change | **yes** | always render | never render | ask once per change |
| **`drawio_to_json`** — write JSON when `.drawio` is edited | **prompt** | always sync back | never sync back | ask once per change |

### Where defaults live

- **Workspace default:** `pipeline.yaml` at the engagement root.

  ```yaml
  defaults:
    md_to_json: prompt
    json_to_drawio: yes
    drawio_to_json: prompt
  ```

- **Per-document override:** YAML frontmatter on the markdown file.

  ```yaml
  ---
  abd_pipeline:
    md_to_json: yes
  ---
  ```

Frontmatter wins over `pipeline.yaml`. Chat answers ("yes" / "no") for a single turn never persist — to persist, ask the user to update the file or `pipeline.yaml`.

## Always-on rules

Two workspace rules are non-negotiable inside this pipeline (they already exist as `.cursor/rules/*.mdc` and as `.github/instructions/*.instructions.md` in any testbed):

1. **execute-rules-gate** — before running step 1 of any skill that has `rules/` or `scanners/`, follow `skills/skill-helpers/execute-skill-using-skills-rules/SKILL.md`. No improvisation.
2. **correct-output** — every correction (output mistake **or** process correction) gets a ledger entry **on disk in the same turn** under the **target skill**: `<target-skill>/corrections-log.md`. Chat is not the record.

## Pipeline CLI (testbed)

The reference implementation ships with the testbed at `test/abd-practice-pipeline-testbed/scripts/pipeline.py`. It is a thin shell that calls the existing engine CLIs — it does **not** reimplement them.

```text
python scripts/pipeline.py validate   --skill <skill-root> --doc <md>
python scripts/pipeline.py save-graph --doc <md>     --graph <story-graph.json>
python scripts/pipeline.py render     --graph <json> --drawio <out.drawio> [--mode outline|exploration|increments]
python scripts/pipeline.py sync-back  --drawio <drawio> --graph <story-graph.json>
python scripts/pipeline.py run        --skill <skill-root> --doc <md>      # full sequence with gates
python scripts/pipeline.py watch      --root <engagement-root>             # background watcher
```

Each subcommand reads `pipeline.yaml` + the doc's frontmatter, decides y/n/p, and shells out to:

- `skills/skill-helpers/execute-skill-using-skills-rules/scripts/run_scanners.py`
- `skills/story-driven-delivery/story-graph-ops/scripts/story_graph_cli.py`
- `skills/story-driven-delivery/drawio-story-sync/scripts/drawio_story_sync_cli.py`

## IDE surface

**VSCode-native primary** — Copilot Chat in agent mode reads `AGENTS.md`, `.github/instructions/*.instructions.md`, `.github/prompts/*.prompt.md`, `.github/chatmodes/*.chatmode.md`. Save-time reactivity is provided by the watcher launched from `.vscode/tasks.json` (`runOn: folderOpen`).

**Cursor 1-1 mirrors only** — `.cursor/commands/*.prompt.md` mirrors `.github/prompts/*` (same names). `.cursor/hooks.json` adds `afterFileEdit` reactivity for Cursor users; this is the single Cursor-only feature with no VSCode-native equivalent.

**Bundle commands** — `.vscode/tasks.json` exposes one task per pipeline subcommand plus `abd: run pipeline` and `abd: watch docs`. Both Cursor and VSCode pick these up.

## See also

- `skills/skill-helpers/execute-skill-using-skills-rules/SKILL.md` — rules gate
- `skills/skill-helpers/correct_output/SKILL.md` — corrections loop
- `skills/story-driven-delivery/story-graph-ops/SKILL.md` — JSON CRUD
- `skills/story-driven-delivery/drawio-story-sync/SKILL.md` — drawio sync
- `test/abd-practice-pipeline-testbed/` — reference wiring with all IDE surfaces
