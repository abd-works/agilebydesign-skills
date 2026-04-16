# Bootstrap contract for `abd-team-member`

## Required parameters

| Parameter | Type | Values / notes |
|-----------|------|----------------|
| `team-role` | string | `Product Owner` · `Analyst` · `Engineer` (case-insensitive OK; normalize to title case in prompts) |
| `workspace` | path | Absolute or repo-relative root where artifacts live (must contain or will contain `story-graph.json` or `docs/story/story-graph.json` for graph work) |

## What the orchestrator passes

`abd-delivery-lead` (or a human) should open a team-member turn with something like:

```text
team-role: Analyst
workspace: C:\dev\my-engagement
```

Optional: link to task brief, scope, or files.

## What the agent does first

1. Load **`AGENT.md`** + persona section in **`team-roles.md`** for `team-role`.
2. Resolve **`workspace`**; if unclear, ask once.
3. Load **practice skills** for that role (see **`AGENT.md`** table) and **common skills** (`story-graph-ops`, `execute_using_rules`, `workspace_skill`, `track_task`).
4. Execute the **Default workflow** in **`AGENT.md`**.

## Scanner `--skill-root` selection

Point `--skill-root` at the **practice skill directory** that matches the artifact you are validating, e.g.:

- Story graph quality → `skills/abd-story-mapping`
- Another practice → that skill’s root (must contain `rules/` and `scanners/` as configured)

`--workspace` is always the engagement **`workspace`** root.
