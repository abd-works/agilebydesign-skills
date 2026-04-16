# Outline



**How it works** (each step is distinct; order matters):

- **Convert** supported sources to Markdown (under `markdown/` in the source tree).
- **Draft** a structure-aware chunking spec: `context_chunking_spec.yaml` (boundaries, splitting, taxonomy for *this* corpus).
- **Strategy pass (optional but important when quality beats speed):** review or edit that YAML *before* chunking and embedding so splits and labels match the material.
- **Chunk** Markdown into `memory/`; when the spec applies, chunks get front matter such as `evidence_type` and `chunk_type`.
- **Embed** chunk vectors into a **local FAISS** index next to your source tree (e.g. `<source_folder>/memory/rag/`—you choose the corpus folder).
- **Search** semantically over what you embedded (e.g. via the project’s search script), not just keyword grep.

**Where to read more:** **`SKILL.md`** (activation and short commands), **`content/parts/process.md`** (full pipeline, flags, examples), **`content/parts/library/`** (chunking YAML detail, script CLI, artifact layout, RAG behavior).
