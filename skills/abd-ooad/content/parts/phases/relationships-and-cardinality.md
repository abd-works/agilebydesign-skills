# Relationships and cardinality — payments example

**Skill:** abd-ooad — **Phase-id:** `relationships-and-cardinality` (Stage 2 — Structure, p7).

**Upstream:** `properties-and-operations` (p6) — every surviving class has typed properties and operations.

Use ASCII glyphs from **`SKILL.md` → ASCII class diagrams — notation** (`----|>`, `..|>`, `*---`, `o---`, `- - ->`).

---

## Narrative relationships

- **Order** (external BC) **1 — 0..*** **Payment** — retry / multiple attempts possible for same order (idempotency distinguishes “same” vs new attempt).
- **Payment** **1 — 0..*** **Refund** — several partial refunds over time.
- **Payment** **1 — 1..*** **AuditEntry** (or events) — every transition logged (append-only).
- **Merchant** (ref) **1 — *** **Payment** — many payments per merchant (via `merchantRef`).
- **Payer** (ref) **1 — *** **Payment**.

---

## Composition vs association

| End | Strength | Rationale |
|-----|------------|-----------|
| **Payment** *—* **FeeBreakdown** / **Money** snapshots | **Composition** (VO inside aggregate) | No standalone “fee” entity; dies with payment context for that attempt. |
| **Payment** — **Refund** | **Association** (strong ref) | Refund has identity; may be queried independently; lifecycle linked but not embedded value. |
| **Payment** — **Order** | **Association** (id only) | Order lives elsewhere. |

---

## ASCII sketch

```
<<external>>
Order
  1 ------------------ * Payment
                           |
                           | 1
                           *
                        Refund

Payment *-------- AuditEntry    (or events *-------- projection)
  (append-only facts; composition if AuditEntry only exists as child row)
```

**Dependency** (dashed):

```
PaymentOrchestrator - - - -> ComplianceGate
PaymentOrchestrator - - - -> PspAdapter
```

---

## Carry forward → Step 8

Encode **invariants** on **Payment** / **Refund** operations (sanctions, partial capture, settlement before fulfillment consumers).

---

## Relationship decisions → term-registry.md

> Tag notes on the class model with `[p7]` — see `templates/domain model template.md` for the full tag table.

Every cross-BC reference and significant relationship resolved or deferred in this phase belongs in `term-registry.md` Notes. Use Notes labels (see **`library/term-capture`** for the full label list).

Common Notes labels added at this phase:

- `Classified - {{kind}} {{reason}}` — when a term's relationship to another class is confirmed (composition, reference, association)
- `Tension - **{{TensionName}}** {{what_is_ambiguous_or_conflicting}}` — when ownership or boundary between two aggregates is unclear
- `Follow-up - {{question_or_action}}` — deferred cardinality or ownership decisions

**Cross-BC references (e.g., `OrderId`, `PayerId`) must have a term row confirming they are references, not embedded aggregates.**

---


## Action Checklist

- [ ] Have you defined the relationship type (composition, aggregation, association, dependency) for every pair?
- [ ] Have you recorded cardinality (1..1, 1..*, 0..*) for each relationship?
- [ ] Have you verified that composition correctly models ownership and lifecycle dependency?
- [ ] Have you updated the class diagram with all relationships and cardinalities?
- [ ] Have you updated `term-registry.md` with `Classified` notes for resolved relationships and `Tension` notes for any unclear cross-BC ownership?
- [ ] Have you noted carry-forward items to Step 8 (invariants)?

---

## Prompt

> **Validate and fix when you find problems.** This step may surface bloat, unclear boundaries, missing invariants, naming drift, spec conflicts, or other robustness gaps. When you notice any of that in your work, **validate** and **fix** the model (or **map-model-spec.json** / class diagram) **before** moving on; record **explicit debt** only when you cannot fix yet, with a clear follow-up.
