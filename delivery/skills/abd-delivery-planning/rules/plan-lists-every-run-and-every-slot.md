---
scanner: plan-shape
---

# Rule: Multi-run plans list every run and every slot — no routine templates

**Scanner:** `scanners/plan-shape-scanner.py` — rule id `plan-lists-every-run-and-every-slot`

When an engagement delivers **more than one product increment** (Runs 2–10, Increments 1–9, or equivalent), the saved plan is a **slot schedule** for the delivery lead — not a reusable pattern. Bootcamp stage files already define skill order; **`agile-delivery-plan.md`** must name **each run** and **each planned slot** (number, phase, role, skill, deliverable).

## DO

- Give **each run** its own `## Run N — …` section with goal, story scope, chain target, and waivers **for that run only**.
- Inside each run, list **Exploration**, **Specification**, and **Engineering** tables with a **`| Slot |`** column and **one row per slot** (executor and reviewer are separate rows unless the plan explicitly documents a paired-row convention used consistently in Run 1–2).
- Assign **monotonic slot numbers** across the engagement; include a **slot index** (first slot, last slot, count) when the plan spans many runs.
- When a skill is **waived** for one run, say so in **that run's header** and **omit those slot rows** — do not substitute a generic offset table.
- Tie deliverables to **increment stories** from `thin-slicing.md` (or the engagement slice doc) in the run header.

## DO NOT

- Add a **"routine template"**, **"slot pattern per increment"**, **"offset +N"**, or **"base slot = last slot + 1"** section instead of listing Runs 3–10 explicitly.
- Use **estimated** slot ranges only (`opens at slot (est.)`, `~68`, `≈ 10 slots each`) without a full slot table for that run.
- Use **`Run 5+`**, **`6+`**, or **`N+`** rows in the runs summary with **"Routine"** as the rationale instead of defining those runs.
- Copy the bootcamp **skill-order table** into the plan as if it were the PawPlace schedule — that belongs in `content/stages/`, not in lieu of slot rows.

## Example (wrong)

```markdown
## Runs 3–10 — Increments 2–9 (routine template)

| Offset | Phase | Role | Skills | Waive when |
| +0 | exploration | business-expert | abd-ubiquitous-language | no new terms |
| … | … | … | … | … |

| Run | Increment | Opens at slot (est.) | Closes at slot (est.) |
| 3 | 2 | 43 | ~68 |
```

(No slot 43, 44, 45…; no per-run Exploration/Specification/Engineering tables.)

## Example (correct)

```markdown
## Run 3 — Increment 2: Click-and-collect

**Stories:** *Add Product to Cart*, … (*thin-slicing.md*).

### Exploration

| Slot | Phase | Role | Skill(s) | Deliverable |
| 43 | exploration | business-expert | abd-ubiquitous-language | UL — cart, order, StripeWave |
| 44 | exploration | reviewer | — | Review slot 43 |
| … | … | … | … | … |
```

(Every run through Run 10 follows the same explicit shape.)
