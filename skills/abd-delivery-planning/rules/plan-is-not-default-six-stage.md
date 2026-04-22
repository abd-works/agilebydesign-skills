---
scanner: plan-shape
---

# Rule: Plan is not a default single-run six-stage waterfall

**Scanner:** `scanners/plan-shape-scanner.py` — `PlanShapeScanner` (rule id `plan-is-not-default-six-stage`)

"Run all six stages start to finish" is the **degenerate case** for trivial engagements with no classified risk. Real plans decompose the work into targeted runs that flush out unknowns early, per `abd-delivery-planning` §2a–2c.

This rule flags plans that have **exactly one run** whose stages are the six canonical stages (`discovery`, `prioritization`, `exploration`, `scenarios`, `acceptance-tests`, `engineering`) in order, **unless** the plan marks itself explicitly as trivial.

## DO

- Break the work into multiple runs that front-load risk.
- Use strategies from `strategies/` as starting points — they decompose the run structure for you.
- If the engagement truly is trivial, mark it with `trivial: true` in the plan's YAML frontmatter, or add a section that states the engagement has no classified risk and explains why a single sweep is appropriate.

## DON'T

- Default to a one-run, six-stage sweep because it feels complete.
- Hide the sweep behind renamed stages (e.g. calling engineering "build" and exploration "analyze") — the scanner normalizes names.

## Example (wrong)

```markdown
| Run | Stages |
| 1 | Discovery → Prioritization → Exploration → Story Definition → Acceptance Tests → Engineering |
```

(Single run, canonical six, no trivial flag, non-empty risks. This is the default-sweep shape.)

## Example (correct — non-trivial decomposition)

```markdown
| Run | Stages |
| 1 | Discovery → Prioritization |
| 2 | Exploration → Engineering |  (first thin slice)
| 3 | Exploration → Engineering |  (second slice)
| 4 | Discovery                 |  (fill-in deferred map)
```

## Example (correct — truly trivial engagement)

```markdown
---
trivial: true
---

# Agile Delivery Plan
Engagement is a five-story internal tool, no classified risks beyond value.

| Run | Stages |
| 1 | Discovery → Prioritization → Exploration → Story Definition → Acceptance Tests → Engineering |
```
