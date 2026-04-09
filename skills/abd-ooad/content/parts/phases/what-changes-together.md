# What changes together — payments example

**Skill:** abd-ooad — **Step 17:** **cohesion** and **bounded context** hints.

**Upstream:** `tension-as-a-signal.md`.

> **Continual refinement:** Full notation is in **[Domain model Markdown](../library/domain-model.md)** (*Domain concept* template; class definition and diagram refined together). In this payments thread, **`**newly added**`** marks a property or operation line **first introduced in this step file** (Steps 1–4 stay pre-notation; formal `- <type> property` / `operation(...) → return` lines begin at Step 5).

---

## Cohesion clusters → term-registry.md

> Tag notes on the class model with `[s1-p17]` — see `templates/domain model template.md` for the full tag table.

Record cohesion clusters — what changes together and what belongs in a different BC — in `term-registry.md` Notes, not in a separate table. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Cohesion Group - {{group_name}} changes with: {{related_terms}}` — terms that form a stable co-change cluster
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — when a term appears in more than one cluster
- `Follow-up - {{question_or_action}}` — boundary decisions deferred to architecture

**Any term whose BC ownership is unclear or disputed gets a `Tension` note here.**

---

## Carry forward → Step 18

**Validate** with **scenarios** — happy path, sanctions, partial capture, idempotency replay.

---

## Continual refinement (this step)

- **Delta:** **cohesion clusters** — **Payment** vs **Order** vs **Catalog** vs **Compliance** vs **Warehouse**; use to sanity-check **module** boundaries and **depends_on** in **`map-model-spec.json`**.

---

## Action Checklist

- [ ] Have you identified distinct cohesion clusters (groups of classes that change together)?
- [ ] Have you confirmed that each cluster maps to a clear bounded context or module boundary?
- [ ] Have you verified that no cluster has cross-cutting dependencies that violate the module boundary?
- [ ] Have you added `Cohesion Group` notes to `term-registry.md` for each cluster, and `Tension` notes for terms that span multiple clusters?
- [ ] Have you updated `map-model-spec.json` `depends_on` entries to reflect cohesion findings?
- [ ] Have you noted carry-forward items to Step 18 (validate with scenarios)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
