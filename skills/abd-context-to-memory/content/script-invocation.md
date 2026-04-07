# Script Invocation

Run from workspace root.

## index_memory.py

Full pipeline: convert → chunk → embed.

```bash
python scripts/index_memory.py --path <source_folder>
python scripts/index_memory.py --path <source_folder> --skip-convert
python scripts/index_memory.py --path <source_folder> --rebuild
```

- `--path`: Source folder of documents.
- `--skip-convert`: Markdown already exists; start at chunking.
- `--rebuild`: Rebuild the FAISS index from existing chunks.

## convert_to_markdown.py

Converts source files to markdown under `<source>/markdown/`.

```bash
python scripts/convert_to_markdown.py --memory <source_path>
python scripts/convert_to_markdown.py --file <file_path>
```

- `--memory`: Convert all supported files in folder.
- `--file`: Convert a single file only.

## chunk_markdown.py

Chunks markdown files into `<source>/memory/`.

```bash
python scripts/chunk_markdown.py --path <source_folder> --output <memory_folder>
```

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
