Follow this page when you work **on** this skill (pipeline order, artifacts, flags). Keep user-facing triggers and commands in `**SKILL.md`**. Use `**content/parts/library/`** for YAML shape, CLI detail, and search (see the table at the end).

---

## Pipeline process

Run **convert → (assess markdown structure) → draft spec → chunk → embed** in that order. Orchestrate with `index_memory.py --path <source_folder>` from a cwd where paths resolve (scripts: `skills/abd-context-to-memory/scripts/`). Full command matrices: [script-invocation.md](library/script-invocation.md).

### 1. Convert to Markdown

**Convert** sources to Markdown with the core converter: it walks the formats it understands (PDF, Office, and the rest listed under Supported inputs below) and writes `.md` files under `markdown/`, keeping roughly the same folders and names as the originals.

**Run post-processors** after extraction where the built-ins apply (e.g. PDF banner cleanup and optional outline alignment). They stay **generic**. If the result still lacks **real sections or subsections**, **choose** the next fix: optional deps (e.g. PyMuPDF), env flags, or a **bespoke** script under `<topic_root>/scripts/`—not silent hope.

**Shape the manuscript during conversion** (`pdf_markdown_post`, MarkItDown options, bespoke `<topic_root>/scripts/`): real headings, sensible sections, GFM tables, deduped running headers. **Cut** with the chunker only along boundaries the markdown and spec already expose; it does not rebuild hierarchy from a wall of text. See chunking-spec.md (*Chunker vs converter*).

**Full convert story** (assess headings, report to the human when bad, bespoke loop): **[library/convert-to-markdown.md](library/convert-to-markdown.md)**. PDF specifics: [library/pdf-extraction-advanced.md](library/pdf-extraction-advanced.md).

For command names and options, see [script-invocation.md](library/script-invocation.md). For what appears on disk, see [output.md](library/output.md).

### 1b. Assess structure 

Check whether Markdown has **headings and subheadings** where you need them. Use a quick skim of `markdown/*.md`, `**markdown/structural_scan_report.txt`** from `draft_chunking_spec.py`, or both.

- **If structure is bad:** Tell the user, suggest either a **new bespoke post-processor** in `<topic_root>/scripts/` or a **different existing** option (e.g. outline pass). **Create it, run it, report results, repeat** until good enough or a blocker needs a human call.
- **If it is still a wall of text or mixed topics** after fixes: run an **AI semantic pass** — group sentences by meaning, identify **topics** / **sub-topics**, add headings or a cleaned markdown file, **complete the pass**, then **re-review** before drafting the spec. See [library/convert-to-markdown.md](library/convert-to-markdown.md) (*Last resort*).
- **If structure is OK:** Continue to draft spec (or use existing YAML) and chunk.


#### Corpus preprocess scripts (`<topic_root>/scripts/`)

When the **Markdown** still needs **code** to become chunkable—not just YAML edits—add **corpus-only** scripts under `**<source_folder>/scripts/`** (topic root: same folder as `markdown/` and `memory/`; the chunking spec lives **inside** `memory/`). Do **not** put that logic in `skills/abd-context-to-memory/scripts/`; those files are the shared **convert → draft spec → chunk → embed** pipeline for every project.


| Topic          | Guidance                                                                                                                                        |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Why**        | PDF/Office exports often lack real headings, repeat running headers, or need deduping before `split_on_heading_level` or regex boundaries work. |
| **Where**      | `<topic_root>/scripts/` — versioned with the corpus you pass to `--path`, not inside the skill repo.                                            |
| **Naming**     | Descriptive stems: `prepare_handbook_for_chunking.py`, `dedupe_chapter_headers.py`, etc.                                                        |
| **Docs**       | Docstring at top of script; one-line pointer in `context_chunking_spec.yaml` comments; optional `scripts/README.md` (usage, `--dry-run`).       |
| **Backups**    | Optional `archive/` under the topic root for a frozen copy before rewriting `markdown/*.md`.                                                    |
| **Chunk scan** | Use `chunk_inputs` in the spec if backups, notes, or duplicates would otherwise be picked up as separate logical docs.                          |
| **Tree**       | Full folder layout (including `scripts/`, `archive/`) → [output.md](library/output.md).                                                         |



### 2. Structural reports + draft chunking spec

**Structural scan** (heading/table metrics) is written to `**markdown/structural_scan_report.*`** — it describes how **converted** markdown looks, not retrieval chunks. Fix conversion until those reports look good.

**Drafted chunking spec** goes to `**memory/context_chunking_spec.yaml`** — rules for splitting into `**memory/**` chunk files. It is skipped on re-runs if a spec already exists (unless `--force`). What each YAML section means is in [chunking-spec.md](library/chunking-spec.md). Layout: [output.md](library/output.md).

### 3. Chunk

The Markdown is cut into smaller files under `memory/` (alongside `**memory/context_chunking_spec.yaml**` when drafted). Decks tend to become one file per slide; long pages split at headings; short pieces may stay one file. If `memory/context_chunking_spec.yaml` is present (or legacy YAML at topic root), the chunker follows it and adds front matter to each piece. If not, it uses simple defaults. Naming patterns and examples are in [output.md](library/output.md); behavior with and without a spec is in [chunking-spec.md](library/chunking-spec.md).

**Agent obligation (quality loop):** After chunking, **check** how many chunks were written and whether splits match the document (e.g. one file for an entire book means boundaries or headings failed). **Do not** tell the user “fix the spec yourself” as the first response. **Automatically** adjust preprocessing (e.g. inject `##` chapter headings when PDF export only repeated `CHAPTER N:` in running headers), **edit** `context_chunking_spec.yaml` (regexes, `split_on_heading_level`, optional `chunk_inputs` to ignore backups), **re-run** chunking, and **re-verify**. Repeat until the result is sane or a true blocker needs a human decision.

### 4. Embed

Each chunk is passed through an embedding model. The vectors are stored in a FAISS index on disk under **your** `<source_folder>/memory/rag/` (whatever path you passed to the pipeline)—not under the skill directory. API keys, env vars, and setup are in [config.md](library/config.md). How the index is built and used is in [rag-retrieval.md](library/rag-retrieval.md).

### 5. Search

You ask a question (or paste a query). The search step compares it to the stored vectors and returns the chunks that match best in meaning, not just keywords. How to run search and what to expect is in [rag-retrieval.md](library/rag-retrieval.md).

---

## Strategy: ask once

If the user asks to convert, chunk, ingest, or refresh and **does not** mention strategy, **ask once**: **strategy pass** (review or edit `context_chunking_spec.yaml` before chunk + embed) vs **straight through** (single `index_memory.py` run does everything in one go). Do **not** silently assume straight-through. Rationale ties to [chunking-spec.md](library/chunking-spec.md).

### Pause before chunking


|                        |                                                                                                                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What the tool does** | A full `index_memory.py` run drafts the spec when needed, then **continues** in the same process: chunk → embed. It does **not** wait for you.                                                                                                                 |
| **What you should do** | Unless the user explicitly chose **straight through**, **pause** after the draft: review or edit `memory/context_chunking_spec.yaml` before treating chunk output as final. To chunk only **after** YAML is ready (and skip re-drafting), use the steps below. |


To edit YAML before relying on new chunk files, run convert and draft only, edit `context_chunking_spec.yaml`, then resume with `--skip-convert --skip-spec` (drafting is skipped; an existing spec is still **loaded** for chunking):

```bash
python scripts/convert_to_markdown.py --memory <source_folder>
python scripts/draft_chunking_spec.py --path <source_folder>
# markdown/structural_scan_report.*  then  memory/context_chunking_spec.yaml when first drafted
# edit memory/context_chunking_spec.yaml
python scripts/index_memory.py --path <source_folder> --skip-convert --skip-spec
```

---

## Common `index_memory.py` flags


| Flag                         | Effect                                             |
| ---------------------------- | -------------------------------------------------- |
| `--path <folder>`            | Required source root                               |
| `--skip-convert`             | Use existing `markdown/`                           |
| `--skip-spec`                | Do not re-draft spec; use existing YAML if present |
| `--skip-convert --skip-spec` | Chunk + embed from existing markdown + spec        |
| `--rebuild`                  | Rebuild FAISS from existing chunks                 |


More options and other scripts: [script-invocation.md](library/script-invocation.md).

---

## Supported inputs

`.pdf`, `.pptx`, `.docx`, `.xlsx`, `.xls`, `.html`, `.htm`, `.txt`, `.csv`, `.json`, `.xml`

---

## When something fails

- Bad path → errors from convert or chunk; unsupported types skipped where possible.
- Embed/search → needs API key and deps per [config.md](library/config.md).
- Broken YAML → warning; chunking may fall back—see [chunking-spec.md](library/chunking-spec.md).

---

## Reference map (`content/parts/library/`)


| Topic                                                     | File                                                             |
| --------------------------------------------------------- | ---------------------------------------------------------------- |
| **Convert → assess headings → bespoke post-process loop** | [convert-to-markdown.md](library/convert-to-markdown.md)         |
| Artifact tree, chunk names, front matter                  | [output.md](library/output.md)                                   |
| `context_chunking_spec.yaml`                              | [chunking-spec.md](library/chunking-spec.md)                     |
| Script CLI                                                | [script-invocation.md](library/script-invocation.md)             |
| Keys, env                                                 | [config.md](library/config.md)                                   |
| Semantic search                                           | [rag-retrieval.md](library/rag-retrieval.md)                     |
| PDF outlines vs built-in post-process                     | [pdf-extraction-advanced.md](library/pdf-extraction-advanced.md) |
| Index of all shards                                       | [README.md](library/README.md)                                   |


---

## Agent rules

1. **Taxonomy** — `draft_chunking_spec.py` leaves taxonomy lists empty until a human or AI fills them from the **actual** corpus ([chunking-spec.md](library/chunking-spec.md)).
2. **Labels** — Prefer `chunk_type` in specs; `modeling_kind` in defaults is a legacy alias in code.
3. **Scope** — Single file: `convert_to_markdown.py --file`. Folder/project: `index_memory.py --path <folder>` or `index_memory.py` with `**CONTENT_MEMORY_ROOT`** or **cwd** as the topic root ([config.md](library/config.md)).
4. **Corpus preprocess scripts** — See the subsection **Corpus preprocess scripts (`<topic_root>/scripts/`)** under Pipeline process earlier in this file, and the folder tree in [output.md](library/output.md).

## Running scripts

Use `**CONTENT_MEMORY_ROOT`**, `**--path**`, or `**cd**` to the corpus — see [config.md](library/config.md). Typical:

`python skills/abd-context-to-memory/scripts/index_memory.py --path <source_folder>`

or, after `export CONTENT_MEMORY_ROOT=...` or `cd` to the corpus:

`python skills/abd-context-to-memory/scripts/index_memory.py`

## Editing this skill

Change `**content/parts/process.md**` and/or `**content/parts/library/*.md**`, then `**python scripts/build.py**` to refresh `**AGENTS.md**`. Keep `**SKILL.md**` as the short entry; update script docstrings when behavior changes.

## Tests / quality

After substantive script changes, run a smoke path on a small folder (convert → spec → chunk → embed) when feasible.