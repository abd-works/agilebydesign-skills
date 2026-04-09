# Smashed abstractions and hidden roles — payments example

**Skill:** abd-ooad — **Step 10:** one noun, several **real** roles.

**Upstream:** `garbled-payments-spec.md`.

> **Continual refinement:** Full notation is in **[Domain model Markdown](../library/domain-model.md)** (*Domain concept* template; class definition and diagram refined together). In this payments thread, **`**newly added**`** marks a property or operation line **first introduced in this step file** (Steps 1–4 stay pre-notation; formal `- <type> property` / `operation(...) → return` lines begin at Step 5).

---

## Smashed roles → term-registry.md

> Tag notes on the class model with `[s1-p10]` — see `templates/domain model template.md` for the full tag table.

Every hidden role discovered in this phase belongs in `term-registry.md` Notes, not in a separate table. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Role Separation - {{merged_role}} splits into: {{role_a}}, {{role_b}}` — when a single noun covers multiple distinct actors or responsibilities
- `Classified - {{kind}} {{reason}}` — when a role resolves to a clear type (Entity, Role, Policy)
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — when role ownership is contested (e.g., org conflict)
- `Follow-up - {{question_or_action}}` — deferred role boundaries

**A single generic class (User, Actor, Person) that blurs permissions, money flow, and config is a smash signal — record it.**

---

## Outcomes (payments)

- **Identity**: **Account** / **PartyId** in IAM BC — **not** modeled fully here.
- **This BC**: **`payerRef`**, **`merchantRef`**, **`actor`** on audit (`user` vs `system` vs `psp_webhook`) — **references + audit**, not rich user graphs.
- **Admin actions** → **configuration** rows or **admin audit** with actor id — optional **AdminAction** log, not `Admin` entity inside payments core.

---

## Carry forward → Step 11

Use **inheritance** only if **PaymentMethod** subtypes share substitutable **authorize/capture** behavior (see next file).

---

## Continual refinement (this step)

- **Delta:** **role separation** — **`payerRef`**, **`merchantRef`**, **`actor`** on audit vs monolithic **User**; refine **Interactions** and collaborator lists when serializing to the spec.

---

## Action Checklist

- [ ] Have you identified any class that serves multiple distinct roles in different contexts?
- [ ] Have you separated smashed abstractions into explicit roles with their own names and responsibilities?
- [ ] Have you checked for hidden roles disguised as generic names (User, Actor, Person)?
- [ ] Have you added `Role Separation` notes to `term-registry.md` for each smashed abstraction found?
- [ ] Have you updated the spec with `payerRef`, `merchantRef`, or equivalent references in place of rich user graphs?
- [ ] Have you noted carry-forward items to Step 11 (inheritance)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
