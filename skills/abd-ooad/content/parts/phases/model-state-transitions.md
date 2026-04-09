# Model state transitions — payments example

**Skill:** abd-ooad — **Step 14:** illegal transitions are **unrepresentable** or **rejected**.

**Upstream:** `invariants-in-the-model.md`, `prefer-composition.md`.

> **Continual refinement:** Full notation is in **[Domain model Markdown](../library/domain-model.md)** (*Domain concept* template; class definition and diagram refined together). In this payments thread, **`**newly added**`** marks a property or operation line **first introduced in this step file** (Steps 1–4 stay pre-notation; formal `- <type> property` / `operation(...) → return` lines begin at Step 5).

---

## State transitions → term-registry.md

> Tag notes on the class model with `[s1-p14]` — see `templates/domain model template.md` for the full tag table.

All state candidates, legal transitions, illegal transitions, and related invariants belong in `term-registry.md` Notes, not only in spec comments or inline tables. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `State Candidate - states: {{list}} illegal transitions: {{list}}` — the full state set and which transitions must be rejected
- `Invariant - {{rule_that_must_always_hold}}` — each guard that enforces a valid transition (e.g., "SETTLED cannot return to AUTHORIZED")
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — ambiguous or spec-conflicting transitions (e.g., TTL 24h vs 72h)
- `Follow-up - {{question_or_action}}` — transitions deferred to product or architecture

**Capture the full lifecycle on the term row for the stateful entity — not only in code comments.**

---

## Payment — states (from spec + consolidation)

`INITIATED` → `METHOD_SELECTED` → `PENDING_REDIRECT` (optional) → `AUTHORIZED` → `CAPTURED` / `PARTIALLY_CAPTURED` → `SETTLED`  
Branches: `FAILED` (terminal), `CANCELLED` (if allowed).

**Refund** (separate aggregate or child): `REQUESTED` → `COMPLETED` / `FAILED`.

---

## Events vs state

- **`payment.settled`** emitted **on** transition to `SETTLED` — **Warehouse** / digital fulfillment subscribe.
- **Webhook** handlers map external status → **command** on aggregate — **not** direct field set from HTTP.

---

## Carry forward → Step 15

**Re-read** spec for missed contradictions (TTL, MoR, digital vs physical).

---

## Continual refinement (this step)

- **Delta:** **PaymentState** / **RefundState** transition sets and **illegal** edges — attach **`Invariant:`** under **`state`** or under **operation** lines that guard transitions; **`**newly added**`** when first stating each guard in formal form.

---

## Action Checklist

- [ ] Have you defined all valid lifecycle states for every stateful entity?
- [ ] Have you documented every allowed transition and every illegal transition?
- [ ] Is each transition guarded by an `Invariant:` line attached to the relevant operation?
- [ ] Have you added `State Candidate` and `Invariant` notes to `term-registry.md` for each stateful term?
- [ ] Have you verified that domain events are emitted on all significant state transitions?
- [ ] Have you updated the class diagram to reflect state and guard information?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
