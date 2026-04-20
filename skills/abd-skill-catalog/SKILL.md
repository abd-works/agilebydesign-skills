---
name: abd-skill-catalog
description: >-
  Scan the agilebydesign-skills repository (root skills/ and agents/), then
  regenerate a reader-facing Markdown outline plus a small multi-page HTML
  site. Each skill and agent entry includes Challenge, Solution, and
  Description (purpose pulled from SKILL.md or the agent entry doc). Optional
  repository layout summarizes files (with links) and common folders in one
  line each.
license: MIT
metadata:
  author: agilebydesign
  version: "1.0.0"
---

# ABD Skill & Agent Catalogue

Maintain a browsable catalogue of **practice skills** under the repo root
`skills/` and **agents** under `agents/`, aligned with the tone of
`agents/abd-skill-builder/docs/process-outline.md` and the compact HTML chrome
used under `agents/abd-skill-builder/docs/overview/`.

## When to use this skill

- You added, renamed, or retired a skill or agent and the catalogue is stale.
- You need a stakeholder-facing index of what each skill and agent is for.
- You want both Markdown (diffable, review in Git) and HTML (quick browse).

## What it produces

| Artifact | Format | Location (default) |
| --- | --- | --- |
| **Outline** | Markdown | `agents/abd-skill-builder/docs/abd-skill-catalog/outline.md` |
| **Site hub** | HTML | `agents/abd-skill-builder/docs/abd-skill-catalog/catalog/index.html` |
| **Skills grid** | HTML | `agents/abd-skill-builder/docs/abd-skill-catalog/catalog/skills.html` |
| **Agents grid** | HTML | `agents/abd-skill-builder/docs/abd-skill-catalog/catalog/agents.html` |

Each catalogue entry includes:

- **Challenge** — the situation or friction the package addresses.
- **Solution** — what the package does about it (usually YAML `description`).
- **Description** — expanded purpose text from `## Purpose` when present.
- **Repository layout** — top-level files with a one-line blurb and relative
  link; common directories (`rules`, `templates`, `scripts`, …) get **one**
  folder-level sentence instead of enumerating every file inside.

## Agent instructions

1. **Regenerate on command.** From the **agilebydesign-skills** repository root,
   run:

   ```bash
   python skills/abd-skill-catalog/scripts/generate_abd_catalog.py
   ```

   Options:

   - `--repo-root <path>` — defaults to the parent of the repo `skills/`
     directory (detected from this script location).
   - `--output-dir <path>` — overrides the default output directory above.

2. **Discovery rules.**

   - **Skills:** every immediate child of `skills/` that contains `SKILL.md`.
     (Skips plain files and folders without `SKILL.md`.)
   - **Agents:** every immediate child of `agents/` that contains one of
     `AGENT.md`, `AGENTS.md`, or `SKILL.md` (first match in that order).

3. **Extraction (skills).** Same heuristics as `skill-garden-catalogue`:

   - *Name* — YAML `name`, else directory name.
   - *Challenge* — first meaningful sentence from `## Purpose`, else first
     substantive bullet from “When to use”, else the H1 title.
   - *Solution* — YAML `description` (trimmed).
   - *Description* — full `## Purpose` body when present, else beginning of
     the markdown body.

4. **Extraction (agents).**

   - *Name* — YAML `name` if present, else markdown H1 heading text.
   - *Challenge / Solution / Description* — prefer `## Purpose` when present;
     otherwise derive from the opening sections (`## Introduction`, first
     paragraphs). YAML `description` feeds **Solution** when present.

5. **Templates.** HTML shell and CSS live under
   `skills/abd-skill-catalog/templates/` and are copied with token replacement.
   Edit those files to change branding or layout without touching Python.

6. **Idempotent.** Running the script twice with the same tree overwrites the
   same outputs deterministically.
