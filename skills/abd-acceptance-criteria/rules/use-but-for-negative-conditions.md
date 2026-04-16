---
scanner: negative-conditions
---

# Rule: Use BUT for negative conditions

**Priority:** (see agile_bots JSON)  
**Scanner:** `scanners/negative-conditions-scanner.py` — **`NegativeConditionsScanner`**

**Migrated from:** `agile_bots/bots/story_bot/behaviors/exploration/rules/use_but_for_negative_conditions.json`

When outcomes describe errors, validation failure, or prevention, include a **BUT** step stating what does **not** happen (e.g. does not save, does not allow).

## DO

- Add BUT when error/prevention language appears and a negative outcome needs to be explicit.

## DON'T

- Describe error outcomes without clarifying what is withheld or blocked.
