# Watch for bloated classes — payments example

**Skill:** abd-ooad — **Step 9:** danger signals for **Payment** growing into a god object.

**Upstream:** `invariants-in-the-model.md`.

> **Continual refinement:** Full notation is in **[Domain model Markdown](../library/domain-model.md)** (*Domain concept* template; class definition and diagram refined together). In this payments thread, **`**newly added**`** marks a property or operation line **first introduced in this step file** (Steps 1–4 stay pre-notation; formal `- <type> property` / `operation(...) → return` lines begin at Step 5).

---

## Bloat signals → term-registry.md

> Tag notes on the class model with `[s1-p9]` — see `templates/domain model template.md` for the full tag table.

Record every bloat signal and proposed extraction in `term-registry.md` Notes, not in a separate table. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Bloat Signal - {{what_clusters_are_mixed}} suggest: {{extract}}` — when a class mixes unrelated property or operation clusters
- `Role Separation - {{merged_role}} splits into: {{role_a}}, {{role_b}}` — when a class is doing two distinct jobs
- `Follow-up - {{question_or_action}}` — deferred extractions or design debt

**Signs to watch for:** unrelated property clusters, methods touching different responsibility areas, long conditional chains on kind/type, name smells like `*Manager` or `*Processor`.**

---

## Carry forward → Step 10

Ask whether **"user"** / **payer** / **admin** are one abstraction or **smashed roles**.

---

## Continual refinement (this step)

- **Delta:** **signals and extract paths** (pricing, redirect, refund policy, notifier) — mostly narrative; new **types** introduced here get **`**newly added**`** on their first **property** / **operation** lines when promoted.

---

## Action Checklist

- [ ] Have you identified any class with more than two distinct responsibilities?
- [ ] Have you identified any class that contains both state management and policy enforcement?
- [ ] Have you proposed concrete extractions (new types) for each bloat signal found?
- [ ] Have you added `Bloat Signal` notes to `term-registry.md` for the bloated class and `Follow-up` notes for each deferred extraction?
- [ ] Have you logged any deferral as explicit design debt with a rationale?
- [ ] Have you noted carry-forward items to Step 10 (smashed abstractions)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
