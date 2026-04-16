---
name: abd-acceptance-criteria
description: >-
  Teaches exploration-phase acceptance criteria for story-graph.json: WHEN/THEN/AND/BUT,
  behavioral language, atomic AC, actor alternation, channel-specific detail, and
  verb–noun naming for story elements. This skill **migrates** rules and scanners **from**
  the agile_bots repo (story_bot exploration behavior) into this skills package — it is a
  portable copy for execute_rules / CLI scanners, not a live symlink or runtime mapping.
  When building AC from sources, output **all** template artifacts in `templates/`
  (currently `acceptance-criteria.md` and `acceptance-criteria.txt`) with the same coverage.
  Use when writing or reviewing acceptance criteria, exploration behavior, WHEN/THEN
  quality, or story-graph.json AC arrays.
---

# abd-acceptance-criteria

## Migration source (agile_bots)

This skill is **migrated from** the Agile Bots codebase — not merely “mapped” to it:

| Role | Location in agile_bots |
| --- | --- |
| Rule definitions (priority, DO/DON'T, examples) | `bots/story_bot/behaviors/exploration/rules/*.json` |
| Scanner implementations | `src/scanners/*` (classes referenced by those JSON files) |

**Canonical product behavior** may continue to evolve in **agile_bots** first. When rules or scanners change there, **re-migrate** (copy + adapt imports) into this skill so Open Agent Skills / `execute_rules` stay aligned.

---

## Steps

1. **Build** using **every** template file in this skill's `templates/` folder, and the `rules/` in this skill.
2. **Validate** using rules in `rules/`. For the **mechanical** scanner pass, use the **execute_rules** skill (same repo): run **`run_scanners.py`** with **`--skill-root`** = this skill directory and **`--workspace`** = the tree that contains **`docs/story/story-graph.json`** (or **`story-graph.json`**). To **list** scanners, use **`rule_inventory.py --list-scanners`** with the same **`--skill-root`**. Full intent (AI/rules pass **plus** scanner pass) and exact commands are in **`skills/execute_using_rules/SKILL.md`**. **Which** scanners run is defined by **`rules/*.md`** (`scanner:` frontmatter → `scanners/<stem>-scanner.py`), not a separate manifest. **Story graph** types live in **`skills/story-graph-ops/scripts/`**. **`scanner_runner`** (execute_rules) drives each scanner CLI the same way.

### Use every template file (required)

When you **create or rewrite** acceptance criteria from requirements, you **must** deliver **one output artifact per file** in `templates/`. **Do not** emit only Markdown or only plain text unless the user **explicitly** asks for a single format.

| Template | What to produce |
| --- | --- |
| `templates/acceptance-criteria.md` | Story-level AC using WHEN/THEN/AND/BUT; include the **`## Instructions`** block from that template at the end (or equivalent summary). |
| `templates/acceptance-criteria.txt` | The **same** behavioral coverage as **plain text** — matching structure; no need to duplicate long Instructions if the `.md` carries them. |

**Consistency:** AC semantics and story coverage must match between `.md` and `.txt`.

**If new files are added** under `templates/` later, produce a corresponding artifact for **each** new template the same way.

---

## When to use this skill

Load this skill when **any** of these apply:

- You are writing or reviewing **`acceptance_criteria`** on stories in `story-graph.json`.
- You need WHEN/THEN/AND quality, atomic AC, actor alternation, BUT for negatives, or channel-specific CLI/Panel wording.
- An agent is asked to “explore” a story, “write AC”, or “align with exploration rules”.
- You are running **execute_rules** scanners against a workspace with a story graph.

---

## Core concepts

### Behavioral vs technical

AC describe **observable** user/system behavior. Avoid implementation detail (file formats, APIs, class names) unless the story is explicitly technical and scoped that way.

### WHEN / THEN / AND / BUT

- **WHEN** — trigger or precondition.
- **THEN** — primary outcome.
- **AND** — additional or chained outcomes (especially multiple system reactions).
- **BUT** — what does **not** happen on error/prevention paths (negative conditions).

Reserve **Given** for **scenarios** (BDD), not for AC lines in the story graph (per agile_bots exploration policy).

### Atomic AC

State the **general** case once; follow-on AC only describe **deltas**. Reduces duplicated WHEN/THEN blocks.

### Actor alternation

Interleave user-visible and system-visible steps. Avoid long runs of the same actor without switching (see rule + scanner).

### Domain consistency

As domains grow, keep **parallel** AC structure across related domains; split stories when one AC mixes incompatible domain behaviors.

---

## Build

Produce **both** **`acceptance-criteria.md`** and **`acceptance-criteria.txt`** artifacts (same coverage), following **`templates/`**. Delivering a single format is incorrect unless the user explicitly requested only one.

---

## Validate

Review **both** artifacts and the story graph for:

- **Behavioral** language and appropriate **WHEN/THEN/AND/BUT** structure.
- **Atomic** AC (no duplicated base blocks).
- **Actor** alternation and **AND** chaining where applicable.
- **Verb–noun** names for epics/sub-epics/stories (shared bar with **abd-story-mapping**; this skill ships the exploration **verb–noun** scanner migrated from agile_bots).

Run mechanical scanners via **execute_rules** as described in **Steps**.

---

<!-- execute_rules:bundle_rules:begin -->

### Rule: Atomic acceptance criteria

**Scanner:** `scanners/atomic-ac-scanner.py` — **`AtomicACScanner`**  
Avoid repeating the same WHEN/THEN/AND prefix across AC; general case once, variations only what differs. (**Full text:** `rules/use-atomic-acceptance-criteria.md`.)

### Rule: Behavioral AC at story level

**Scanner:** `scanners/behavioral-ac-scanner.py` — **`BehavioralACScanner`**  
Intent/policy from migrated JSON; mechanical scan currently empty in source repo. (**Full text:** `rules/behavioral-ac-at-story-level.md`.)

### Rule: Stories have 4–9 acceptance criteria (heuristic)

**Scanner:** `scanners/story-sizing-scanner.py` — **`StorySizingScanner`**  
Counts WHEN+AND tokens; aligns with exploration sizing goals. (**Full text:** `rules/stories-have-4-to-9-acceptance-criteria.md`.)

### Rule: Alternate actors in steps

**Scanner:** `scanners/actor-alternation-scanner.py` — **`ActorAlternationScanner`**  
Avoid >2 consecutive steps from the same actor. (**Full text:** `rules/alternate-actors-in-steps.md`.)

### Rule: Enumerate all AC permutations

**Scanner:** `scanners/enumerate-ac-permutations-scanner.py` — **`EnumerateACPermutationsScanner`**  
Policy; mechanical scan stub in source repo. (**Full text:** `rules/enumerate-all-ac-permutations.md`.)

### Rule: Keep AC consistent across connected domains

**Scanner:** `scanners/ac-domain-crossing-scanner.py` — **`ACDomainCrossingScanner`**  
Warn when one AC appears to mix multiple domain behaviors with behavioral verbs. (**Full text:** `rules/keep-acceptance-criteria-consistent-across-connected-domains.md`.)

### Rule: Use AND for multiple reactions

**Scanner:** `scanners/reaction-chaining-scanner.py` — **`ReactionChainingScanner`**  
Chain sequential system reactions; flag separate WHEN/THEN for chained system-only steps; cap long AND chains. (**Full text:** `rules/use-and-for-multiple-reactions.md`.)

### Rule: Use BUT for negative conditions

**Scanner:** `scanners/negative-conditions-scanner.py` — **`NegativeConditionsScanner`**  
Error language without BUT may warn. (**Full text:** `rules/use-but-for-negative-conditions.md`.)

### Rule: Use channel-specific language

**Scanner:** `scanners/channel-specific-language-scanner.py` — **`ChannelSpecificLanguageScanner`**  
Prefer concrete cli./Panel examples over generic “Bot …”. (**Full text:** `rules/use-channel-specific-language.md`.)

### Rule: Verb–noun format for story elements

**Scanner:** `scanners/verb-noun-scanner.py` — **`VerbNounScanner`**  
NLTK-heavy name checks for epic/sub-epic/story nodes (migrated implementation). (**Full text:** `rules/use-verb-noun-format-for-story-elements.md`.)

<!-- execute_rules:bundle_rules:end -->
