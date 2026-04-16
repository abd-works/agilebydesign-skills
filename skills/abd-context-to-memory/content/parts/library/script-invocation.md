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
