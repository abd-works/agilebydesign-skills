# Configuration

## Required

Set `OPENAI_API_KEY` for embedding. Place it in any of:

- `<repo>/conf/.secrets`
- `<repo>/conf/.env`
- `<skill_root>/.env`
- `cwd/.env`

`_config.py` loads it automatically.

## Chunking spec

See `chunking-spec.md`. Placed beside the `--path` source folder; drafted automatically, edit before chunking runs.

## Optional (skill-config.json)

Not required for the basic pipeline. Only needed if you want to override defaults
in other tools that reference this skill.
