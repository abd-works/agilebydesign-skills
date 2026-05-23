# CLI Delivery Harness — Contract

> Durable, observable ABD delivery that survives walk-away, recovers from stalls, and scales run independence as error rates drop.

---

# Ubiquitous Language — Actors and Key Concepts

---
state: ubiquitous-language
---

## Module: [CLI Delivery Harness]

> **Status: NEW** — this module does not exist yet; it is being designed in this contract.

_The execution and durability layer: configure, launch agents, monitor heartbeats, recover from stalls, notify humans, resume from disk._

Scope: The outer process and disk state that make ABD delivery walk-away durable, observable from any device, and resumable without re-briefing.

**Terms**:
- **Engagement**
  - **engagement** — a bounded unit of delivery work with its own workspace, plan, war room, and artifacts
  - **engagement workspace** — absolute path to the root folder; contains all artifacts, war room, and plan
  - **engagement parameters** — the full set of inputs the operator provides: workspace path, context brief, profile, autonomy level, notification channel, stall timeout, start/end stage preferences
  - **harness configuration** — one-time setup: API key, default stall timeout, notification channel, permissions, sandbox mode, MCP allowlist
  - **profile** — engagement shape: greenfield, brownfield, small-build, feature, or bespoke
  - **context brief** — source material provided by the operator: documents, links, API refs, prior work
- **War Room**
  - **war room** — the `delivery-war-room/` folder; disk-based source of truth for slot state, blockers, and audit
  - **manifest** — `manifest.md`; goal, profile, autonomy level, checkpoint policy, ordered slot definitions
  - **run log** — `run-log.jsonl`; append-only audit trail of every slot launch, block, resume, stall, and completion
  - **instructions** — `INSTRUCTIONS.md`; verbatim protocol the team member agent reads on autostart
- **Slot**
  - **slot** — a unit of delegated work assigned to one team member agent for one stage of one run
  - **slot start file** — `slot-NN-start.md`; full bootstrap handoff: role, workspace, stage, scope, skills, corrections, early questions
  - **running file** — `slot-NN-running.json`; agent_id, run_id, timestamps, heartbeat
  - **finished file** — `slot-NN-finished.md`; artifact paths, scanner results, timestamp
  - **blocked file** — `slot-NN-blocked.md`; question, context paths, reason for stop
  - **answer file** — `slot-NN-answer.md`; human-written response to unblock
  - **active slot** — smallest NN where start exists and finished does not
  - **slot lifecycle** — PENDING → RUNNING → BLOCKED → FINISHED | FAILED
- **Operator**
  - **operator** — human who initiates engagements, approves plans, reviews gates, answers blockers
  - **checkpoint** — mandatory stop where the delivery lead agent presents output and waits for operator approval
  - **autonomy level** — tight, moderate, or full; governs delivery lead's freedom to change runs
- **CLI Harness**
  - **cli harness** — outer process that launches agents, monitors heartbeats, recovers from stalls, sends notifications, reads run sizing policy from manifest to adjust enforcement
  - **agent mode** — execution target: `local` (operator machine) or `cloud` (Cursor-hosted VM); set in harness configuration
  - **local agent** — agent launched via Cursor SDK `LocalAgentOptions` against the local workspace; falls back to CLI subprocess when SDK is not installed
  - **cloud agent** — agent launched via Cursor SDK `CloudAgentOptions` against a cloned repo on a Cursor-hosted VM; walk-away durable, no open terminal required; agent ID prefixed `bc-`
  - **repo url** — GitHub repository URL used by cloud mode to clone the workspace into the VM
  - **heartbeat** — timestamp in running file updated every 60 seconds while agent streams output
  - **stall timeout** — configurable duration after which a stale heartbeat triggers recovery
  - **retry** — one automatic relaunch of the same slot with the same bootstrap prompt
  - **notification** — message sent to operator via configured channel on block, stall, failure, or completion
  - **status command** — CLI harness command reading manifest, active slot, checklist progress, and last log entry; returns one-line engagement summary
  - **session kill** — operator closing terminal, restarting machine, or losing connectivity; harness recovers from disk on restart; cloud agents survive session kill and resume by ID

---

_The *CLI harness* reads the *war room* on startup, finds the *active slot*, launches agents, monitors *heartbeats*, and recovers from *stalls*. It reads the *run sizing policy* from the *manifest* and adjusts checkpoint frequency, notification content, and *stall timeout* accordingly. The *operator* configures the harness once (*harness configuration*) — including *agent mode* (local or cloud) and optionally a *repo url* — then provides *engagement parameters* per engagement, interactively prompted for anything missing. In *local* mode, agents run on the operator's machine via the Cursor SDK (`LocalAgentOptions`), falling back to CLI subprocess when the SDK is not installed. In *cloud* mode, agents run as *cloud agents* on Cursor-hosted VMs via `CloudAgentOptions`, making the engagement walk-away durable — no open terminal or IDE required. The *war room* is the complete interface: any human can read *manifest*, *run log*, and slot files from any device without an open session. The *status command* provides a one-line engagement summary without launching agents. When the *operator* writes an *answer file*, the *CLI harness* resumes the blocked agent. On *session kill*, the harness reads disk and picks up where it left off — local stale *running files* from killed sessions are treated as stalls; *cloud agents* survive session kill and resume by ID (prefixed `bc-`)._

---

## Module: [Lead Delivery Through Agents]

> **Status: EXISTS / EXTENDING** — the delivery lead agent (`agents/abd-delivery-lead/`), team member agent (`agents/abd-team-member/`), and their skills already exist. This module describes what they do in the context of the harness, and where they need extending (risk-based harness enforcement, early question triggers from corrections, reviewer slots).

_The orchestration and execution layer: delivery lead builds plans and authors slots; team member agents execute stage work; reviewers validate; adaptive run sizing learns from corrections._

Scope: The agent roles, skills, risk classification, run sizing, gate validation, and slot chaining that drive what happens inside each slot — as orchestrated by the delivery lead and executed by team members.

**Terms**:
- **Delivery Lead Agent**
  - **delivery lead agent** — agent that orchestrates the 8-step workflow: establish workspace, build plan, open stage, bootstrap team member, validate exit, hand off, revise plan, complete. Does not produce stage artifacts — delegates to team members and validates their output. On resume after session kill, reads war room state and resumes without re-running completed stages
  - **agile delivery plan** — narrative plan document at `<workspace>/agile-delivery-plan.md`; runs, stages, scope, rationale, context inventory, risk classification
  - **plan changelog** — `<workspace>/agile-delivery-plan.changelog.md`; append-only record of plan revisions after each run
  - **delivery plan checklist** — `<workspace>/abd-delivery-lead/progress/delivery-plan-checklist.md`; generated by track_task, tracks stage completion with markdown checkboxes, preserves `[x]` state across regenerations
  - **run** — a planned sequence of stages with defined scope, checkpoint policy, and rationale; one engagement has one or more runs
  - **run summary** — structured entry in the run log at end of each run: stages completed, artifact quality, correction count, sizing outcome; triggers adaptive sizing review
  - **stage** — one phase of delivery work within a run; defined by `stages/<stage>.md` with entry conditions, exit gate, team role, and practice skill
  - **exit gate** — conditions from `stages/<stage>.md` that must pass before a stage is complete
  - **cross-stage check** — validation that current stage artifacts are consistent with prior stages
  - **slot chaining** — creating the next slot-start after validating the current slot-finished; loops back to open stage
- **Delivery Lead Skills**
  - **abd-delivery-planning** — skill the lead reads to assess context, classify risks, select a strategy, and design runs; lives at `skills/delivery/abd-delivery-planning/`
  - **strategy** — a strategy file under `abd-delivery-planning/strategies/` matching the engagement's risk profile; 9 exist (bug-fix, legacy-migration, new-initiative variants, new-thin-slice, new-user-story, regulatory-compliance, spike-poc)
  - **abd-delivery-war-room** — skill providing war room protocol, INSTRUCTIONS.md template, and slot file templates; lives at `skills/delivery/abd-delivery-war-room/`
  - **track_task** — skill the lead uses to generate and maintain the delivery plan checklist; lives at `skills/skill-helpers/track_task/`
  - **execute-skill-using-skills-rules** — skill providing scanner execution (`run_scanners.py`) and corrections logging; used by both lead (gate validation) and team member (artifact validation)
- **Stage Definitions**
  - **discovery** — stage producing a story map from raw context; team role: Product Owner; practice skill: abd-story-mapping; outputs: story-graph.json, story-map.md
  - **prioritization** — stage producing thin slices and ordering; team role: Product Owner; practice skill: abd-thin-slicing; outputs: slice assignments in graph, thin-slicing.md
  - **exploration** — stage producing behavioral acceptance criteria; team role: Analyst; practice skill: abd-acceptance-criteria; outputs: AC arrays in graph, acceptance-criteria.md
  - **scenarios** (Story Definition) — stage producing spec-by-example scenarios with concrete values; team role: Analyst; practice skill: abd-specification-by-example; outputs: scenario files, graph references
  - **acceptance-tests** — stage producing executable RED tests; team role: Engineer; practice skill: abd-acceptance-test-driven-development; outputs: test files, test-to-story mapping
  - **engineering** — stage producing GREEN production code; team role: Engineer; practice skill: abd-clean-code; outputs: production code, refactored design
  - **default stage order** — discovery → prioritization → exploration → scenarios → acceptance-tests → engineering; not mandatory — runs pick subsets based on risk and scope
- **Team Member Agent**
  - **team member agent** — agent that executes stage work inside one slot; follows its own 8-step workflow: set up → sync → read skill rules → produce draft artifacts → self-review → present at mid-slot checkpoint → update graph via story-graph-ops → run scanners → verify outcomes → finish or block
  - **team role** — one of Product Owner, Analyst, or Engineer; determines which role playbook and practice skills the agent uses; assigned by the delivery lead in the slot start file
  - **role playbook** — `agents/abd-team-member/roles/<role>.md`; defines persona, goals, and "what good looks like" per delivery phase for each team role
  - **bootstrap prompt** — assembled from slot start file + AGENT.md + INSTRUCTIONS.md; the full context the team member reads on launch
  - **early question trigger** — condition in slot start file that forces the agent to stop and write blocked.md instead of guessing
  - **reviewer** — a team member agent with `team-role: reviewer` that validates prior slot output against exit gates and scanners; does not produce new stage artifacts
  - **story-graph-ops** — CLI and Python module for CRUD on story-graph.json; used by the team member to update the graph at each stage
- **Practice Skills** (used by team member, delegated by delivery lead)
  - **practice skill** — a skill package with SKILL.md, templates/, rules/*.md, and scanners/; the team member reads SKILL.md and rules before producing artifacts, then runs scanners after
  - **practice skill family** — a group of related practice skills for a delivery discipline: story-driven delivery (5 skills), domain-driven design (6 skills), architecture-centric delivery (4 skills), user experience design (3 skills), engineering (2 skills, shared)
  - **scanner** — automated check under a practice skill's `scanners/` folder; run via `execute-skill-using-skills-rules` to validate artifacts against rules
  - **stage artifact** — output files the team member produces using practice skill templates: story maps, AC, scenarios, tests, code, story-graph.json updates
  - **corrections log** — `<workspace>/docs/corrections-log.md`; written by team member on user correction at checkpoints; read by delivery lead for gate validation and adaptive sizing
  - **story-graph.json** — structured graph of epics, stories, AC, scenarios maintained by story-graph-ops; updated by team member at each stage, validated by delivery lead at gates
- **Adaptive Run Sizing**
  - **risk classification** — six risk types (value, technical, delivery, domain, integration, AI-model) that drive initial run shape; performed by delivery lead using abd-delivery-planning
  - **run sizing policy** — rules governing stories per slot, stages per run, and checkpoint frequency; initial state set by risk classification, adapted after each run
  - **harness enforcement** — how the CLI harness varies behavior (checkpoint pauses, notification content, stall timeout) based on current policy read from the manifest
  - **error rate** — frequency of correction entries per stage across recent slots; computed from corrections log
  - **autonomy escalation** — moving from tight → moderate → full as error rate drops; proposed by delivery lead, approved by operator

---

_The *delivery lead agent* follows an 8-step orchestration workflow. It establishes the *engagement workspace*, reads *abd-delivery-planning* and matching *strategies* to build the *agile delivery plan* with *risk classification*, then sets up the *war room* after *operator* approval. For each *stage* in a *run*, it reads the *stage definition*, verifies entry conditions, authors a *slot start file* with *team role*, ordered *practice skills*, filtered *corrections*, and *early question triggers* — then the *CLI harness* launches a *team member agent*. The *team member agent* bootstraps from its *role playbook*, syncs with existing workspace artifacts, reads the *practice skill* rules, produces draft *stage artifacts*, self-reviews against rules, and presents at a mid-slot *checkpoint* for *operator* confirmation. After confirmation it updates *story-graph.json* via *story-graph-ops*, runs *scanners*, verifies outcomes against the *role playbook*, and writes a *finished file* or *blocked file*. The *CLI harness* detects the *finished file* and notifies the *operator*. The *delivery lead agent* validates the *exit gate* and *cross-stage checks*, presents gate results at a stage *checkpoint* for *operator* approval, marks the stage in the *delivery plan checklist*, and chains to the next *slot*. After the last *slot* in a *run*, the *delivery lead agent* writes a *run summary*, appends to the *plan changelog*, reads the *corrections log* to compute the *error rate*, and proposes *run sizing policy* changes. The *CLI harness* reads the updated policy from the *manifest* and adjusts its enforcement. A *reviewer* is a team member that validates another slot's output before the lead signs off. On *session kill*, a fresh *delivery lead agent* reads the *war room* state and resumes without re-running completed stages. The *delivery lead agent* and *CLI harness* interact exclusively through the *war room* — neither calls the other directly._

---

## Core Domain

### Core Domain — Module: CLI Delivery Harness

> Concepts below belong to the **CLI Delivery Harness** module. All concepts here are **new**.

---

### Engagement

*Engagement* is the top-level bounded unit of delivery work. It owns the *engagement workspace* — the absolute path where all artifacts, the *war room*, the *agile delivery plan*, and the *corrections log* live. Every engagement has exactly one *profile* that shapes the default run structure, and one *autonomy level* that governs how much freedom the *delivery lead agent* has. The *engagement* is the container that makes everything resumable: its disk state is the complete brief — no chat history or session memory is required.

#### engagement

- owns one *engagement workspace* that is the root for all *stage artifacts*, the *war room*, and the *agile delivery plan*
- is initialized by the *operator* providing a workspace path and *context brief*
- has exactly one *profile* (greenfield, brownfield, small-build, feature, or bespoke) that shapes the default *run sizing policy*
- has exactly one *autonomy level* (tight, moderate, or full) that constrains *delivery lead agent* run-change freedom
- **Invariant:** an *engagement* is fully described by its disk state — no information lives only in chat or session memory

#### agile delivery plan

- is the narrative plan at `<workspace>/agile-delivery-plan.md`; written by the *delivery lead agent* using *abd-delivery-planning*
- contains context inventory (provided vs missing), risk classification, strategy name, and *run* definitions with concrete outcome rationales
- is updated by the *delivery lead agent* after each *run* completes or when the *operator* overrides
- **Invariant:** every run in the plan has a rationale naming a concrete outcome, not just a risk type

#### profile

- is a property of *engagement* — classifies the engagement shape (greenfield, brownfield, small-build, feature, bespoke)

#### context brief

- is a property of *engagement* — the source material the *operator* provides: documents, links, API references, prior work

#### engagement workspace

- is a property of *engagement* — the absolute path to the root folder

#### engagement parameters

- is the full set of inputs the *operator* provides to define a new *engagement*
- required: *engagement workspace* path, *context brief* (documents, links, API refs, prior work)
- required: *profile* (greenfield, brownfield, small-build, feature, bespoke) — shapes default *run sizing policy*
- required: *autonomy level* (tight, moderate, full) — constrains *delivery lead agent* run-change freedom
- optional: *notification* channel (email, Slack, webhook URL) — where block/stall/completion alerts go
- optional: *stall timeout* override — seconds before a stale *heartbeat* triggers recovery (defaults from *harness configuration*)
- optional: start-stage, end-stage — to resume or scope a partial run
- optional: MCP tools needed — which tool surfaces the *team member agent* requires
- is provided by the *operator* at session start; the *delivery lead agent* reads it and uses it to build the *agile delivery plan* and *manifest*
- **Invariant:** the *operator* must provide at minimum workspace path, context brief, profile, and autonomy level — the system does not guess these

#### harness configuration

- is a one-time setup for the *CLI harness*, stored at `~/.cursor/cli-config.json` or project `.cursor/cli.json`
- defines: API key (`CURSOR_API_KEY`), default *stall timeout*, default *notification* channel, permissions allowlist, sandbox mode, MCP server allowlist, approval mode
- is read by the *CLI harness* on startup before any *engagement* is loaded
- per-engagement overrides (from *engagement parameters*) take precedence over defaults
- **Invariant:** the *CLI harness* cannot launch agents without a valid API key and permissions configuration

#### Decisions made

- *Engagement* is the top-level container; it has no lifecycle independent of the *operator* creating it (independence test: depends on *operator* to exist, but is the central organizing concept).
- *Profile* is a type property of *engagement*, not a separate concept — all profiles follow the same planning/execution flow, differing only in default run shape.
- *Context brief* is a property — it is input material, not a behavioral concept.
- *Engagement parameters* is a concept — it is the full configuration surface with required and optional fields, read by both the *delivery lead agent* and the *CLI harness*.
- *Harness configuration* is a concept — it has its own storage location, its own defaults, and per-engagement override behavior.

#### References

**Ref — Contract goals**
Source: docs/cli-delivery-harness-contract.md
Locator: Section 14 — Goals this contract serves
Extract: whole

---

### War Room

*War Room* is the file-based source of truth for slot state, artifacts, blockers, and audit. It lives at `delivery-war-room/` under the *engagement workspace* and replaces paste-and-copy handoffs between orchestrator and executor threads. The *war room* is what makes the system observable from any device — the *manifest*, *run log*, and slot files are readable from a phone, another PC, or GitHub web without an open Cursor session.

#### war room

- lives at `<workspace>/delivery-war-room/` and contains *manifest*, *instructions*, *run log*, and all *slot* files
- is created by the *delivery lead agent* after the *operator* approves the *agile delivery plan*
- is the exclusive interface between the *CLI harness*, the *delivery lead agent*, and the *team member agent* — no handoff happens outside these files
- is the interface for the *operator* and *ABD team members* to check in on progress from any device
- **Invariant:** the *war room* is always the source of truth for slot state — if disk says finished, no agent needs to ask "is it done?"

#### manifest

- defines the goal, *profile*, *autonomy level*, checkpoint policy, and ordered *slot* definitions for the current *engagement*
- is written by the *delivery lead agent* and may be overridden by the *operator*
- is read by the *CLI harness* to determine the *active slot*
- **Invariant:** every slot in the *manifest* has an exact run_scope (story ids or slice id), not a qualitative description

#### run log

- is the append-only audit trail at `delivery-war-room/run-log.jsonl`
- records every *slot* launch, block, resume, stall, retry, failure, and completion with agent_id, run_id, and timestamps
- is read by the *operator* and *ABD team members* for progress monitoring, and by the *delivery lead agent* for *adaptive run sizing*

#### instructions

- is a property of *war room* — the verbatim protocol (`INSTRUCTIONS.md`) the *team member agent* reads on autostart

#### Decisions made

- *War room* is a concept, not a folder convention — it has distinct behavior (state machine for slots, audit trail, device-independent interface).
- *Manifest* is a concept — it defines the engagement's slot structure and is read by both agents and the harness.
- *Run log* is a concept — it has its own append-only behavior and is consumed by multiple actors.
- *Instructions* is a property — it is a static template file, not a behavioral concept.

#### References

**Ref — War room skill**
Source: skills/delivery/abd-delivery-war-room/SKILL.md
Locator: Workspace layout; Delivery lead — start of a cycle
Extract: whole

---

### Slot

*Slot* is the unit of delegated work. It binds together a stage, a role, a run scope, and a set of *practice skills* into one assignment for a *team member agent*. A *slot* has a strict lifecycle (PENDING → RUNNING → BLOCKED → FINISHED | FAILED) enforced by the files in the *war room*: the *slot start file* is the handoff in, the *finished file* is the handoff out, and the *blocked file* / *answer file* pair is the human-in-the-loop mechanism. The *delivery lead agent* authors slots; the *CLI harness* executes them; the *team member agent* fulfills them.

#### slot

- is created when the *delivery lead agent* writes a *slot start file* to the *war room*
- transitions through a lifecycle: PENDING (start file exists, no running file) → RUNNING (harness launched agent) → BLOCKED (agent needs human input) → FINISHED (scanners green, artifacts listed) or FAILED (stall timeout, unrecoverable error)
- is scoped to exactly one stage, one role, and one run scope (story ids or slice id)
- lists the *practice skills* to use and their order (or "agent determines")
- carries filtered *corrections* from prior slots via the `Affects` tag
- **Invariant:** a *slot* cannot be marked FINISHED until all listed *practice skill* *scanners* pass
- **Invariant:** a *slot* cannot be followed by the next *slot* until the *delivery lead agent* validates its *exit gate*

#### slot start file

- is the full bootstrap handoff at `slot-NN-start.md`; contains team-role, workspace, stage, run_scope, skills (ordered), corrections filter, checkpoint policy, and *early question triggers*
- is written only by the *delivery lead agent*, never by the *CLI harness* or *team member agent*
- **Invariant:** run_scope must be exact (story ids or slice id) — never a qualitative hand-wave

#### running file

- is `slot-NN-running.json`; carries agent_id, run_id, started_at, and last *heartbeat* timestamp
- is written and updated by the *CLI harness*
- is read by the *CLI harness* on loop for stall detection, and by the *operator* for live progress

#### finished file

- is `slot-NN-finished.md`; lists all *stage artifact* paths, scanner pass confirmation, and timestamp
- is written by the *team member agent* after all *scanners* pass
- is read by the *delivery lead agent* for gate validation and *slot chaining*

#### blocked file

- is `slot-NN-blocked.md`; carries the question, context paths, and reason for stop
- is written by the *team member agent* when an *early question trigger* fires or the agent cannot proceed
- triggers a *notification* to the *operator* via the *CLI harness*

#### answer file

- is `slot-NN-answer.md`; the *operator's* written response to unblock the agent
- can be written from any device — the file on disk is the interface
- triggers the *CLI harness* to resume the *team member agent*

#### active slot

- is a derived state: the smallest NN where *slot start file* exists and *finished file* does not
- is computed by the *CLI harness* on every loop iteration

#### slot lifecycle

- is a property of *slot* — the state machine: PENDING → RUNNING → BLOCKED → FINISHED | FAILED

#### Decisions made

- *Slot* is the central operational concept — it binds stage, role, scope, skills, and corrections into one unit of work.
- *Slot start file*, *finished file*, *blocked file*, *answer file*, *running file* are all concepts — each has distinct authorship, readership, and behavior.
- *Active slot* is a derived state, not a separate concept — it is computed, not stored.
- *Slot lifecycle* is a type property — the states are a fixed set with identical transition rules.

#### References

**Ref — Contract slot lifecycle**
Source: docs/cli-delivery-harness-contract.md
Locator: Section 4 — Slot lifecycle
Extract: whole

---

### Operator

*Operator* is the human who governs the engagement. The *operator* initiates engagements, approves plans at *checkpoints*, reviews *exit gates*, answers blockers, and decides the *autonomy level*. The *operator's* touch is lightest when things work — review at end of run, answer when blocked — and heaviest during cold start when the *run sizing policy* is tight and every *slot* gets a *checkpoint*.

#### operator

- initiates an *engagement* by providing the *engagement workspace* path and *context brief*
- approves or overrides the *agile delivery plan* at the planning *checkpoint*
- sets the *autonomy level* (tight, moderate, or full) that governs *delivery lead agent* run-change freedom
- reviews *exit gate* results presented by the *delivery lead agent* at stage *checkpoints*
- writes *answer files* to unblock *team member agents* — from any device
- receives *notifications* on block, stall, failure, and completion events

#### checkpoint

- is a mandatory stop where an agent presents output and waits for *operator* approval before proceeding
- two scopes: **stage checkpoint** (delivery lead presents gate results, operator approves stage exit) and **mid-slot checkpoint** (team member presents draft artifacts within a slot for operator confirmation before finalizing)
- frequency is governed by the *manifest* checkpoint_policy: after_every_slot, after_every_run, or on_block_only
- **Invariant:** no stage transition happens without a *checkpoint* unless checkpoint_policy explicitly allows it

#### autonomy level

- is a property of *engagement* — tight (lead proposes all changes, operator approves each), moderate (wider scope, fewer stops), or full (lead applies changes, notifies after)

#### ABD team member *(boundary)*

- is a human team member (not the agent) who checks in on *war room* files and *stage artifacts* from any device
- does not write *slot* files or approve *checkpoints* — only the *operator* does

#### Decisions made

- *Operator* is a concept — it has distinct identity, responsibilities (approve, answer, govern), and interactions with multiple other concepts.
- *Checkpoint* is a concept — it is a behavioral gate with its own invariant, not just a timestamp.
- *Autonomy level* is a type property of *engagement* — all levels follow the same governance flow, differing by degree.
- *ABD team member* (human) is boundary — this scope owns the operator role; human team members interact only as read-only observers of the *war room*.

#### References

**Ref — Contract goals**
Source: docs/cli-delivery-harness-contract.md
Locator: Section 14 — operator role is light
Extract: whole

---

### CLI Harness

*CLI Harness* is the durability layer — the outer process that makes agent execution walk-away safe. It reads the *war room*, launches *team member agents* for each *active slot*, monitors *heartbeats*, detects stalls, retries once, fails and notifies on repeated stalls, and resumes agents after the *operator* writes an *answer file*. The *CLI harness* never plans, never authors *slots*, and never runs *practice skills* — it is pure execution infrastructure.

#### cli harness

- runs as a loop: read *manifest* → find *active slot* → launch or monitor *team member agent* → detect stall/block/finish → act
- launches *team member agents* via `agent -p --trust --force --output-format stream-json` (headless) or via Cloud Agents API for unattended *slots*
- writes and updates *running files* with agent_id, run_id, and *heartbeat* timestamps
- appends every state transition to the *run log*
- sends *notifications* to the *operator* on block, stall, failure, and completion
- on restart, reads *war room state* and resumes from where it left off — no re-brief required
- **Invariant:** the *CLI harness* never creates *slot start files* — only the *delivery lead agent* authors *slots*
- **Invariant:** the *CLI harness* never runs *practice skills* or *scanners* — only the *team member agent* does

#### heartbeat

- is a timestamp in the *running file* updated every 60 seconds while the *team member agent* streams output
- is read by the *CLI harness* on every loop to detect stalls

#### stall timeout

- is a property of *CLI harness* — configurable duration after which a stale *heartbeat* triggers recovery

#### retry

- is one automatic relaunch of the same *slot* with the same *bootstrap prompt* and a new agent_id
- **Invariant:** at most one *retry* per *slot* — a second stall transitions to FAILED

#### notification

- is a message sent to the *operator* via a configured channel (email, Slack, webhook) on block, stall, failure, or completion
- carries the *slot* number, event type, relevant agent_ids, and summary text

#### status command

- is a CLI harness command that reads *manifest*, *active slot*, *delivery plan checklist* progress, and last *run log* entry
- returns a one-line engagement status summary (current stage, slot state, checklist progress)
- available to the *operator* without launching an agent or opening an IDE

#### session kill

- is the *operator* closing the terminal, restarting the machine, or losing connectivity mid-slot
- the *CLI harness* recovers by reading the *war room* on restart — no re-brief required
- a stale *running file* from a killed session is treated as a stall and follows the recovery flow

#### Decisions made

- *CLI harness* is a concept — it has distinct identity (the outer loop), state (current slot, heartbeat tracking), and behavior (launch, monitor, recover, notify).
- *Heartbeat*, *stall timeout*, *retry*, *notification* are all concepts — each has distinct behavior and interactions with other concepts.
- *Status command* is a concept — it provides a lightweight read-only status surface without launching agents.
- *Session kill* is a concept — it is a named recovery trigger with distinct behavior (stale heartbeat → stall flow).
- The harness does not own planning, skills, or gates — that boundary is invariant.

#### References

**Ref — Contract harness loop**
Source: docs/cli-delivery-harness-contract.md
Locator: Section 7 — CLI harness loop
Extract: whole

---

### Core Domain — Module: Lead Delivery Through Agents

> Concepts below belong to the **Lead Delivery Through Agents** module. The delivery lead agent, team member agent, and their skills **already exist** in `agents/abd-delivery-lead/`, `agents/abd-team-member/`, and `skills/`. Concepts marked **(extending)** describe new behavior this contract adds.

---

### Delivery Lead Agent

*Delivery Lead Agent* is the orchestrator. It builds the *agile delivery plan* using *abd-delivery-planning*, authors *slot start files* with exact scope and skill lists, validates *exit gates* after each *slot*, chains *slots* by writing the next *slot start file*, and proposes *run sizing policy* changes based on the *corrections log*. It never executes *practice skills* itself — it delegates to *team member agents* and validates their output.

#### delivery lead agent

- reads *abd-delivery-planning* SKILL.md and all `strategies/*.md` to build or revise the *agile delivery plan*
- creates the *war room* and writes the *manifest* after the *operator* approves the plan
- authors each *slot start file* with team-role, workspace, stage, exact run_scope, ordered skills, filtered corrections, and *early question triggers*
- validates *exit gates* by reading `stages/<stage>.md` and running *cross-stage checks* and *scanners* via *execute-skill-using-skills-rules*
- chains *slots* by writing the next *slot start file* after validating the current *finished file*
- writes a *run summary* to the *run log* at the end of each run
- proposes *run sizing policy* changes by reading the *corrections log* and *run log* after each run completes
- appends plan revisions to the *plan changelog* after each run
- uses *track_task* to maintain the *delivery plan checklist*
- on resume after *session kill*: a fresh session reads *manifest*, *run log*, *delivery plan checklist*, and *agile delivery plan*, determines where to resume from slot state, and does not re-run completed stages
- **Invariant:** never runs *practice skills* directly — always delegates to a *team member agent*
- **Invariant:** never opens slot N+1 without validating slot N *exit gate* (unless *manifest* declares override)

#### exit gate

- is a set of conditions from `stages/<stage>.md` that must all pass before a stage is complete
- is checked by the *delivery lead agent* against produced *stage artifacts*, the *corrections log*, and *scanner* results
- on failure, a structured entry is logged in the *corrections log* and rework is directed

#### cross-stage check

- is validation that current *stage artifacts* are consistent with prior stages (story graph valid, domain terms consistent, no active correction violated)
- is performed by the *delivery lead agent* during *exit gate* validation

#### slot chaining

- is the act of creating `slot-(NN+1)-start.md` after validating `slot-NN-finished.md`
- carries forward produced artifact paths, decisions, open questions, and filtered *corrections*

#### run summary

- is a structured entry the *delivery lead agent* writes to the *run log* when the last slot in a *run* completes
- contains: run number, stages completed, artifact quality summary, correction count by stage, sizing outcome
- triggers the adaptive sizing review — the *delivery lead agent* reads it alongside the *corrections log* to propose *run sizing policy* changes

#### run

- is a planned sequence of *stages* with defined scope, checkpoint policy, and rationale
- one *engagement* has one or more *runs*; a *run* may cover a subset of stages (e.g. Discovery → Prioritization in Run 1, Exploration → Engineering in Run 2)
- dimensions: stages (which, in order), scope (stories/slices/epics), checkpoint policy (within team member / across stages / across runs), rationale (concrete outcome when run completes)
- defined in the *agile delivery plan*, tracked in the *delivery plan checklist*

#### stage

- is one phase of delivery work within a *run*; defined by `stages/<stage>.md` with entry conditions, *exit gate*, team role, and *practice skill*
- six stages exist in the default pipeline: discovery → prioritization → exploration → scenarios → acceptance-tests → engineering
- plans are not required to run all six — *runs* pick subsets based on risk and scope
- each stage maps to one *team role* and one primary *practice skill*

#### plan changelog

- is `<workspace>/agile-delivery-plan.changelog.md`; append-only record of plan revisions written by the *delivery lead agent* after each *run* (Step 7)

#### delivery plan checklist

- is `<workspace>/abd-delivery-lead/progress/delivery-plan-checklist.md`; generated by *track_task*, tracks stage completion with markdown checkboxes, preserves `[x]` state across regenerations

#### strategy

- is a strategy file under `abd-delivery-planning/strategies/` matching the engagement's risk profile
- 9 strategies exist: bug-fix, legacy-migration, new-initiative variants (business-UX-risk, no-documented-architecture, proprietary-tech-risk), new-thin-slice, new-user-story, regulatory-compliance, spike-poc
- the *delivery lead agent* reads `strategies/README.md` then the matching file(s) during plan creation (Step 2)

#### abd-delivery-planning *(boundary)*

- is a skill owned by the delivery planning module; the *delivery lead agent* depends on it for plan mechanics (context analysis, risk classification, strategies, run design)

#### abd-delivery-war-room *(boundary)*

- is a skill providing war room protocol, `INSTRUCTIONS.md` template, and slot file templates; lives at `skills/delivery/abd-delivery-war-room/`
- the *delivery lead agent* depends on it when creating and populating the *war room*

#### track_task *(boundary)*

- is a skill that creates and maintains the *delivery plan checklist* — the *delivery lead agent* depends on it for checkbox progress tracking

#### execute-skill-using-skills-rules *(boundary)*

- is a skill providing `run_scanners.py` and the corrections logging process; used by both the *delivery lead agent* (gate validation, plan scanners) and the *team member agent* (artifact validation)

#### Decisions made

- *Delivery lead agent* is a concept — it has distinct identity, complex behavior (plan, author, validate, chain, adapt), and interactions with every other concept in the system.
- *Exit gate*, *cross-stage check*, *slot chaining* are concepts — each has distinct behavior triggered by specific events.
- *Run* is a concept — it has dimensions (stages, scope, checkpoint policy, rationale) and state (planned → in-progress → complete).
- *Run summary* is a concept — it is a structured entry in the run log that triggers the adaptive sizing review.
- *Stage* is a concept — it has entry conditions, exit gate, team role, practice skill, and outputs.
- *Plan changelog*, *delivery plan checklist*, *strategy* are concepts — each is a named artifact with a defined lifecycle.
- *abd-delivery-planning*, *abd-delivery-war-room*, *track_task*, *execute-skill-using-skills-rules* are boundary — this scope uses them but does not own their internals.

#### References

**Ref — Delivery lead AGENT.md**
Source: agents/abd-delivery-lead/AGENT.md
Locator: Steps 1–8
Extract: whole

---

### Team Member Agent

*Team Member Agent* is the executor. It runs inside one *slot*, reads the assigned *practice skills*, produces *stage artifacts*, validates with *scanners*, and writes the *finished file* when done — or the *blocked file* when stuck. It never plans, never chains *slots*, and never validates *exit gates*. Its scope is exactly what the *slot start file* says.

#### team member agent

- reads `abd-team-member/AGENT.md` and the role file under `roles/<role>.md` on bootstrap
- syncs with existing workspace artifacts (checks for conflicts with prior stages)
- reads each *practice skill* SKILL.md and all `rules/*.md` before generating any output
- reads the *corrections log* filtered by `Affects` for the current stage and run scope
- produces draft *stage artifacts* using skill templates to the *engagement workspace*
- self-reviews drafts against loaded skill rules before presenting
- presents drafts at a mid-slot *checkpoint* with summary and unknowns; *operator* confirms or corrects
- updates *story-graph.json* via *story-graph-ops* for stages that produce graph content
- runs *scanners* for each *practice skill* after producing an artifact; fixes failures before proceeding
- verifies stage outcomes match the *role playbook* definition of "what good looks like"
- writes the *finished file* when all *scanners* pass, listing artifact paths and scanner confirmation
- writes the *blocked file* when an *early question trigger* fires or it cannot proceed
- **Invariant:** never marks a *slot* finished while any listed *practice skill* has failing *scanners*
- **Invariant:** never guesses past an *early question trigger* — stops and writes *blocked file*

#### bootstrap prompt

- is assembled from the *slot start file* content + `abd-team-member/AGENT.md` + `delivery-war-room/INSTRUCTIONS.md`
- is the complete context for the *team member agent* — no prior chat or session is needed

#### team role

- is one of Product Owner, Analyst, or Engineer; determines which *role playbook* and *practice skills* the agent uses
- assigned by the *delivery lead agent* in the *slot start file* based on the *stage* definition
- each *stage* maps to exactly one *team role*: discovery/prioritization → Product Owner, exploration/scenarios → Analyst, acceptance-tests/engineering → Engineer

#### role playbook

- is `agents/abd-team-member/roles/<role>.md`; defines persona, goals, and "what good looks like" per delivery phase for each *team role*
- three exist: `product-owner.md`, `analyst.md`, `engineer.md`
- read by the *team member agent* at bootstrap (Step 1) to set context for the session

#### reviewer

- is a *team member agent* with `team-role: reviewer` that validates prior slot output against *exit gates* and *scanners*
- does not produce new *stage artifacts* — only validates existing ones
- uses the same `AGENT.md` and *war room* protocol; distinguished only by role in the *slot start file*
- assigned by the *delivery lead agent* optionally after an executor slot

#### early question trigger

- is a named condition in the *slot start file* (e.g. "domain-relationship-uncertain") that forces the *team member agent* to stop at the current stage and write a *blocked file* instead of guessing
- is authored by the *delivery lead agent* based on recurring error patterns in the *corrections log*

#### story-graph.json *(boundary)*

- is the structured graph of epics, stories, AC, and scenarios maintained by *story-graph-ops*; updated by the *team member agent* at each stage, validated by the *delivery lead agent* at gates

#### story-graph-ops *(boundary)*

- is the CLI and Python module for creating, reading, updating, and validating *story-graph.json*; lives at `skills/story-driven-delivery/story-graph-ops/`
- the *team member agent* uses it to update the graph at each stage; the *delivery lead agent* uses `story_graph_cli.py read` for *cross-stage checks*

#### practice skill *(boundary)*

- is an ABD skill (e.g. *abd-story-mapping*, *abd-acceptance-criteria*, *abd-ubiquitous-language*) that produces a *stage artifact*; the *team member agent* depends on it for artifact generation and validation rules

#### scanner *(boundary)*

- is `run_scanners.py` that validates *stage artifacts* against skill rules; the *team member agent* depends on it for artifact quality checks

#### stage artifact *(boundary)*

- is a file produced by a *practice skill* (e.g. `story-graph.json`, `acceptance-criteria.md`, `ubiquitous-language.md`); owned by the engagement, consumed by downstream stages

#### corrections log *(boundary)*

- is `docs/corrections-log.md`; owned by the correction process, consumed by both the *delivery lead agent* and the *team member agent* via the `Affects` filter

#### Decisions made

- *Team member agent* is a concept — it has distinct identity (one per slot), behavior (read skills, produce artifacts, validate, block/finish), and constraints (never plans, never chains).
- *Team role* is a concept — it determines the agent's persona, goals, and practice skills; assigned per stage.
- *Role playbook* is a concept — it defines per-role behavior expectations; read at bootstrap.
- *Reviewer* is a concept — it has distinct behavior (validate only, no new artifacts) and assignment rules (delivery lead decides).
- *Bootstrap prompt* is a concept — it is assembled from multiple sources and is the complete context for the agent.
- *Early question trigger* is a concept — it has distinct behavior (force stop) and is authored by the *delivery lead agent* based on error patterns.
- *Story-graph.json*, *story-graph-ops*, *practice skill*, *scanner*, *stage artifact*, *corrections log* are boundary — this scope uses them but does not own their internals.

#### References

**Ref — Team member AGENT.md**
Source: agents/abd-team-member/AGENT.md
Locator: Steps 1–8
Extract: whole

**Ref — Team member roles**
Source: agents/abd-team-member/roles/
Locator: product-owner.md, analyst.md, engineer.md, team-roles.md
Extract: whole

---

### Adaptive Run Sizing

*Adaptive Run Sizing* governs how big runs are, how tight checkpoints are, and how much freedom the *delivery lead agent* has — both at initial planning and after each run completes. The **initial** sizing comes from risk classification in *abd-delivery-planning*: the *delivery lead agent* reads context, classifies risks (value, technical, delivery, domain, integration, AI-model), picks a strategy, and designs runs whose scope, stage count, and checkpoint density match the risk profile. The **ongoing** adaptation reads the *corrections log* and *run log* after each run, counts error patterns by stage, and adjusts the *run sizing policy*. The *CLI harness* enforces whatever sizing the *delivery lead agent* sets — checkpoint frequency, notification content, and stall timeout all vary with the current policy.

#### adaptive run sizing

- has two phases: **initial sizing** (from risk classification) and **ongoing adaptation** (from corrections)
- **initial sizing:** the *delivery lead agent* reads context via *abd-delivery-planning*, classifies risks using the six risk types (value, technical, delivery, domain, integration, AI-model), selects a strategy from `strategies/*.md`, and designs runs with scope, stages, and checkpoint density that match the risk profile
- **ongoing adaptation:** after each *run* completes, the *delivery lead agent* reads the *corrections log* entries tagged by stage for the completed run, compares the *error rate* to prior runs in the *run log*, and proposes changes
- proposes changes to the *run sizing policy*: wider scope per *slot*, fewer *checkpoints*, or higher *autonomy level*
- adds *early question triggers* to future *slot start files* when recurring errors appear at late stages
- **Invariant:** initial sizing always precedes the first slot — the *delivery lead agent* does not author `slot-01-start.md` without a risk-informed plan

#### risk classification

- is performed by the *delivery lead agent* during plan creation using *abd-delivery-planning*
- classifies engagement context against six risk types: *value risk* (wrong thing), *technical risk* (wrong tech), *delivery risk* (miss schedule/quality), *domain risk* (misunderstand rules), *integration risk* (external systems), *AI-model risk* (hallucination likely)
- each classified risk drives run ordering (riskiest first), checkpoint tightness (high risk → per-story within team member), and *early question trigger* placement
- is recorded in `agile-delivery-plan.md` as part of the context assessment
- **Invariant:** the plan must classify at least one risk type — a plan with no risk classification is not a plan

#### run sizing policy

- governs stories per *slot*, stages per *run*, and *checkpoint* frequency
- **initial state** is set by *risk classification*: high-risk engagements start with 1 stage per run, 1–2 stories per slot, checkpoints within team member; low-risk start wider
- has three adaptive phases: cold start (tight, per-story checkpoints), corrections declining (wider scope, per-run checkpoints), stable (multi-stage runs, on block only)
- **Invariant:** changes require *operator* approval when *autonomy level* is tight or moderate; only *full* autonomy allows lead to apply changes unilaterally

#### harness enforcement

- the *CLI harness* reads the *run sizing policy* from the *manifest* and enforces it mechanically
- **checkpoint frequency:** when policy is `after_every_slot`, the *CLI harness* pauses and notifies the *operator* after each slot completes; when `on_block_only`, it chains automatically
- **notification content:** high-risk slots include risk type and early question triggers in notifications; stable slots include only completion status
- **stall timeout:** high-risk slots use a shorter *stall timeout* (agent more likely to loop on unfamiliar domain); stable slots use the default from *harness configuration*
- the *CLI harness* does not determine sizing — it reads and enforces what the *delivery lead agent* writes to the *manifest*

#### error rate

- is the frequency of *correction* entries per stage across recent *slots*
- is computed from the *corrections log* filtered by the current engagement's runs

#### autonomy escalation

- is the progression from tight → moderate → full as the *error rate* drops across runs
- is proposed by the *delivery lead agent* and approved by the *operator* (unless *autonomy level* is already full)

#### Decisions made

- *Adaptive run sizing* is a concept with two distinct phases (initial from risk, ongoing from corrections) — both are behavioral and interact with the *delivery lead agent*, *corrections log*, and *operator*.
- *Risk classification* is a concept — it has its own procedure, six typed risk categories, and directly drives run ordering and checkpoint density. It is performed by the *delivery lead agent* using *abd-delivery-planning* (boundary).
- *Run sizing policy* is a concept — it has state (current phase), is set initially by *risk classification*, and adapted by error patterns.
- *Harness enforcement* is a concept — the *CLI harness* varies its behavior (checkpoint pauses, notification content, stall timeouts) based on the current policy. This is the connection point between delivery planning intelligence and harness execution.
- *Error rate* is a derived value computed from the *corrections log* — concept-worthy because it drives the adaptive loop.
- *Autonomy escalation* is a concept describing the progression — not a property, because it has its own trigger conditions and approval rules.

#### References

**Ref — Contract adaptive sizing**
Source: docs/cli-delivery-harness-contract.md
Locator: Section 6 — Adaptive run sizing
Extract: whole

---

## Boundary Domain

### Boundary — Module: CLI Delivery Harness

> Boundary concepts consumed by the CLI Delivery Harness. These are the agents and skills the harness launches, monitors, and reads output from — but does not own.

---

### Delivery Lead Agent Definition

Owned by: agents/abd-delivery-lead

- is `agents/abd-delivery-lead/AGENT.md`; **exists** — defines the orchestration workflow (Steps 1–8), bootstrap inputs, checkpoint protocol, and correction carry-forward
- the *delivery lead agent* in the Core Domain executes this definition; the harness launches it and reads its war room outputs

#### Decisions made

- Boundary to Harness module: the harness launches and monitors the delivery lead but does not own its orchestration logic.

#### References

**Ref — Delivery lead AGENT.md**
Source: agents/abd-delivery-lead/AGENT.md
Locator: Steps 1–8
Extract: whole

---

### Team Member Agent Definition

Owned by: agents/abd-team-member

- is `agents/abd-team-member/AGENT.md`; **exists** — defines bootstrap from war room, role resolution, skill execution, scanner validation, and finished/blocked file authoring
- has role definitions under `agents/abd-team-member/roles/`: analyst, engineer, product-owner — each scopes which *practice skills* the agent uses
- the harness assembles the *bootstrap prompt* and launches team member agents; it reads finished/blocked files as outputs

#### Decisions made

- Boundary to Harness module: the harness launches team members and reads their slot files; does not own their execution logic.

#### References

**Ref — Team member AGENT.md**
Source: agents/abd-team-member/AGENT.md
Locator: whole
Extract: whole

---

### Boundary — Module: Lead Delivery Through Agents

> Boundary concepts consumed by the Lead Delivery module. These are the skills, correction process, stage definitions, and reviewer role the agents depend on.

---

### Practice Skill

Owned by: agilebydesign-skills

- is an ABD skill (e.g. *abd-story-mapping*, *abd-acceptance-criteria*) that produces *stage artifacts* and carries `rules/*.md` and `scanners/` for validation
- is read by the *team member agent* before generating output; skill order comes from the *slot start file*

#### Decisions made

- Boundary: this scope depends on *practice skills* for artifact generation and validation, but does not own their definitions or rules.

#### References

**Ref — Execute skill using skills rules**
Source: skills/execute-skill-using-skills-rules/SKILL.md
Locator: whole
Extract: whole

---

### Corrections Log

Owned by: correct_output

- is `docs/corrections-log.md`; structured entries with DO/DO NOT, Example wrong/correct, `Affects` tags
- is written by both the *delivery lead agent* (gate failures) and the *team member agent* (output errors)
- is read by the *delivery lead agent* for *adaptive run sizing* and by the *team member agent* for correction carry-forward

#### Decisions made

- Boundary: the correction process owns the log format and workflow; this scope consumes it as input to gates, carry-forward, and adaptive sizing.

#### References

**Ref — Correction process**
Source: skills/correct_output/SKILL.md
Locator: Instructions
Extract: whole

---

### Stage Definition

Owned by: abd-delivery-lead/stages

- is `stages/<stage>.md` in the delivery lead agent folder; defines entry conditions, *exit gate* items, team role, and practice skill for each stage
- is read by the *delivery lead agent* when opening a stage and validating *exit gates*

#### Decisions made

- Boundary: stage definitions are authored as part of the delivery lead agent, not the harness.

#### References

**Ref — Stage files**
Source: agents/abd-delivery-lead/stages/
Locator: discovery.md, exploration.md, etc.
Extract: whole

---

# Acceptance Criteria — Actor Interactions

Stories describing every interaction between humans, agents, skills, disk artifacts, and notification surfaces. Each story names **who** acts, **what** they read or write, **which** skill or tool is involved, and **who** sees the result.

The story map is one integrated epic. Stories are interleaved in the natural sequence an engagement follows — each story is tagged with the module it primarily belongs to.

| Module | Status | Stories |
|---|---|---|
| **CLI Delivery Harness** | NEW | Configure and Bootstrap Engagement, Launch Slot Execution, Block and Resume on Human Input, Recover from Agent Stall, Check In on Progress, Resume After Session Kill |
| **Lead Delivery Through Agents** | EXISTS / EXTENDING | Kick Off Engagement, Set Up War Room, Execute Stage Work in Slot, Complete and Validate Slot, Review Slot Output, Chain to Next Slot, Adapt Run Sizing from Corrections, Complete Plan |

---

## Story: Configure and Bootstrap Engagement

**Epic:** CLI Delivery Harness · **Story type:** user

### Domain terms

- *Operator* — human who sets up and governs an engagement
- *Harness Configuration* — one-time CLI harness setup: API key, agent mode (local / cloud), repo URL (cloud), model, default stall timeout, notification channel, permissions, sandbox, MCP allowlist; stored at `cli_harness/cli-config.json` or `~/.cursor/cli-config.json`
- *Agent Mode* — execution target for launched agents: `local` (operator's machine) or `cloud` (Cursor-hosted VM via Cloud Agents API)
- *Engagement Parameters* — the full input set: workspace path, context brief, profile, autonomy level, notification channel, stall timeout override, start/end stage, MCP tools
- *Engagement Workspace* — absolute path to the root folder for all engagement artifacts
- *CLI Harness* — outer process that reads configuration, validates parameters, and scaffolds the workspace
- *Delivery Lead Agent* — agent that receives the validated parameters and builds the plan

### Acceptance criteria

1. **WHEN** the *Operator* runs the *CLI Harness* for the first time on a machine
   **THEN** the *CLI Harness* reads `cli_harness/cli-config.json` (or `~/.cursor/cli-config.json`) for API key, *Agent Mode*, repo URL, model, default stall timeout, notification channel, permissions allowlist, and sandbox mode
   **AND** if the API key is missing or invalid, the *CLI Harness* reports the error and stops
   **AND** if *Agent Mode* is `cloud` and repo URL is not set, the *CLI Harness* reports the error and stops
   **BUT** the *CLI Harness* does not guess defaults for security-sensitive settings (API key, permissions)

2. **WHEN** the *Operator* starts a new engagement without specifying all *Engagement Parameters*
   **THEN** the *CLI Harness* prompts the *Operator* interactively for each missing required parameter in turn: *Engagement Workspace* path, *Context Brief* (path to documents or inline description), *Profile* (greenfield / brownfield / small-build / feature / bespoke), *Autonomy Level* (tight / moderate / full)
   **AND** for each optional parameter (notification channel, stall timeout, MCP tools, start/end stage), the *CLI Harness* offers the default from *Harness Configuration* and asks the *Operator* to accept or override
   **AND** the *CLI Harness* validates the *Engagement Workspace* path exists and is writable before proceeding
   **BUT** the *CLI Harness* never guesses a required parameter — it always asks; skipping a prompt is not allowed for workspace, context, profile, or autonomy

3. **WHEN** all *Engagement Parameters* are validated
   **THEN** the *CLI Harness* creates the workspace folder structure if it does not exist: `delivery-war-room/`, `docs/`, `abd-delivery-lead/progress/`
   **AND** the *CLI Harness* initializes `delivery-war-room/run-log.jsonl` (empty, append-only)
   **AND** the *CLI Harness* writes a `harness-config.json` snapshot to `delivery-war-room/` recording the merged parameters for this engagement (so resume does not need the operator to re-specify)
   **AND** the *CLI Harness* launches the *Delivery Lead Agent* with the *Engagement Parameters* as the initial prompt
   **BUT** the *CLI Harness* does not write `manifest.md`, `INSTRUCTIONS.md`, or `slot-NN-start.md` — those are the *Delivery Lead Agent's* job

4. **WHEN** the *Operator* resumes an existing engagement (workspace already has `delivery-war-room/`)
   **THEN** the *CLI Harness* reads `delivery-war-room/harness-config.json` for the engagement's merged parameters
   **AND** the *CLI Harness* does not ask the *Operator* to re-specify workspace, profile, autonomy, or notification settings
   **BUT** the *Operator* can override any parameter on resume if they choose

   **Evidence:** Contract goals — resume without re-brief; disk is source of truth.

---

## Story: Kick Off Engagement

**Epic:** Lead Delivery Through Agents · **Story type:** user

### Domain terms

- *Operator* — human who initiates and governs an engagement
- *Delivery Lead Agent* — agent that orchestrates runs, slots, and gates
- *Engagement Workspace* — absolute path to the root folder for all engagement artifacts
- *Agile Delivery Plan* — narrative plan document at `<workspace>/agile-delivery-plan.md`
- *Risk Classification* — assessment of engagement context against six risk types: value, technical, delivery, domain, integration, AI-model
- *Strategy* — a file under `abd-delivery-planning/strategies/` matching the engagement's risk profile (9 exist)
- *Run* — a planned sequence of stages with defined scope, checkpoint policy, and rationale
- *Stage* — one phase of delivery work defined by `stages/<stage>.md` with entry conditions, exit gate, team role, and practice skill
- *Delivery Plan Checklist* — `abd-delivery-lead/progress/delivery-plan-checklist.md`; plan progress checkboxes
- *abd-delivery-planning* — skill that builds, documents, and revises the *Agile Delivery Plan*
- *execute-skill-using-skills-rules* — skill providing scanner execution and corrections logging
- *track_task* — skill that creates and maintains the *Delivery Plan Checklist*
- *CHECKPOINT* — mandatory stop where the *Delivery Lead Agent* presents output and waits for *Operator* approval

### Acceptance criteria

1. **WHEN** the *CLI Harness* launches the *Delivery Lead Agent* with *Engagement Parameters*
   **THEN** the *Delivery Lead Agent* confirms the *Engagement Workspace* path and inventories existing artifacts
   **AND** the *Delivery Lead Agent* creates `abd-delivery-lead/progress/` and generates an initial *Delivery Plan Checklist* using *track_task*
   **AND** the *Delivery Lead Agent* reads `abd-delivery-planning` SKILL.md, `strategies/README.md`, and matching *Strategy* files
   **AND** the *Delivery Lead Agent* reads any existing `agile-delivery-plan.md` and `docs/corrections-log.md` in the *Engagement Workspace*

2. **WHEN** the *Delivery Lead Agent* has read context and strategies
   **THEN** the *Delivery Lead Agent* assesses the engagement context against the six risk types (*Risk Classification*)
   **AND** the *Delivery Lead Agent* selects the *Strategy* that matches the risk profile
   **AND** the *Delivery Lead Agent* designs *Runs* with *Stages*, scope, and checkpoint policy
   **AND** the *Delivery Lead Agent* writes `agile-delivery-plan.md` to *Engagement Workspace* root
   **AND** the *Delivery Lead Agent* regenerates the *Delivery Plan Checklist* using *track_task*
   **AND** the *Delivery Lead Agent* runs plan-shape scanners using *execute-skill-using-skills-rules*
   **BUT** the *Delivery Lead Agent* does not advance past *CHECKPOINT* until the *Operator* approves the plan

3. **WHEN** the *Operator* tells the *Delivery Lead Agent* to use specific runs (overriding the plan)
   **THEN** the *Delivery Lead Agent* documents the *Operator*-specified runs in the *Agile Delivery Plan*
   **AND** the *Delivery Lead Agent* updates the plan to reflect the override
   **BUT** the *Delivery Lead Agent* records the override rationale so the audit trail is honest

   **Evidence:** Story map — Establish Workspace and Build Plan (Steps 1–2); AGENT.md Steps 1–2.

---

## Story: Launch Slot Execution

**Epic:** CLI Delivery Harness · **Story type:** system

### Domain terms

- *CLI Harness* — outer process that launches agents, monitors heartbeats, and recovers from stalls
- *Slot* — a unit of delegated work with a defined lifecycle: PENDING → RUNNING → BLOCKED → FINISHED | FAILED
- *Slot Start File* — `delivery-war-room/slot-NN-start.md`; full bootstrap handoff for the *Team Member Agent*
- *Running File* — `delivery-war-room/slot-NN-running.json`; agent_id, run_id, started_at, last_heartbeat
- *Run Log* — `delivery-war-room/run-log.jsonl`; append-only audit trail
- *Team Member Agent* — agent that executes stage work inside one *Slot*
- *Active Slot* — smallest NN where *Slot Start File* exists and no `slot-NN-finished.md` exists
- *Bootstrap Prompt* — assembled from *Slot Start File* + `abd-team-member/AGENT.md` + `INSTRUCTIONS.md`

### Acceptance criteria

1. **WHEN** the *Delivery Lead Agent* opens a stage for a slot
   **THEN** the *Delivery Lead Agent* reads `stages/<stage>.md` for entry conditions and *Exit Gate* items
   **AND** the *Delivery Lead Agent* verifies entry conditions are met from prior stage artifacts
   **AND** the *Delivery Lead Agent* determines the team role and selects ordered *Practice Skills* from the stage definition
   **AND** the *Delivery Lead Agent* filters `docs/corrections-log.md` for stage-relevant entries
   **AND** the *Delivery Lead Agent* adds *Early Question Triggers* from corrections patterns
   **AND** the *Delivery Lead Agent* writes `slot-NN-start.md` with team-role, workspace, stage, run_scope, skills, filtered corrections, and early_questions

2. **WHEN** the *CLI Harness* detects a new *Slot Start File* in the *War Room*
   **THEN** the *CLI Harness* identifies the *Active Slot* (smallest NN with `slot-NN-start.md` present and `slot-NN-finished.md` absent)
   **AND** the *CLI Harness* assembles the *Bootstrap Prompt* from *Slot Start File* content + `agents/abd-team-member/AGENT.md` + `delivery-war-room/INSTRUCTIONS.md`
   **AND** the *CLI Harness* launches the *Team Member Agent* via Cursor SDK — using `LocalAgentOptions` when *Agent Mode* is `local`, or `CloudAgentOptions` (with *Repo URL*) when *Agent Mode* is `cloud`; falls back to CLI subprocess in local mode when the SDK is not installed
   **AND** the *CLI Harness* writes `slot-NN-running.json` with agent_id, run_id, mode (local/cloud), started_at, and initial heartbeat timestamp
   **AND** the *CLI Harness* appends a RUNNING entry to the *Run Log*
   **BUT** the *CLI Harness* does not launch a second agent if a *Running File* already exists with a fresh heartbeat

3. **WHEN** no *Active Slot* exists (all slots finished or no start files)
   **THEN** the *CLI Harness* reports "no pending work" and idles
   **BUT** the *CLI Harness* does not create slots — only the *Delivery Lead Agent* authors *Slot Start Files*

   **Evidence:** Story map — Open Stage and Launch Slot (Steps 3–4); AGENT.md Steps 3–4.

---

## Story: Execute Stage Work in Slot

**Epic:** Lead Delivery Through Agents · **Story type:** system

### Domain terms

- *Team Member Agent* — agent executing inside a *Slot*
- *Practice Skill* — ABD skill (e.g. *abd-story-mapping*, *abd-acceptance-criteria*, *abd-ubiquitous-language*) that produces a stage artifact
- *Stage Artifact* — file produced by a *Practice Skill* (e.g. `story-graph.json`, `acceptance-criteria.md`, `ubiquitous-language.md`)
- *Scanners* — `run_scanners.py` scripts that validate *Stage Artifacts* against skill rules
- *Corrections Log* — `docs/corrections-log.md`; mistakes logged with DO/DO NOT, tagged by Affects
- *Early Question Trigger* — condition named in *Slot Start File* that forces the *Team Member Agent* to stop and write a *Blocked File* instead of guessing

### Acceptance criteria

1. **WHEN** the *Team Member Agent* starts from the *Bootstrap Prompt*
   **THEN** the *Team Member Agent* reads `abd-team-member/AGENT.md` and the role file under `roles/<role>.md`
   **AND** the *Team Member Agent* syncs with existing workspace artifacts (checks for conflicts with prior work)
   **AND** the *Team Member Agent* reads the *Corrections Log* filtered by `Affects` for the current stage and run scope
   **AND** the *Team Member Agent* reads each *Practice Skill* listed in the *Slot Start File* (SKILL.md and all `rules/*.md`) before generating any output

2. **WHEN** the *Team Member Agent* produces a draft *Stage Artifact*
   **THEN** the *Team Member Agent* self-reviews the draft against the loaded rules before presenting
   **AND** the *Team Member Agent* presents the draft at a *CHECKPOINT* with a summary of what was produced and any unknowns
   **AND** the *Operator* confirms or corrects the draft
   **AND** if the *Operator* corrects, the *Team Member Agent* logs the correction to `docs/corrections-log.md` before fixing the artifact

3. **WHEN** the *Team Member Agent* has a confirmed draft
   **THEN** the *Team Member Agent* updates `story-graph.json` using *story-graph-ops* (for stages that produce graph content: discovery, prioritization, exploration, scenarios, acceptance-tests)
   **AND** the *Team Member Agent* runs *Scanners* for each *Practice Skill* against the produced artifacts
   **AND** if *Scanners* fail, the *Team Member Agent* fixes violations and re-runs until clean — or presents violations at a *CHECKPOINT* for human decision
   **BUT** the *Team Member Agent* does not mark the slot finished until all *Practice Skills* listed in the *Slot Start File* have passing *Scanners*

4. **WHEN** all *Scanners* pass
   **THEN** the *Team Member Agent* verifies stage outcomes match the *Role Playbook* definition of "what good looks like"
   **AND** the *Team Member Agent* writes `slot-NN-finished.md` listing all *Stage Artifact* paths, scanner pass confirmation, and timestamp

5. **WHEN** the *Team Member Agent* encounters an *Early Question Trigger* condition (e.g. uncertain domain relationship at UL/CRC stage)
   **THEN** the *Team Member Agent* writes `slot-NN-blocked.md` with the specific question, what it tried, and which artifact paths are relevant
   **BUT** the *Team Member Agent* does not guess past the trigger — it stops and waits for a human answer

6. **WHEN** the *Team Member Agent* produces output that contradicts a prior correction in the *Corrections Log*
   **THEN** the *Team Member Agent* re-reads the correction entry and regenerates the artifact
   **AND** the *Team Member Agent* appends a new Example (wrong) to the existing correction entry
   **BUT** no artifact is marked done while it violates an active correction

   **Evidence:** Story map — Execute Stage Work; AGENT.md Steps 1–8.

---

## Story: Block and Resume on Human Input

**Epic:** CLI Delivery Harness · **Story type:** user

### Domain terms

- *Blocked File* — `delivery-war-room/slot-NN-blocked.md`; question, context paths, reason for stop
- *Answer File* — `delivery-war-room/slot-NN-answer.md`; human-written response to unblock the agent
- *Notification* — message sent to *Operator* (and optionally *ABD Team Member*) via configured channel (email, Slack, webhook)

### Acceptance criteria

1. **WHEN** the *Team Member Agent* writes a *Blocked File* to `delivery-war-room/`
   **THEN** the *CLI Harness* detects the new *Blocked File*
   **AND** the *CLI Harness* sends a *Notification* to the *Operator* with the slot number, question text, and artifact paths from the *Blocked File*
   **AND** the *CLI Harness* updates `slot-NN-running.json` status to BLOCKED
   **AND** the *CLI Harness* appends a BLOCKED entry to the *Run Log*
   **BUT** the *CLI Harness* does not cancel the agent session — it idles awaiting the *Answer File*

2. **WHEN** the *Operator* writes an *Answer File* (`slot-NN-answer.md`) to `delivery-war-room/`
   **THEN** the *CLI Harness* detects the *Answer File*
   **AND** the *CLI Harness* resumes the *Team Member Agent* with the answer content (via `agent resume` or `Agent.resume(agent_id)` with the answer as the follow-up prompt)
   **AND** the *CLI Harness* updates `slot-NN-running.json` status back to RUNNING
   **AND** the *CLI Harness* appends a RESUMED entry to the *Run Log*

3. **WHEN** the *Operator* writes the *Answer File* from a different device (phone, another PC, GitHub web)
   **THEN** the *CLI Harness* detects and processes it identically — the file on disk is the interface, not the device
   **BUT** no agent session or IDE must be open on the answering device — only write access to the repo

   **Evidence:** Contract goals — check in from anywhere; answer when blocked.

---

## Story: Complete and Validate Slot

**Epic:** Lead Delivery Through Agents · **Story type:** system

### Domain terms

- *Finished File* — `delivery-war-room/slot-NN-finished.md`; artifact paths, stage-complete status, scanner results
- *Exit Gate* — conditions from `stages/<stage>.md` that must pass before the stage is considered complete
- *Cross-Stage Check* — validation that artifacts from this stage are consistent with prior stages (e.g. story graph still valid, domain terms consistent)
- *Sync-Upstream* — workspace rule that offers to propagate changes between artifact levels (code ↔ tests ↔ specs ↔ stories)

### Acceptance criteria

1. **WHEN** the *Team Member Agent* has all *Scanners* green for every *Practice Skill* in the *Slot*
   **THEN** the *Team Member Agent* writes `slot-NN-finished.md` listing all *Stage Artifact* paths, scanner pass confirmation, and timestamp
   **AND** the *Team Member Agent* notes any *Sync-Upstream* offers in the *Finished File*

2. **WHEN** the *CLI Harness* detects a new *Finished File*
   **THEN** the *CLI Harness* sends a completion *Notification* to the *Operator* with artifact summary and scanner pass/fail
   **AND** the *CLI Harness* signals the *Delivery Lead Agent* to validate gates

3. **WHEN** the *Delivery Lead Agent* reads the *Finished File*
   **THEN** the *Delivery Lead Agent* reads `stages/<stage>.md` for the *Exit Gate* conditions
   **AND** the *Delivery Lead Agent* verifies each *Exit Gate* item against the produced *Stage Artifacts*
   **AND** the *Delivery Lead Agent* runs *Cross-Stage Checks* (story graph valid via `story_graph_cli.py read`, domain terms consistent, no active correction violated)
   **AND** the *Delivery Lead Agent* runs *Practice Skill Scanners* on the team member's output using *execute-skill-using-skills-rules*

4. **WHEN** all *Exit Gate* conditions pass
   **THEN** the *Delivery Lead Agent* presents gate results at a *CHECKPOINT*
   **AND** the *Operator* approves the stage exit
   **AND** the *Delivery Lead Agent* checks off the stage line in the *Delivery Plan Checklist*

5. **WHEN** the *Delivery Lead Agent* detects a gate failure
   **THEN** the *Delivery Lead Agent* writes a structured entry in `docs/corrections-log.md` (DO/DO NOT, Example wrong, Affects tag)
   **AND** the *Delivery Lead Agent* presents the failure to the *Operator* at a *CHECKPOINT*
   **BUT** the *Delivery Lead Agent* does not open the next slot until the *Operator* confirms rework is complete or accepts the state

   **Evidence:** Story map — Validate Stage Exit (Step 5); AGENT.md Step 5.

---

## Story: Recover from Agent Stall

**Epic:** CLI Delivery Harness · **Story type:** system

### Domain terms

- *Heartbeat* — timestamp in `slot-NN-running.json` updated every 60 seconds by the *CLI Harness* while the agent streams output
- *Stall Timeout* — configurable duration (N minutes) after which a stale *Heartbeat* triggers recovery
- *Retry* — one automatic relaunch of the same *Slot* with the same *Bootstrap Prompt*

### Acceptance criteria

1. **WHEN** the *CLI Harness* detects that `slot-NN-running.json` heartbeat is older than the *Stall Timeout*
   **THEN** the *CLI Harness* cancels the stalled agent process
   **AND** the *CLI Harness* appends a STALLED entry to the *Run Log* with the agent_id and elapsed time
   **AND** the *CLI Harness* relaunches the *Slot* as a *Retry* (same *Bootstrap Prompt*, new agent_id)
   **AND** the *CLI Harness* updates `slot-NN-running.json` with the new agent_id and run_id

2. **WHEN** the *Retry* also stalls (second stall on the same slot)
   **THEN** the *CLI Harness* marks the slot FAILED in the *Run Log*
   **AND** the *CLI Harness* sends a *Notification* to the *Operator* with slot number, both agent_ids, and the failure reason
   **AND** the *CLI Harness* writes `slot-NN-blocked.md` describing the repeated stall so the *Operator* can investigate
   **BUT** the *CLI Harness* does not retry a third time — human intervention is required

   **Evidence:** Contract goals — stalls never go silent; recover or notify.

---

## Story: Chain to Next Slot

**Epic:** Lead Delivery Through Agents · **Story type:** system

### Domain terms

- *Slot Chaining* — the *Delivery Lead Agent* creating `slot-(NN+1)-start.md` after validating `slot-NN-finished.md`

### Acceptance criteria

1. **WHEN** the *Delivery Lead Agent* confirms all *Exit Gates* pass and the *Operator* approves the stage exit
   **THEN** the *Delivery Lead Agent* marks the stage done in the *Delivery Plan Checklist*
   **AND** the *Delivery Lead Agent* passes artifacts, decisions, and filtered corrections forward
   **AND** the *Delivery Lead Agent* appends a slot-completion event to `run-log.jsonl`
   **AND** the *Delivery Lead Agent* reads the *Manifest* for the next slot definition
   **AND** the *Delivery Lead Agent* authors the next `slot-(NN+1)-start.md` (loop back to Launch Slot Execution)
   **AND** the *CLI Harness* detects the new *Slot Start File* on its next loop iteration and launches the *Team Member Agent*

2. **WHEN** the *Manifest* checkpoint_policy is `after_every_slot`
   **THEN** the *Delivery Lead Agent* presents a *CHECKPOINT* to the *Operator* before writing the next *Slot Start File*
   **BUT** when checkpoint_policy is `on_block_only`, the *Delivery Lead Agent* chains automatically without *Operator* pause

3. **WHEN** the current slot is the last slot in a *Run*
   **THEN** the *Delivery Lead Agent* proceeds to Complete Run and Adapt Sizing (see Adapt Run Sizing from Corrections story)

   **Evidence:** Story map — Hand Off and Chain to Next Stage (Step 6); AGENT.md Step 6.

---

## Story: Check In on Progress

**Epic:** CLI Delivery Harness · **Story type:** user

### Domain terms

- *ABD Team Member* — human team member (not the agent) who checks in on engagement progress
- *Progress View* — the set of war room files any human can read from any device to understand engagement status

### Acceptance criteria

1. **WHEN** the *Operator* or *ABD Team Member* opens the repo from any device (phone, laptop, GitHub web)
   **THEN** they can read `manifest.md` to see the goal, profile, slots, and which slot is active
   **AND** they can read `abd-delivery-lead/progress/delivery-plan-checklist.md` to see which stages and runs are checked off
   **AND** they can read `run-log.jsonl` to see every agent launch, block, resume, stall, and completion with timestamps and agent_ids
   **AND** they can read `slot-NN-finished.md` to see which artifacts were produced and whether scanners passed
   **AND** they can read `slot-NN-blocked.md` (if present) to see what question the agent is stuck on
   **AND** they can read any *Stage Artifact* linked in a *Finished File* to review the actual output
   **BUT** no open Cursor session, IDE, or CLI is required — the repo on disk (or on GitHub) is the entire interface

2. **WHEN** the *Operator* wants to see live progress on a running slot
   **THEN** the *Operator* reads `slot-NN-running.json` for agent_id, run_id, started_at, and last_heartbeat
   **AND** the *Operator* reads the *Slot Start File* for current stage, skills, and run scope
   **AND** the *Operator* can tail `run-log.jsonl` for the latest entries from that agent_id

3. **WHEN** the *Operator* wants a one-line engagement status summary
   **THEN** the *CLI Harness* provides a `status` command reading `manifest.md`, active slot, checklist progress, and last log entry

   **Evidence:** Story map — Check In on Progress; Contract goals — check in from anywhere.

---

## Story: Resume After Session Kill

**Epic:** CLI Delivery Harness · **Story type:** user

### Domain terms

- *Session Kill* — the *Operator* closing the terminal, restarting the machine, or losing connectivity mid-slot
- *War Room State* — the collection of files in `delivery-war-room/` that fully describe where the engagement is

### Acceptance criteria

1. **WHEN** the *Operator* restarts the *CLI Harness* after a *Session Kill*
   **THEN** the *CLI Harness* reads `delivery-war-room/manifest.md` and scans for the *Active Slot*
   **AND** if `slot-NN-running.json` exists with a stale heartbeat, the *CLI Harness* follows the stall recovery flow (cancel, retry once, or fail + notify)
   **AND** if `slot-NN-blocked.md` exists without a corresponding `slot-NN-answer.md`, the *CLI Harness* sends a *Notification* and waits
   **AND** if `slot-NN-finished.md` exists without gates validated, the *CLI Harness* launches the *Delivery Lead Agent* to validate gates and chain the next slot
   **BUT** the *CLI Harness* never asks the *Operator* to re-explain context — the *War Room State* is the complete brief

2. **WHEN** the *CLI Harness* needs to resume the *Delivery Lead Agent* after a kill
   **THEN** the *CLI Harness* launches a fresh *Delivery Lead Agent* session
   **AND** the *Delivery Lead Agent* reads the *Manifest*, *Run Log*, *Delivery Plan Checklist*, and *Agile Delivery Plan*
   **AND** the *Delivery Lead Agent* determines where to resume based on the slot state (last finished, running, or blocked)
   **AND** the *Delivery Lead Agent* does not re-run stages or slots already marked complete in the checklist
   **BUT** the *Delivery Lead Agent* re-validates the last *Finished File* if gates were not yet checked off

3. **WHEN** the *Operator* resumes from a different machine
   **THEN** the same behavior applies — the *War Room State* in the shared repo is device-independent
   **AND** if *Agent Mode* is `cloud`, the *CLI Harness* resumes the *Cloud Agent* by its `bc-`-prefixed agent_id via `Agent.resume()` — no stall, no relaunch
   **BUT** if *Agent Mode* is `local`, agent_ids from a prior machine's CLI session are not resumable; the *CLI Harness* treats a stale *Running File* from another machine as a stall and follows recovery

   **Evidence:** Story map — Resume After Session Kill; Contract goals — kill session, resume days later without re-brief.

---

## Story: Adapt Run Sizing from Corrections

**Epic:** Lead Delivery Through Agents · **Story type:** user

### Domain terms

- *Error Rate* — frequency of correction entries per stage across recent slots
- *Run Sizing Policy* — rules governing how many stories per slot, how many stages per run, and checkpoint frequency
- *Autonomy Escalation* — moving from tight → moderate → full as the *Error Rate* drops
- *Plan Changelog* — `agile-delivery-plan.changelog.md`; append-only record of plan revisions after each run

### Acceptance criteria

1. **WHEN** the last slot in a *Run* is complete and gates pass
   **THEN** the *Delivery Lead Agent* summarizes run results and artifact quality
   **AND** the *Delivery Lead Agent* reads *Corrections Log* entries tagged by stage for the completed run
   **AND** the *Delivery Lead Agent* computes the *Error Rate* across completed slots
   **AND** the *Delivery Lead Agent* compares the *Error Rate* to prior runs in the *Run Log*
   **AND** the *Delivery Lead Agent* appends a run revision to the *Plan Changelog*
   **AND** the *Delivery Lead Agent* regenerates the *Delivery Plan Checklist* preserving completed `[x]` marks

2. **WHEN** corrections are declining across runs
   **THEN** the *Delivery Lead Agent* proposes wider scope per slot and fewer checkpoints for the next run
   **AND** the *Delivery Lead Agent* proposes *Autonomy Escalation* if the *Error Rate* trend supports it
   **AND** the *Delivery Lead Agent* records the *Run Sizing Policy* change proposal in the *Agile Delivery Plan*

3. **WHEN** corrections show a recurring error class at a late stage (e.g. domain confusion at spec or code stage)
   **THEN** the *Delivery Lead Agent* adds an *Early Question Trigger* for that error class at an earlier stage (e.g. UL/CRC) in the next run's *Manifest* slot definitions
   **AND** the *Delivery Lead Agent* logs the pattern in `docs/corrections-log.md` with a forward-looking DO entry

4. **WHEN** the *Operator* approves the run summary and sizing changes
   **THEN** the *Delivery Lead Agent* writes the updated *Run Sizing Policy* to the *Manifest*
   **AND** the *CLI Harness* reads the updated policy from the *Manifest*
   **AND** the *CLI Harness* adjusts checkpoint frequency, stall timeout, and notification content for subsequent slots

5. **WHEN** the *Autonomy Level* is `tight` or `moderate`
   **THEN** all *Run Sizing Policy* changes are presented to the *Operator* at a *CHECKPOINT* before taking effect
   **BUT** when *Autonomy Level* is `full`, the *Delivery Lead Agent* applies changes and notifies the *Operator* after the fact

   **Evidence:** Story map — Complete Run and Adapt Sizing (Step 7); AGENT.md Step 7.

---

## Story: Set Up War Room

**Epic:** Lead Delivery Through Agents · **Story type:** system

### Domain terms

- *War Room* — the `delivery-war-room/` folder; disk-based source of truth for slot state, blockers, and audit
- *Manifest* — `manifest.md`; goal, profile, autonomy level, checkpoint policy, ordered slot definitions
- *INSTRUCTIONS.md* — verbatim protocol the team member agent reads on autostart
- *Run Log* — `run-log.jsonl`; append-only audit trail
- *Run Sizing Policy* — rules governing scope per slot, stages per run, checkpoint frequency
- *abd-delivery-war-room* — skill providing war room templates and slot file protocol

### Acceptance criteria

1. **WHEN** the *Operator* approves the *Agile Delivery Plan* at the Step 2 *CHECKPOINT*
   **THEN** the *Delivery Lead Agent* creates `delivery-war-room/` in the *Engagement Workspace*
   **AND** the *Delivery Lead Agent* writes `INSTRUCTIONS.md` from the *abd-delivery-war-room* template
   **AND** the *Delivery Lead Agent* writes `manifest.md` with goal, *Profile*, *Autonomy Level*, checkpoint policy, and ordered slot definitions
   **AND** the *Delivery Lead Agent* writes `profile.md` summarizing the *Profile* rationale
   **AND** the *Delivery Lead Agent* initializes `run-log.jsonl`
   **BUT** the *Delivery Lead Agent* does not write `slot-01-start.md` until the war room structure is complete

2. **WHEN** the *Delivery Lead Agent* sets up the *War Room*
   **THEN** the *Delivery Lead Agent* writes the initial *Run Sizing Policy* to the *Manifest* based on the *Risk Classification* from the plan
   **AND** the *CLI Harness* can read the *Manifest* to determine checkpoint frequency, stall timeout, and notification content for the first slot

3. **WHEN** the *Engagement Workspace* already contains `delivery-war-room/` (resumed engagement)
   **THEN** the *Delivery Lead Agent* reads the existing *Manifest* and *Run Log*
   **AND** the *Delivery Lead Agent* does not overwrite existing war room files
   **BUT** the *Delivery Lead Agent* may update the *Manifest* if the plan was revised

   **Evidence:** Story map — Set Up War Room sub-epic; delivery lead creates the folder, not the harness.

---

## Story: Review Slot Output

**Epic:** Lead Delivery Through Agents · **Story type:** system

### Domain terms

- *Reviewer* — a *Team Member Agent* with `team-role: reviewer` that validates prior slot output
- *Reviewer Finished File* — `slot-NN-finished.md` written by the reviewer with gate pass/fail and findings

### Acceptance criteria

1. **WHEN** the *Delivery Lead Agent* decides independent validation is needed before gate sign-off
   **THEN** the *Delivery Lead Agent* authors a *Slot Start File* with `team-role: reviewer` and a scope limited to the prior slot's output artifacts
   **AND** the *CLI Harness* launches the *Reviewer* agent

2. **WHEN** the *Reviewer* is launched
   **THEN** the *Reviewer* reads the prior slot's *Finished File* and all artifact paths listed in it
   **AND** the *Reviewer* validates artifacts against the *Exit Gate* conditions from `stages/<stage>.md`
   **AND** the *Reviewer* runs *Scanners* using *execute-skill-using-skills-rules*
   **AND** the *Reviewer* writes a *Reviewer Finished File* with findings
   **BUT** the *Reviewer* does not produce new *Stage Artifacts* — only validates existing ones

3. **WHEN** the *Delivery Lead Agent* reads the *Reviewer Finished File*
   **THEN** the *Delivery Lead Agent* incorporates findings into the *Exit Gate* decision
   **AND** if the reviewer found failures, the *Delivery Lead Agent* logs corrections and may re-author the executor slot for rework

   **Evidence:** Story map — Review Slot Output sub-epic; reviewer is optional, assigned by delivery lead.

---

## Story: Complete Plan

**Epic:** Lead Delivery Through Agents · **Story type:** user

### Domain terms

- *Delivery Plan Checklist* — `abd-delivery-lead/progress/delivery-plan-checklist.md`; tracks stage completion
- *Strategy* — a strategy file under `abd-delivery-planning/strategies/` matching the engagement's risk profile

### Acceptance criteria

1. **WHEN** all runs in the *Agile Delivery Plan* are complete
   **THEN** the *Delivery Lead Agent* presents a final summary of all runs, artifact quality, and corrections patterns at a *CHECKPOINT*
   **AND** the *Delivery Lead Agent* closes the *Delivery Plan Checklist* (all items `[x]`)

2. **WHEN** the engagement revealed a novel pattern not covered by existing strategies
   **THEN** the *Delivery Lead Agent* proposes a new *Strategy* file for `abd-delivery-planning/strategies/`
   **AND** the *Operator* approves or rejects the new strategy

3. **WHEN** the *Operator* approves plan completion
   **THEN** the *Delivery Lead Agent* appends a final entry to the *Plan Changelog*
   **AND** the *Delivery Lead Agent* appends a plan-complete event to the *Run Log*

   **Evidence:** Story map — Complete Plan sub-epic; Delivery Lead Step 8.

---

# Technical Contract

The sections below define the mechanical specifications that implement the behaviors described in the Acceptance Criteria and Ubiquitous Language above.

---

## Separation of concerns

| Layer | Owns | Does NOT own |
|-------|------|--------------|
| **Delivery lead agent + abd-delivery-planning** | Risk classification, strategy selection, run design, slot authoring (entry-condition verification, role/skill selection), gate validation (exit gates + cross-stage checks + scanners via execute-skill-using-skills-rules), slot chaining, adaptive run sizing, plan changelog, run summary | Process spawning, stall recovery, heartbeat |
| **War room (disk)** | Source of truth for slot state, artifacts, blockers, audit, run sizing policy (in manifest) | Execution, planning logic |
| **Team member agent** | Stage work inside one slot: self-review → mid-slot checkpoint → story-graph-ops update → scanners → role-playbook outcome check → finished/blocked | Orchestration, next slot, gate validation |
| **CLI harness** | Launch slot, heartbeat, stall → retry/notify, resume after session kill, notification on finished/blocked/stall, read run sizing policy from manifest to adjust enforcement, status command | Planning, skill content, gate validation |

---

## War room layout

```text
<workspace>/delivery-war-room/
  INSTRUCTIONS.md
  manifest.md              # runs, slots, profile, autonomy level
  profile.md               # greenfield | brownfield | small-build | feature | bespoke
  run-log.jsonl            # append-only audit: slot, agent_id, run_id, status, timestamps
  slot-01-start.md
  slot-01-running.json     # { agent_id, run_id, started_at, last_heartbeat }
  slot-01-finished.md      # only after scanners green
  slot-01-blocked.md       # agent needs human input
  slot-01-answer.md        # human response → harness resumes
  …
```

**Active slot rule:** smallest `NN` where `start` exists, `finished` absent, and not superseded by `blocked` awaiting `answer`.

---

## `manifest.md` fields (bespoke per engagement)

```yaml
goal: "<one line>"
profile: greenfield | brownfield | small-build | feature | bespoke
autonomy: tight | moderate | full
checkpoint_policy: after_every_slot | after_every_run | on_block_only
run_sizing_policy:
  stories_per_slot: 2
  stages_per_run: 1
  stall_timeout_minutes: 15
  notification_detail: high   # high | normal — high-risk slots include risk type + early questions
slots:
  - id: "01"
    run: "Run 1 — discovery slice A"
    stage: discovery
    role: product-owner
    skills: [abd-story-mapping, abd-domain-terms]
    expected_artifacts: [story-graph.json, docs/domain/domain-terms.md]
    entry_conditions: [context-brief-provided]
    early_question_triggers: [domain-relationship-uncertain]
```

Delivery lead agent writes this from `abd-delivery-planning` after risk classification. `run_sizing_policy` is updated by the lead after each run; the CLI harness reads it to adjust checkpoint frequency, stall timeout, and notification content. Operator can override runs upfront; lead documents overrides with rationale.

---

## Slot lifecycle

```
PENDING → RUNNING → [BLOCKED] → FINISHED | FAILED
```

| Transition | Who | Condition |
|------------|-----|-----------|
| → PENDING | Delivery lead agent | Verifies entry conditions from `stages/<stage>.md`; writes `slot-NN-start.md` with role, skills, corrections, early questions |
| PENDING → RUNNING | CLI harness | Detects start file, assembles bootstrap prompt, launches team member agent, writes `slot-NN-running.json` |
| RUNNING → BLOCKED | Team member agent | Writes `slot-NN-blocked.md` with specific question + context paths; harness notifies operator |
| BLOCKED → RUNNING | CLI harness | Detects `slot-NN-answer.md`, resumes agent with answer |
| RUNNING → FINISHED | Team member agent | Self-review + mid-slot checkpoint confirmed + scanners green + role-playbook outcomes verified; writes `slot-NN-finished.md`; harness notifies operator |
| FINISHED → gates validated | Delivery lead agent | Reads finished file, validates exit gates + cross-stage checks + scanners; presents at stage checkpoint for operator approval |
| → FAILED | CLI harness | Stall timeout (after one retry) or unrecoverable error; writes reason to run log; notifies operator |

**Lead cannot mark a run complete without** `slot-NN-finished.md` + gate check + operator approval.

**Lead cannot open slot N+1 without** validating slot N gates and operator approving stage exit (or explicit override in `manifest.md`).

---

## `slot-NN-start.md` required fields

```markdown
team-role: product-owner | analyst | engineer | reviewer
workspace: <absolute path>
stage: discovery | prioritization | exploration | scenarios | acceptance-tests | engineering
run_scope: story ids or slice id — exact, not "the onboarding flow"
skills: [abd-story-mapping, abd-domain-terms]   # ordered; from stage definition
corrections: docs/corrections-log.md — filter by Affects for this stage and scope
checkpoint: after_slot | mid_slot | none
entry_conditions_met: [list of verified preconditions from stages/<stage>.md]
early_questions: if domain relationship uncertain → STOP and write blocked.md
```

---

## Adaptive run sizing

Policy encoded in delivery lead AGENT.md / planning skill and written to `manifest.md` `run_sizing_policy` — CLI harness reads and enforces:

| Phase | Run size | Checkpoints | Autonomy | Harness enforcement |
|-------|----------|-------------|----------|---------------------|
| **Cold start** | 1 stage, 1–2 stories per slot | After every slot | `tight` | Short stall timeout, high notification detail |
| **Corrections declining** | Wider scope per slot | After every run | `moderate` | Default stall timeout, normal notification |
| **Stable** | Multi-stage runs, pre-approved chains | On block only | `full` (if granted upfront) | Long stall timeout, completion-only notification |

After each run: lead writes a **run summary** to `run-log.jsonl`, appends a revision to `agile-delivery-plan.changelog.md`, reads `docs/corrections-log.md` tagged by stage, computes error rate, and proposes sizing changes. Recurring error class at a late stage → next run adds `early_question_triggers` at an earlier stage in the manifest. If autonomy is tight/moderate, operator approves sizing changes at a checkpoint first.

---

## CLI harness loop

```
loop:
  1. Read manifest → read run_sizing_policy → adjust stall timeout + notification detail
  2. Read agent_mode from config (local | cloud)
  3. Find active slot NN (smallest with start, no finished)
  4. If slot-NN-finished exists → notify operator (artifact summary + scanner pass/fail) → signal delivery lead to validate gates
  5. If slot-NN-blocked and no answer → notify operator; wait
  6. If slot-NN-running.json heartbeat stale (> stall timeout from policy) → cancel → retry once → FAILED + notify
  7. Else launch via Cursor SDK:
       local mode  → Agent.create(local=LocalAgentOptions(cwd=workspace))
       cloud mode  → Agent.create(cloud=CloudAgentOptions(repos=[{url, ref}]))
       cli fallback→ cursor agent -p ... (local only, when SDK not installed)
     Bootstrap prompt assembled from slot-NN-start.md + AGENT.md + INSTRUCTIONS.md
  8. Track agent_id + run_id; append RUNNING to run-log.jsonl; monitor heartbeat every 60s
  9. On run end: if blocked file → notify; if finished → goto 4
```

**Status:** `harness status` reads manifest + active slot + checklist progress + last run-log entry → one-line summary.

**Agent modes:**

| Mode | Config | Execution | Walk-away? |
|------|--------|-----------|------------|
| `local` | `agent_mode: local` | Operator machine via Cursor SDK `LocalAgentOptions` (fallback: CLI subprocess) | No — requires open terminal |
| `cloud` | `agent_mode: cloud`, `repo_url` set | Cursor-hosted VM via SDK `CloudAgentOptions` | Yes — survives terminal/machine shutdown |

Cloud agent IDs are prefixed `bc-`. The SDK auto-detects runtime on `Agent.resume(agent_id)`.

**Resume:** On restart after session kill → read war room state → stale running.json treated as stall → recovery flow. Launch fresh delivery lead session that reads manifest/log/checklist/plan and resumes from slot state. Cloud agents resume by ID. No re-brief.

---

## Check-in from anywhere

Anyone opens the repo (or GitHub on phone) and reads:

- `manifest.md` — where we are, profile, autonomy, run sizing policy
- `abd-delivery-lead/progress/delivery-plan-checklist.md` — plan progress (checked-off stages)
- `run-log.jsonl` — what ran, when, outcome, run summaries
- `slot-NN-finished.md` — artifacts touched, scanner results
- `slot-NN-blocked.md` — what question the agent is stuck on (if present)
- `agile-delivery-plan.changelog.md` — plan revision history
- Stage artifacts linked in finished file

Live progress: `slot-NN-running.json` heartbeat + `run-log.jsonl` tail.

Quick check: `harness status` for one-line summary without launching agents.

---

## Notifications

| Event | Action | Detail level |
|-------|--------|-------------|
| `blocked.md` created | Notify operator — question, context paths, slot number | Always high |
| Heartbeat stale | Cancel agent → retry once → if second stall: FAILED + notify | Always high |
| `finished.md` created | Notify operator — artifact summary, scanner pass/fail | Per `run_sizing_policy.notification_detail` |
| Gates pass + operator approves | Notify — stage complete, checklist updated | Normal |
| Gates fail | Notify — correction logged, rework directed | Always high |
| `FAILED` (after retry) | Notify immediately — slot number, both agent_ids, failure reason | Always high |
| Run summary complete | Notify — run results, sizing proposal (if any) | Normal |
| Run change proposed by lead | Notify — approve at checkpoint (tight/moderate) or after the fact (full) | Normal |

---

## Non-negotiables (enforced before finished)

1. Practice skills listed in `start` were read (SKILL.md + `rules/*.md`) and followed
2. Team member self-reviewed drafts against loaded rules before presenting
3. Mid-slot checkpoint confirmed by operator before finalizing artifacts
4. `story-graph.json` updated via `story-graph-ops` for graph-producing stages
5. `run_scanners.py` green for each skill in slot
6. Stage outcomes verified against role playbook "what good looks like"
7. Corrections log updated if output was wrong (at mid-slot checkpoint or scanner failure)
8. Sync-upstream offered per workspace rules
9. Exit gate from `stages/<stage>.md` checked by lead + scanners via execute-skill-using-skills-rules
10. Operator approves stage exit at stage checkpoint before lead opens next slot

Flexible: skill order, bespoke steps, stage order — as long as scanners and gates pass.

---

## Engagement profiles

| Profile | Default run shape | Early-question bias |
|---------|-------------------|---------------------|
| **greenfield** | discovery → exploration first | domain terms before AC |
| **brownfield** | module partition → domain terms | integration boundaries at CRC |
| **small-build** | thin slice → spec → test → code | one story at a time |
| **feature** | scoped epic, skip unrelated stages | scope creep → blocked at planning |
| **bespoke** | lead designs from context inventory | from corrections history |

---

## First pilot

1. One engagement, one run, 3–4 slots max
2. Profile: pick one
3. Autonomy: `tight`
4. One intentional kill-and-resume test
5. Measure: corrections tagged by stage; did domain confusion surface at UL/CRC not spec?

---

## Implementation order

1. **War room templates** — extend file formats: manifest with `run_sizing_policy`, slot-start with `entry_conditions_met`, finished with scanner detail
2. **Delivery lead AGENT.md** — wire Steps 1–8: entry-condition verification, slot authoring with role/skill from stage def, gate validation via execute-skill-using-skills-rules, run summary, plan changelog, lifecycle recovery on resume
3. **Team member AGENT.md** — wire: self-review, mid-slot checkpoint, story-graph-ops update, role-playbook outcome verification
4. **CLI harness script** — main loop: read manifest + run_sizing_policy, launch/monitor agents, heartbeat, stall → retry/notify, finished → notify, blocked → notify, status command, session-kill recovery
5. **Adaptive run-sizing** — lead reads corrections at run end, proposes policy changes, writes updated policy to manifest; harness reads and enforces
6. **Blocker / answer protocol** — blocked.md + answer.md on disk; harness detects + resumes; any-device write support
7. **Audit trail** — run-log.jsonl with agent IDs, timestamps, outcomes, run summaries; plan changelog

---

## Goals this contract serves

- **Walk-away execution** — agents keep working when you leave; stalls recover or escalate
- **Check in from anywhere** — phone, another PC, web; inspect artifacts without opening the original chat
- **Bespoke runs** — delivery lead builds per engagement; war room tracks on disk
- **Earliest error detection** — domain confusion at UL/CRC, not spec/code; small runs + tight gates → scale as errors drop
- **Mechanical orchestration** — lead reliably spawns member/reviewer; scanners enforced before finished
- **Operator role is light** — review at end of run; answer when blocked; not policing every tool call
