# Invariants in the model — payments example

**Skill:** abd-ooad — **Phase-id:** `invariants-in-the-model` (Stage 2 — Structure, p8).

**Upstream:** `relationships-and-cardinality` (p7) — associations and cardinality are confirmed.


## From spec → enforced behavior

| Rule (text) | Enforce on |
|-------------|------------|
| No double-charge for same idempotency intent | **`Payment.initiate`** — return existing aggregate or reject duplicate **successful** outcome. |
| Sanctioned country: block **before** method selection | **`ComplianceGate`** + **`Payment`** refuses `recordMethodSelection` if payer blocked (or earlier gate). |
| Partial capture only if rail supports | **`Payment.capture`** checks **connector capability** (policy/config). |
| Refund reason codes required | **`Refund.request`** — rejects missing **ReasonCode** when policy says required. |
| `payment.settled` before warehouse pick (physical) | **Event ordering** — **`Payment.settle`** emits event; fulfillment BC subscribes — invariant is **cross-BC** contract test, not one method on Payment. |
| Append-only audit | **`AuditEntry`** immutable; no `update`. |

---

## Example guard clauses (conceptual)

- `capture(amount)` — `amount ≤ authorizedRemainder`; state in `{AUTHORIZED, PARTIALLY_CAPTURED}`; rail allows partial.
- `settle()` — state allows settlement; fraud/compliance flags satisfied (if modeled).
- `requestRefund(amount)` — `sum(prior refunds) + amount ≤ captured`.

---

## Invariants and conflicts → term-registry.md

> Tag notes on the class model with `[p8]` — see `templates/domain model template.md` for the full tag table.

Every invariant and every unresolved spec conflict belongs in `term-registry.md` Notes — not only in a spec comment. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Invariant - {{rule_that_must_always_hold}}` — the enforced condition and where it lives (which operation/aggregate)
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — configurable TTLs, cross-BC rules, timing conflicts
- `Follow-up - {{question_or_action}}` — deferred invariant decisions awaiting product or architecture input

---

## Carry forward → Step 9

Watch **Payment** for bloat as more rules arrive — split policies if needed.

---


## Action Checklist

- [ ] Have you identified at least one invariant per major aggregate?
- [ ] Is each invariant expressed as a condition that must always be true, not a procedure?
- [ ] Are all invariants attached to the relevant `property` or `operation` line in the spec?
- [ ] Have you documented open decisions (e.g. configurable TTLs) where invariants are not yet fully defined?
- [ ] Have you added `Invariant` notes to `term-registry.md` for each enforced rule, and `Tension` notes for spec conflicts?
- [ ] Have you noted carry-forward items to Step 9 (watch for bloat)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
