(E) Deliver Through CLI Harness and Agents
    (E) Configure and Bootstrap Engagement
        (S) Operator --> Set Harness API Key and Defaults
        (S) Operator --> Configure Notification Channel and Stall Timeout
        (S) System --> Persist Harness Configuration to Disk
        (S) Operator --> Provide Engagement Parameters
        (S) CLI Harness --> Prompt for Missing Required Parameters
        (S) CLI Harness --> Create Engagement Workspace
        (S) CLI Harness --> Merge Parameters into Harness Config File
        (S) CLI Harness --> Launch Delivery Lead Agent with Engagement Context
    (E) Establish Workspace and Build Plan (Delivery Lead Steps 1–2)
        (S) Delivery Lead Agent --> Confirm Workspace Path and Inventory Existing Artifacts
        (S) Delivery Lead Agent --> Create Progress Folder and Generate Initial Checklist Using track_task
        (S) Delivery Lead Agent --> Read abd-delivery-planning SKILL.md and Matching Strategy Files
        (S) Delivery Lead Agent --> Assess Context Against Six Risk Types
        (S) Delivery Lead Agent --> Select Delivery Strategy from strategies/
        (S) Delivery Lead Agent --> Design Runs with Stages, Scope, and Checkpoint Policy
        (S) Delivery Lead Agent --> Write agile-delivery-plan.md to Workspace Root
        (S) Delivery Lead Agent --> Run Plan-Shape Scanners Using execute-skill-using-skills-rules
        (S) Delivery Lead Agent --> Present Plan at CHECKPOINT
        (S) Operator --> Approve or Revise Delivery Plan
    (E) Set Up War Room (after plan approval)
        (S) Delivery Lead Agent --> Create delivery-war-room/ Folder
        (S) Delivery Lead Agent --> Write manifest.md with Goal, Profile, Autonomy, Checkpoint Policy, Slot Definitions
        (S) Delivery Lead Agent --> Write INSTRUCTIONS.md from abd-delivery-war-room Template
        (S) Delivery Lead Agent --> Write profile.md with Profile Rationale
        (S) Delivery Lead Agent --> Initialize run-log.json
        (S) Delivery Lead Agent --> Set Initial Run Sizing Policy from Risk Classification
    (E) Open Stage and Launch Slot (Delivery Lead Steps 3–4, repeats per stage)
        (S) Delivery Lead Agent --> Read stages/<stage>.md for Entry Conditions and Exit Gate
        (S) Delivery Lead Agent --> Verify Entry Conditions Met from Prior Stage Artifacts
        (S) Delivery Lead Agent --> Determine Team Role and Select Ordered Practice Skills
        (S) Delivery Lead Agent --> Filter Corrections Log for Stage-Relevant Entries
        (S) Delivery Lead Agent --> Add Early Question Triggers from Corrections Patterns
        (S) Delivery Lead Agent --> Write slot-NN-start.md with Role, Workspace, Stage, Scope, Skills, Corrections, Questions
        (S) CLI Harness --> Detect New Slot Start File in War Room
        (S) CLI Harness --> Assemble Bootstrap Prompt from Slot Start + AGENT.md + INSTRUCTIONS.md
        (S) CLI Harness --> Launch Team Member Agent
        (S) CLI Harness --> Write Running File and Start Heartbeat Monitor
    (E) Execute Stage Work (Team Member, inside one slot)
        (S) Team Member Agent --> Read Slot Start File for Role, Scope, and Skills
        (S) Team Member Agent --> Resolve Team Role and Read Role Playbook
        (S) Team Member Agent --> Sync with Existing Workspace Artifacts
        (S) Team Member Agent --> Read Practice Skill SKILL.md and All rules/*.md
        (S) Team Member Agent --> Generate Artifacts Using Practice Skill Templates
        (S) Team Member Agent --> Self-Review Draft Against Loaded Rules
        (S) Team Member Agent --> Present Draft at CHECKPOINT
        (S) Operator --> Confirm or Correct Draft
        (S) Team Member Agent --> Log Correction to corrections-log.md on User Correction
        (S) Team Member Agent --> Update story-graph.json Using story-graph-ops
        (S) Team Member Agent --> Run Scanners Using execute-skill-using-skills-rules
        (S) Team Member Agent --> Fix Violations and Re-Run Until Clean
        or (S) Team Member Agent --> Present Violations at CHECKPOINT for Human Decision
        (S) Team Member Agent --> Verify Stage Outcomes Match Role Playbook
        (S) Team Member Agent --> Write slot-NN-finished.md with Artifact Paths and Scanner Results
        or (S) Team Member Agent --> Write slot-NN-blocked.md with Question and Context
    (E) Handle Block During Execution
        (S) CLI Harness --> Detect Blocked File in War Room
        (S) CLI Harness --> Send Block Notification with Question Context to Operator
        (S) Operator --> Write Answer File to War Room from Any Device
        (S) CLI Harness --> Detect Answer File Arrival
        (S) CLI Harness --> Resume Blocked Agent with Answer Context
    (E) Recover from Stall During Execution
        (S) CLI Harness --> Detect Stall from Expired Heartbeat
        (S) CLI Harness --> Kill Stalled Agent Process
        (S) CLI Harness --> Retry Stalled Slot with Same Bootstrap Prompt
        (S) CLI Harness --> Mark Slot as Failed After Retry Exhausted
        (S) CLI Harness --> Send Failure Notification to Operator
    (E) Validate Stage Exit (Delivery Lead Step 5)
        (S) CLI Harness --> Detect Finished File and Notify
        (S) Delivery Lead Agent --> Read Finished File and Stage Artifacts
        (S) Delivery Lead Agent --> Verify Exit Gate Conditions from stages/<stage>.md
        (S) Delivery Lead Agent --> Run Cross-Stage Consistency Checks Against Prior Stages
        (S) Delivery Lead Agent --> Run Practice Skill Scanners on Team Member Output
        (S) Delivery Lead Agent --> Log Corrections on Gate Failure
        (S) Delivery Lead Agent --> Present Gate Results at CHECKPOINT
        (S) Operator --> Approve Stage Exit
    (E) Review Slot Output (optional, before gate sign-off)
        (S) Delivery Lead Agent --> Author Reviewer Slot Start File with team-role: reviewer
        (S) CLI Harness --> Launch Reviewer Agent
        (S) Reviewer --> Read Prior Slot Finished File and Artifacts
        (S) Reviewer --> Validate Against Exit Gates and Scanners
        (S) Reviewer --> Write Reviewer Finished File with Findings
        (S) Delivery Lead Agent --> Read Reviewer Findings Before Gate Sign-Off
        * Gap: Reviewer role playbook (roles/reviewer.md) does not exist yet.
    (E) Hand Off and Chain to Next Stage (Delivery Lead Step 6, loops back)
        (S) Delivery Lead Agent --> Mark Stage Done in Delivery Plan Checklist
        (S) Delivery Lead Agent --> Pass Artifacts, Decisions, and Filtered Corrections Forward
        (S) Delivery Lead Agent --> Append Slot Completion Event to run-log.jsonl
        (S) Delivery Lead Agent --> Author Next slot-NN-start.md
        (S) CLI Harness --> Detect Next Slot and Launch (loop to Open Stage)
    (E) Complete Run and Adapt Sizing (Delivery Lead Step 7)
        (S) Delivery Lead Agent --> Summarize Run Results and Artifact Quality
        (S) Delivery Lead Agent --> Read Corrections Log Entries by Stage for This Run
        (S) Delivery Lead Agent --> Compute Error Rate Across Completed Slots
        (S) Delivery Lead Agent --> Append Run Revision to plan Changelog
        (S) Delivery Lead Agent --> Regenerate Checklist Preserving Completed Marks
        (S) Delivery Lead Agent --> Propose Run Sizing Policy Changes Based on Error Patterns
        (S) Delivery Lead Agent --> Propose Autonomy Escalation if Error Rate Declining
        (S) CLI Harness --> Read Updated Run Sizing Policy from Manifest
        (S) CLI Harness --> Adjust Checkpoint Frequency, Stall Timeout, and Notification Content
        (S) Delivery Lead Agent --> Present Run Summary at CHECKPOINT
        (S) Operator --> Approve Run Completion and Sizing Changes
    (E) Complete Plan (Delivery Lead Step 8)
        (S) Delivery Lead Agent --> Present Final Summary of All Runs
        (S) Delivery Lead Agent --> Propose New Strategy File if Engagement Pattern is Novel
        (S) Delivery Lead Agent --> Close Delivery Plan Checklist
        (S) Operator --> Approve Plan Completion
    (E) Check In on Progress (anytime)
        (S) Operator --> Read Manifest from Any Device
        (S) Operator --> Read Run Log for Audit Trail
        (S) Operator --> Read Active Slot Files for Current Status
        (S) Operator --> Read Finished Files for Completed Artifacts
    (E) Resume After Session Kill
        (S) CLI Harness --> Read War Room State on Startup
        (S) CLI Harness --> Find Active Slot with No Running Process
        (S) CLI Harness --> Relaunch Agent from Slot Start File
        (S) CLI Harness --> Recover In-Progress Work from Disk Artifacts
        * Gap: Delivery lead agent lifecycle — does the harness launch it once per engagement, once per run, or once per slot? Resume needs to handle lead recovery, not just team members.

## Consolidation Notes (for AC phase)

### Stage-Specific Practice Skills (under Execute Stage Work)
The team member workflow is the same for all six stages; what varies is role, practice skill, and output.
AC must specify per stage:
- Discovery: Product Owner, abd-story-mapping → story-graph.json + story-map.md
- Prioritization: Product Owner, abd-thin-slicing → slice assignments + thin-slicing.md
- Exploration: Analyst, abd-acceptance-criteria → AC arrays + acceptance-criteria.md
- Story Definition: Analyst, abd-specification-by-example → scenario files + graph refs
- Acceptance Tests: Engineer, abd-acceptance-test-driven-development → RED test files + test mapping
- Engineering: Engineer, abd-clean-code → GREEN production code

### Practice Skill Families
Five families with consistent structure (SKILL.md, templates/, rules/*.md, scanners/):
- Story-driven delivery: abd-story-mapping, abd-thin-slicing, abd-acceptance-criteria, abd-specification-by-example, abd-acceptance-test-driven-development
- Domain-driven design: abd-ubiquitous-language, abd-class-responsibility-collaborator, abd-object-model, abd-scenario-walkthrough, abd-domain-terms, abd-module-partition
- Architecture-centric delivery: abd-architecture-outline, abd-architecture-blueprint, abd-architecture-template, abd-architecture-reference
- User experience design: abd-information-architecture, abd-ux-mockup, abd-interface-design
- Engineering: abd-clean-code (shared with story-driven for GREEN/REFACTOR)

### Delivery Lead Skills (not delegated — used directly by lead)
- abd-delivery-planning: context, risk, strategy selection, run design (9 strategies in strategies/)
- abd-delivery-war-room: war room protocol, INSTRUCTIONS.md template, slot file templates
- track_task: delivery plan checklist generation and checkpoint tracking
- execute-skill-using-skills-rules: scanner execution for gate validation + corrections logging
- guidance/workspace: workspace resolution and skill-config.json

### Delivery Lead ↔ CLI Harness Interaction
They interact exclusively through the war room (disk):
- Lead writes: manifest, slot start files, run log entries, sizing policy
- Harness reads: manifest (sizing policy), slot start files (bootstrap), finished/blocked/answer files
- Harness writes: running files (heartbeat), notifications
- Neither calls the other directly

### Reviewer Role
Same AGENT.md and war room protocol as executor. AC must specify:
- How team-role: reviewer is assigned (lead authors reviewer slot)
- What reviewer reads (prior slot finished file + artifacts only)
- What reviewer writes (reviewer finished file with findings)
- Whether reviewer can log corrections or only report findings

### Notification Types
Four triggers, same channel, different content:
- Completion: artifact summary + scanner pass/fail
- Block: question text, context, reason
- Stall: agent ID, duration, retry status
- Failure: slot number, error, retry exhausted
- High-risk enrichment: risk type + early question triggers appended

## Context Gaps

- Reviewer role playbook: no `agents/abd-team-member/roles/reviewer.md` exists — need to author.
- AI-model risk type: listed in contract but not confirmed in abd-delivery-planning strategies — check strategies/*.md.
- DDD and UX skills in pipeline: six stages map to story-driven and engineering skills. Where do DDD (UL, CRC, object-model) and UX (IA, mockup, interface-design) skills fit? Alternative stages, parallel tracks, or extensions?
- abd-delivery-war-room skill: exists at `skills/delivery/abd-delivery-war-room/` but not referenced in current delivery lead AGENT.md — active or dormant?
- Delivery lead agent lifecycle: 8-step workflow assumes continuous session. Does harness launch lead once per engagement, per run, or per slot? Resume-after-kill must handle lead recovery too.
- Harness configuration persistence: `~/.cursor/cli-config.json` vs `.cursor/cli.json` — confirm canonical path and per-engagement merge.
