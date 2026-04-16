---
scanner: ac-domain-crossing
---

# Rule: Keep AC consistent across connected domains

**Priority:** 2  
**Scanner:** `scanners/ac-domain-crossing-scanner.py` — **`ACDomainCrossingScanner`**

**Migrated from:** `agile_bots/bots/story_bot/behaviors/exploration/rules/keep_acceptance_criteria_consistent_across_connected_domains.json`

At small scale, AC can cover multiple domain objects. As behaviors diverge, scope AC to one domain and keep **structure** parallel across related domains. AC that mixes multiple domain behaviors signals **split the story**.

## DO

- Keep parallel structure for parallel domains (same depth and pattern).
- Split when one AC mixes distinct domain behaviors that deserve separate stories.

## DON'T

- Mix unrelated domain validations in one giant AC when at scale.
- Use inconsistent depth across connected domains without reason.
