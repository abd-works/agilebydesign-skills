# AGENTS — abd-context-to-memory

## Purpose

Convert office documents (PDF, PPTX, DOCX, XLSX, etc.) to **Markdown** with a **core converter** plus **shared post-processors** where needed. Then **check** whether you got real **headings and subheadings**; if not, **tell the user**, suggest a **bespoke post-processor** under `<topic_root>/scripts/` or another fix, **run it**, and **repeat**. If the text is still a **semantic mess**, use an **AI pass** to group sentences by topic, name **sub-topics**, add structure, **finish the pass**, and **review again** before chunking.

After that: draft a **structure-based chunking spec** (`context_chunking_spec.yaml`), **chunk** into `memory/` with evidence labels when a spec exists, and **embed** into a local **FAISS** index for semantic search. Support an explicit **strategy pass** (review/edit the YAML before chunk+embed) when quality matters more than one-shot throughput.

Full pipeline order and commands: **[process.md](../process.md)**. Convert step detail: **[convert-to-markdown.md](convert-to-markdown.md)**.


---

## Outline

**How it works** (each step is distinct; order matters):

- **Convert** supported sources to Markdown (under `markdown/` in the source tree).
- **Draft** a structure-aware chunking spec: `context_chunking_spec.yaml` (boundaries, splitting, taxonomy for *this* corpus).
- **Strategy pass (optional but important when quality beats speed):** review or edit that YAML *before* chunking and embedding so splits and labels match the material.
- **Chunk** Markdown into `memory/`; when the spec applies, chunks get front matter such as `evidence_type` and `chunk_type`.
- **Embed** chunk vectors into a **local FAISS** index next to your source tree (e.g. `<source_folder>/memory/rag/`—you choose the corpus folder).
- **Search** semantically over what you embedded (e.g. via the project’s search script), not just keyword grep.

**Where to read more:** **`SKILL.md`** (activation and short commands), **`content/parts/process.md`** (full pipeline, flags, examples), **`content/parts/library/`** (chunking YAML detail, script CLI, artifact layout, RAG behavior).


---

## Role

You are an expert in **extracting context** from messy source material—structure, intent, and evidence—not just transcribing text; in **semantic chunking** (where ideas start and end so retrieval stays coherent); and in **memory that is built for search**, so boundaries and labels match how people will question the corpus later.

You have knowledge in **structure-based chunking specs** (`context_chunking_spec.yaml`), **evidence and chunk taxonomy** (`evidence_type`, `chunk_type`) as corpus-specific choices, **office-to-Markdown conversion**, **FAISS embedding and semantic search**, and when a **strategy pass** (review YAML before chunk+embed) is worth the pause.

You help with **running and explaining** the **abd-context-to-memory** flow—convert → draft spec → chunk → embed → search—**interpreting** whether splits respect meaning, **guiding** strategy-pass vs straight-through, and **grounding** commands in **`SKILL.md`**, the full **Pipeline process** in **`content/parts/process.md`**, and reference material in **`content/parts/library/`**. Run **`scripts/`** from a shell where **`CONTENT_MEMORY_ROOT`**, **`--path`**, or **cwd** points at the corpus so paths resolve. If the user asks to ingest or refresh and **does not** mention strategy, **ask once**: strategy pass vs straight-through—do not assume silently.


---

## Process

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
## Reference documentation

### `convert-to-markdown.md`

# Convert to Markdown (core converter + post-process + quality loop)

This page is the **convert** step in the full pipeline. The **whole chain** (convert → assess structure → spec → chunk → embed, flags, strategy pass) lives in **[process.md](../process.md)**—read that for order and commands.

**Principle:** **Structural composition and decomposition**—chapters, sections, tables you can split on—belong in **conversion and markdown post-process** (`pdf_markdown_post`, corpus scripts). The **chunker** only cuts along boundaries already present in the files; it does not rebuild hierarchy. See [chunking-spec.md](chunking-spec.md) (*Chunker vs converter*).

---

## What happens on disk

1. **Core markdown converter** — `convert_to_markdown.py` uses MarkItDown (and format-specific paths for Office XML, PPTX charts, etc.) to turn each supported source into a `.md` file under **`markdown/`**, mirroring paths and names. Details: [output.md](output.md).

2. **Built-in post-processors** — After extraction, **PDFs** (and only PDFs in the default tool) pass through shared cleanup in `pdf_markdown_post` (banner collapse, conservative `CHAPTER` / `APPENDIX` / `PART` line promotion, optional outline alignment when **PyMuPDF** is installed). That is **not** guaranteed to fix every book; it is generic. Deep dive: [pdf-extraction-advanced.md](pdf-extraction-advanced.md).

---

## After convert: assess headings and subheadings

**Goal:** Chunking and RAG work best when the markdown has real **sections** (headings), not a flat wall of text.

**Agents and humans should check:**

- Does the file have **`#` / `##` / `###`** (or enough structure) where the source had chapters or sections?
- Run or inspect **`draft_chunking_spec.py`** output (or open **`markdown/structural_scan_report.txt`**) — it reports heading counts and hints (e.g. chapter-like patterns vs noise).

**If structure looks bad** (few or no headings, wrong breaks, no subsections where you expect them):

1. **Tell the user clearly** what failed (e.g. “almost no `##`, chunking will be poor”).
2. **Suggest a fix path:**
   - **Turn on or add** something that already exists: e.g. install **PyMuPDF** for PDF outline injection, adjust env flags (`PDF_SKIP_*`) documented in [pdf-extraction-advanced.md](pdf-extraction-advanced.md), or re-export the source with better tags.
   - **Or** add a **bespoke post-processor** — a script under **`<topic_root>/scripts/post-processors`** that rewrites `markdown/*.md` for *this* corpus and potentially other of te same type (see below).

3. **Implement, run, repeat:** Add or change the bespoke script, run it on `markdown/`, re-check headings (and re-run structural scan if needed). **Repeat** until structure is good enough to chunk, or until you hit a limit and need a human decision.

**Choosing “which post-processor”:** The **agent** should pick the most likely improvement when the default pipeline is not enough—e.g. outline pass if the PDF has bookmarks; regex or scripted fixes if the problem is a known pattern; **not** one-size-fits-all hacks in the shared skill for a single publisher.

---

## Last resort: the source is still a mess (semantic / topic pass)

Sometimes the extract stays **unusable for heading-based chunking**: one long stream of text, headings missing or wrong, or topics **mixed in one block**. Regex and bespoke layout fixes are not enough.

**Then run an AI-led semantic pass** (not a fixed script in the skill—**judgment** in chat or a corpus-specific tool you control):

1. **Read** the markdown in meaningful slices (or the whole file if size allows).
2. **Decide what belongs together** — which sentences and paragraphs form one **topic**; whether a topic should split into **sub-topics**.
3. **Materialize structure** — e.g. inject `##` / `###` titles that match *meaning*, add blank-line breaks between units, or write a **cleaner parallel file** under `markdown/` (keep a backup of the raw extract).
4. **Complete one full pass**, then **look at the results again**: coherence, missing boundaries, wrong merges. **Iterate** until sections reflect topics well enough to draft a spec and chunk.

Only after this should you rely on `draft_chunking_spec.py` and heading-driven splits. For taxonomy and chunk labels after semantic restructuring, see [chunking-spec.md](chunking-spec.md).

---

## Bespoke post-processors (corpus scripts)

Shared skill code stays generic. Anything **book- or publisher-specific** belongs in:

**`<topic_root>/scripts/`** — same folder as `markdown/` and `memory/` (the chunking spec lives **inside** `memory/context_chunking_spec.yaml`).

Name scripts clearly (`prepare_handbook_headings.py`, …), document usage in the script docstring, and optionally point to them from comments in `context_chunking_spec.yaml`. More convention: [process.md](../process.md) (section *Corpus preprocess scripts*).

---

## Where this fits in the full pipeline

| Step | What |
|------|------|
| **1 — Convert** | This page + `convert_to_markdown.py` |
| **2 — Assess** | Headings / structural scan / human skim |
| **3 — Fix loop** | Bespoke script or different built-in options; re-run until good |
| **3b — Semantic pass (optional)** | If still a mess: AI groups sentences by topic, names sub-topics, injects structure; **re-review** output before spec |
| **4 — Draft spec** | `draft_chunking_spec.py` → `markdown/structural_scan_report.*` + `memory/context_chunking_spec.yaml` |
| **5 — Chunk** | `chunk_markdown.py` |
| **6 — Embed** | `embed_and_index.py` |

Orchestrated one-shot: **`index_memory.py --path <source_folder>`** — see [process.md](../process.md).

CLI flags for convert only: [script-invocation.md](script-invocation.md).


---

### `config.md`

# Configuration

## Topic root (where memory lives)

There is **no** persisted “workspace” in this skill. Scripts resolve a **topic root** (`ROOT` in `_config.py`) in this order:

1. **`CONTENT_MEMORY_ROOT`** — environment variable (automation / CI / one place to point all commands at a corpus).
2. **Current working directory** — if the env var is unset.

**Per-run override:** pass **`--path`** (or `--rag` / `--memory` where documented) so the corpus folder is explicit; that wins over defaults.

If the user has **not** said where the corpus lives and **has not** set `CONTENT_MEMORY_ROOT`, **ask** which folder holds the documents (or confirm **cwd**) **before** converting—do not silently treat an arbitrary shell cwd as the corpus. Same rule applies whenever generic “workspace” instructions would have applied: substitute this **topic root** guidance instead.

**`index_memory.py`**, **`draft_chunking_spec.py`**, **`embed_and_index.py`**, and **`search_memory.py`** use `ROOT` when flags are omitted; embed/search use `<ROOT>/memory` and `<ROOT>/memory/rag` by default.

Markdown, `context_chunking_spec.yaml`, `memory/`, and `memory/rag/` are created **under that topic folder**—not inside the skill package.

## Where embeddings go

Embedding writes under **`<topic_folder>/memory/rag/`** when you pass `--path <topic_folder>` to `index_memory.py`, or under **`<ROOT>/memory/rag/`** when you rely on the defaults above. The skill package does not hold corpus data; each project keeps its own index beside its content.

## Required

Set `OPENAI_API_KEY` for embedding. Place it in any of:

- `<repo>/conf/.secrets`
- `<repo>/conf/.env`
- `<skill_root>/.env`
- `cwd/.env`

`_config.py` loads it automatically.


---

### `chunking-spec.md`

# Chunking spec (`context_chunking_spec.yaml`)

## Chunker vs converter

Separate three jobs—conversion, drafting the spec, and chunking—so you do not blame the chunker for bad markdown or a bad spec.

**Convert sources to navigable markdown.** Use the **core converter**, shared **post-processors** such as `pdf_markdown_post`, and **corpus-specific scripts** under the topic’s `scripts/` when the default pipeline is not enough. Aim for real headings, sections that match the book, intact tables, and less PDF noise (running headers, page junk).

**Draft the chunking spec (`draft_chunking_spec.py`).** Read structural signals in the markdown (headings, tables, patterns) and **write a first draft** of `context_chunking_spec.yaml` so you are not hand-authoring YAML from zero. Treat it as a starting point, not a repair pass for broken conversion.

**Chunk the markdown (`chunk_markdown.py`).** Cut files to your size rules and the boundaries in the spec—`section_boundaries`, heading levels, `max_chunk_chars`, and the rest. The tool only follows structure the markdown and spec already expose; it does not infer meaning from a wall of text.

**Fix markdown and spec settings when boundaries are wrong.** Adjust structure and noise in the markdown and the regexes or fields in `context_chunking_spec.yaml`; do not wait for a “smarter chunker” to invent hierarchy.

---

## Where the spec lives

- **Canonical:** `memory/context_chunking_spec.yaml`
- **`chunk_markdown.py`** reads `section_boundaries`, `splitting`, and `defaults` for splitting and YAML front matter.
- **`taxonomy`** documents corpus-specific labels (AI- or human-authored); the emitter may warn if `defaults` omit labels while taxonomy lists are non-empty.

**`chunk_inputs`** (optional): topic-relative paths, e.g. `["markdown/Book.md"]`. When set, **only** those files are chunked—useful when the folder also has backups, notes, or duplicate stems. Without it, the chunker scans all `.md` under the topic root (see `chunk_markdown.py`).

**Corpus preprocess:** If markdown must be **reformatted using additional code processors** before boundaries work, look in **`<topic_root>/scripts/`** (not the skill’s `scripts/`). Details → [../process.md](../process.md) (*Corpus preprocess scripts*).

If no spec exists, chunking uses built-in heuristics and chunks may get `<!-- Source: … -->` instead of full YAML front matter (unless implemented otherwise).

---

## Minimum shape (example)

```yaml
# Optional: restrict chunking to specific markdown files (POSIX paths from topic root).
chunk_inputs: ["markdown/PrimarySource.md"]

section_boundaries:
  chapter_break_regex: "^CHAPTER\\s+\\d+"
  section_break_regex: "^##\\s+"
  all_caps_standalone: true

splitting:
  min_chunk_chars: 400
  max_chunk_chars: 8000
  keep_markdown_tables_intact: true
  split_on_heading_level: 2

defaults:
  evidence_type: mixed
  chunk_type: prose_block

taxonomy:
  evidence_type: []
  chunk_type: []
```

The chunk spec script drafter leaves **`taxonomy`** empty by design. After you classify the source, fill `evidence_type` and `chunk_type` lists and set  in `defaults` (the chunker may still accept `modeling_kind` as an alias for one release path).

---

## Sections (reference)

| Section | Purpose |
|---------|---------|
| `chunk_inputs` | Optional allow-list of topic-relative `.md` paths; if omitted, all eligible markdown under the topic is considered |
| `section_boundaries` | Regexes that start a new major unit; informs where splits are meaningful |
| `splitting` | Size limits, heading level for splits, `keep_markdown_tables_intact` (logged by chunker; valid pipe tables are still fixed in **convert**—chunker only splits at headings/markers) |
| `defaults` | Fallback `evidence_type` / `chunk_type` on each chunk’s front matter |
| `taxonomy` | Allowed labels for *this* corpus—filled by you after reading the source, not a global enum in tooling |

---

## `evidence_type` vs `chunk_type`

Two axes on each chunk when a spec is active (from `defaults` until you add finer labeling):

| Axis | Question | Examples |
|------|----------|----------|
| `evidence_type` | What does this chunk look like as exported text? (form) | `prose`, `table`, `list`, `mixed`, `metadata_noise` |
| `chunk_type` | What **role or structure** in *this* manuscript? | Corpus-specific: `chapter`, `archetype_sheet`, `stat_block`, `powers`, `toc_or_index`, … |

They diverge when form and role differ (e.g. `evidence_type: table`, `chunk_type: stat_block`).

---

## Why review the YAML? (`draft_chunking_spec.py` is a guess)

**Problem:** `draft_chunking_spec.py` infers patterns from headings, tables, slides, and noise heuristics. Odd layouts, mixed templates, or PDF junk can yield **wrong regexes** or **empty/wrong taxonomy** → poor splits and weak labels → bad retrieval.

**Passes:**

| Pass | Who | What happens |
|------|-----|----------------|
| **1 — Structural (automatic)** | Scripts | Convert → `draft_chunking_spec.py` writes **`markdown/structural_scan_report.*`** and drafts **`memory/context_chunking_spec.yaml`** when no spec exists yet (same scan drives both; console shows the structural scan). |
| **2 — Strategy (human + AI)** | You | Compare the draft to real `markdown/` files. Adjust boundary regexes, table/list handling, noise vs signal, fill **`taxonomy`**, tune **`defaults`**. |

---

## When to pause (two events)

The pipeline **does not** insert a mandatory stop in code. **You** choose when to pause. Default expectation: **pause for strategy** unless the user explicitly asked for a single straight-through run (see [../process.md](../process.md) — *Strategy: ask once*).

### Event A — After the spec is drafted, before you trust chunks

| | |
|--|--|
| **What the tool does** | A full `index_memory.py` run **drafts** the spec (when needed), then **continues in the same process**: chunk → embed. It does **not** wait for you. |
| **What you should do** | **Pause** after the draft exists: open and edit `memory/context_chunking_spec.yaml` (and rely on the structural report) **before** treating `memory/` chunk files as final. To avoid chunking until YAML is ready, use the **split workflow** in [../process.md](../process.md): convert + draft only → edit YAML → `index_memory.py --skip-convert --skip-spec`. |
| **What the user does** | Chooses **strategy pass** vs **straight through** when asked; if strategy pass, expects a review step before embeddings are treated as production-ready. |

### Event B — Chunk output looks wrong (splits, sizes, counts)

| | |
|--|--|
| **What went wrong** | Examples: split mid-table, wrong sections, **one giant chunk**, **absurd split counts**. |
| **What you should do** | **Pause**—do **not** hand off or declare success. **Edit** the spec and/or **preprocess** markdown (inject headings, dedupe running headers, fix regexes). Set **`chunk_inputs`** if extra `.md` files pollute the scan. **Re-run** `chunk_markdown.py` or `index_memory.py --skip-convert --skip-spec`. **Verify** chunk count and spot-check files. **Repeat** until boundaries and sizes look right, then involve the user. |
| **What the user does** | Gets a corpus that is actually retrievable—not a first-cut disaster—because you stopped and fixed instead of shipping bad chunks. |

### Event C — Markdown is semantically messy (no trustworthy headings)

| | |
|--|--|
| **What you should do** | **Before** relying only on regex tweaks, run an **AI semantic pass**: infer what belongs together, name topics and sub-topics, inject structure or a cleaned file, **finish one full pass**, then review and iterate. See [convert-to-markdown.md](convert-to-markdown.md) (*Last resort: semantic / topic pass*). |
| **Rule** | The chunker follows **structure you give it**; it does not replace reading for meaning. |

```bash
python scripts/index_memory.py --path <source_folder> --skip-convert --skip-spec
```

Use `--rebuild` when only embeddings must refresh from existing chunks.

---

## Before the user trusts chunked output — checklist

| Topic | You check |
|-------|-----------|
| **Boundaries** | Do `section_boundaries` regexes match real chapter/section breaks? False positives? |
| **Tables / lists** | Should tables stay intact? Templates that need their own rule? |
| **Noise** | ToC, headers, license blocks—exclude or tag (`metadata_noise`, etc.)? |
| **Taxonomy** | Did you fill `evidence_type` / `chunk_type` from **this** source (not a generic list)? |
| **Defaults** | Do defaults match “most chunks” until you relabel? |

**Tell the user** what was inferred from structure vs what still needs eyeballing on the real markdown.

---

## Workflow (ordered)

1. **You** run `draft_chunking_spec.py --path <source>` (or a full `index_memory` once, then **pause**—see Event A). Outputs include **`markdown/structural_scan_report.*`** and **`memory/context_chunking_spec.yaml`** when new.
2. **You** review and edit `context_chunking_spec.yaml` (especially taxonomy and boundaries).
3. **You** run `index_memory.py --path <source> --skip-convert --skip-spec` when the spec is ready (`--skip-spec` skips **re-drafting**; an existing file is **loaded** for chunking).

Full command matrices and strategy vs straight-through: [../process.md](../process.md) and [script-invocation.md](script-invocation.md).


---

### `script-invocation.md`

# Script Invocation

Run from your **topic folder** (or set **`CONTENT_MEMORY_ROOT`**). All paths are **yours**: pass the folder where your documents (and later `markdown/`, `memory/`, `memory/rag/`) live—nothing in these commands assumes a central store inside the skill package.

## index_memory.py

Full pipeline: convert → draft spec → chunk → embed.

```bash
python scripts/index_memory.py --path <source_folder>
python scripts/index_memory.py --path <source_folder> --skip-convert
python scripts/index_memory.py --path <source_folder> --skip-spec
python scripts/index_memory.py --path <source_folder> --skip-convert --skip-spec
python scripts/index_memory.py --path <source_folder> --rebuild
```

- `--path`: Source folder of documents.
- `--skip-convert`: Markdown already exists; skip convert step.
- `--skip-spec`: Skip spec draft step (use existing `context_chunking_spec.yaml` or no spec).
- `--rebuild`: Rebuild the FAISS index from existing chunks.

## draft_chunking_spec.py

Structural scan of markdown sources → draft `context_chunking_spec.yaml`.

```bash
python scripts/draft_chunking_spec.py --path <source_folder>
python scripts/draft_chunking_spec.py --path <source_folder> --force
```

- `--path`: Folder containing `markdown/` (or markdown files directly).
- `--force`: Overwrite an existing spec. Default: skip if already present.

Prints a structural report and **always writes the same text** to **`structural_scan_report.txt`** beside the source folder. Writes **`context_chunking_spec.yaml`** there too. **Review and edit the spec before running chunk_markdown.py.**

## convert_to_markdown.py

Converts source files to markdown under `<source>/markdown/`.

```bash
python scripts/convert_to_markdown.py --memory <source_path>
python scripts/convert_to_markdown.py --file <file_path>
```

- `--memory`: Convert all supported files in folder.
- `--file`: Convert a single file only.

## chunk_markdown.py

Chunks markdown files into `<source>/memory/`. Uses `context_chunking_spec.yaml` if present.

```bash
python scripts/chunk_markdown.py --path <source_folder> --output <memory_folder>
```

When a spec is present, chunks include YAML front matter with `chunk_id`, `evidence_type`, `chunk_type`, and `section_path`.

## embed_and_index.py

Embeds chunks and writes FAISS index to `<memory_folder>/rag/`.

```bash
python scripts/embed_and_index.py --path <memory_folder>
python scripts/embed_and_index.py --path <memory_folder> --replace
```

- `--path`: The `memory/` folder containing chunks.
- `--replace`: Rebuild index from scratch.

## search_memory.py

Semantic search over the FAISS index.

```bash
python scripts/search_memory.py "<query>" --rag <memory/rag> [--k 5] [--format text|json]
```

- `--rag`: Path to the `rag/` folder (`<source>/memory/rag`).
- `--k`: Number of results (default 5).
- `--format`: `text` (default) or `json`.

## markdown_to_excel.py / markdown_to_docx.py / markdown_to_pdf.py

Generic export utilities.

```bash
python scripts/markdown_to_excel.py <input.md> [output.xlsx]
python scripts/markdown_to_docx.py  <input.md> [output.docx]
python scripts/markdown_to_pdf.py   <input.md> [output.pdf] [--pdf-engine weasyprint]
```

**Dependencies**: `pip install openpyxl pypandoc` + pandoc binary.


---

### `output.md`

# Output structure

After `index_memory.py --path <source>`:

```
<source>/                       ← topic root (CONTENT_MEMORY_ROOT or --path)
  scripts/                       ← optional: corpus-only preprocess (see below)
    prepare_*.py, README.md
  markdown/
    .../<file>.md              ← converted from originals
    structural_scan_report.txt ← structural scan (assess converted markdown; same text as console)
    structural_scan_report.md
  archive/                       ← optional: backups (e.g. pre-normalization .md)
  memory/                        ← chunks + chunking spec (not structural scan)
    context_chunking_spec.yaml   ← chunking rules + taxonomy (draft after structure looks OK)
    .../<file>__slide_01.md      ← chunks (front matter when spec active)
    .../<file>__section_00.md
    rag/
      index.faiss
      metadata.json
```

**Legacy:** older runs may have `context_chunking_spec.yaml` under `markdown/` or at `<source>/` (topic root). The chunker checks **`memory/`** first, then those paths.

## Corpus `scripts/` (topic root)

Optional **`scripts/`** under `<source>/` holds **corpus-only** preprocess (normalize Markdown so chunking can split). Not the shared tools in `skills/abd-context-to-memory/scripts/`. **Full convention** (why, naming, docs, `archive/`, `chunk_inputs`) → [../process.md](../process.md) → subsection *Corpus preprocess scripts (`<topic_root>/scripts/`)*.

## Chunk naming

- PowerPoint: `<stem>__slide_01.md`, `__slide_02.md`, …
- Prose: `<stem>__section_00.md`, `__section_01.md`, …
- Short file (one chunk): `<stem>.md`

## Chunk content (without spec)

Each chunk includes `<!-- Source: path -->` for traceability.

## Chunk content (with spec)

Each chunk has YAML front matter:

```yaml
---
chunk_id: <stem>__section_00
source:
  canonical_path: <relative path to source md>
evidence_type: mixed
chunk_type: prose_block
section_path: ["Chapter 3", "Powers"]
---

<chunk body text>
```

`evidence_type` and `chunk_type` come from `context_chunking_spec.yaml → defaults` until you relabel per chunk. Legacy key `modeling_kind` in old specs maps to `chunk_type` in the chunker.


---

### `rag-retrieval.md`

# RAG Semantic Retrieval

Build the FAISS index on **your machine**, next to your source tree (see [config.md](config.md)). Point `--rag` at that folder when searching—there is no default index path inside this skill repo.

When the user asks about content in memory, run semantic search and inject results.

## Trigger Phrases

Run `search_memory "<query>"` when the user says:

- "use memory", "search memory", "what does memory say"
- "from our content", "from ABD materials", "from our decks"
- "what do we have on [topic]"
- Asks about Agile, training, proposals, service offerings, or any ingested materials

## Agent Flow

1. **Derive query** — Extract a semantic query from the user's question.
2. **Run search** — From a shell where paths resolve (topic folder, or set `CONTENT_MEMORY_ROOT`):
   ```bash
   python skills/abd-context-to-memory/scripts/search_memory.py "<query>" --rag <source>/memory/rag --k 5
   ```
3. **Inject results** — Use the returned chunks in your response.
4. **Cite sources** — Include path and slide/section when using retrieved content. If chunks have front matter, also note `evidence_type` / `chunk_type` to signal how much weight to give the result.

## Requirements

- RAG deps: `pip install -r skills/abd-context-to-memory/requirements-rag.txt`
- `OPENAI_API_KEY` set
- Index exists: run `index_memory.py --path <source>` first

## Output Layout

```
<source>/memory/rag/
  index.faiss
  metadata.json
```

## Chunk front matter (when spec was active during chunking)

Results may include chunks with YAML front matter. Use the labels to calibrate your response:

| `chunk_type` (corpus-specific) | How to use |
|----------------|-----------|
| Normative roles (e.g. `stat_block`, `powers`, rules-like sections) | Cite carefully — check against source |
| Illustration / example scenes | Use as illustration unless corroborated |
| `toc_or_index`, `noise_or_art`, navigation-like | Low weight |


---

