# Delivery package

Consolidated **delivery lead**, **team member (executor)**, **team reviewer**, shared **stages** and **roles**, delivery **skills**, and flow **instructions/prompts**.

**Canonical source:** edit `delivery/content/` only — not copied under `agents/` or `skills/`.

## Deploy layout (engagement workspace)

| `--ide` | Target | Shared content |
| --- | --- | --- |
| `cursor` (default) | `.cursor/` | `.cursor/content/` only |
| `vscode` | `.github/` | `.github/content/` only |
| `both` | both | one `content/` per tree |

```text
<workspace>/.cursor/
  agents/          delivery-lead, delivery-team-member, delivery-team-reviewer
  skills/          abd-delivery-planning, abd-delivery-war-room, delivery-estimation
  content/         stages/, roles/  (single copy)
  rules/
  commands/
```

## Path conventions (after deploy)

| From | To stages / roles |
| --- | --- |
| `.cursor/agents/<name>/` | `../../content/stages/`, `../../content/roles/` |
| `.cursor/skills/<skill>/` | `../../content/...` |
| `.cursor/skills/<skill>/{rules,strategies,templates}/` | `../../../content/...` |
| Cross-folder skills from agents | `../skills/...` |

Same relative paths resolve in the source `delivery/` package during editing.

## Deploy

```bash
python scripts/deploy_family_package.py --package delivery --to C:\dev\abd-pet-store-demo
```

Or deploy everything (all family packages + standalone skills):

```powershell
& scripts/deploy-skills.ps1 -Force
```
