---
scanner: behavioral-ac
---

# Rule: Behavioral AC at story level

**Priority:** 4  
**Scanner:** `scanners/behavioral-ac-scanner.py` — **`BehavioralACScanner`** (policy / intent; mechanical pass is currently a no-op in agile_bots — migrated as-is)

**Migrated from:** `agile_bots/bots/story_bot/behaviors/exploration/rules/behavioral_ac_at_story_level.json`

Behavioral AC belongs at story level in `story-graph.json`. Use When/Then format (**no Given** in AC — reserve Given for scenarios). AC should describe behavioral outcomes, not technical implementation.

## DO

- Use behavioral language for user actions and system responses.
- Focus on observable outcomes and system responses.
- WHEN/THEN/AND may appear as separate lines in structured AC entries.

## DON'T

- Use technical implementation terms (config, json, api, sql, class, method) as the primary description.
- Use programming, database, or raw API terminology in place of behavior.
