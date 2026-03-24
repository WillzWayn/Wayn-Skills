---
description: >
  Create professional LaTeX documents — CVs, academic reports, presentations (Beamer),
  and manage BibTeX references. Use this skill whenever the user asks to create, edit,
  or compile any LaTeX document, write a resume/CV in LaTeX, build slides or a presentation,
  write an academic paper or report, or set up bibliography management. Also triggers when
  the user mentions .tex files, pdflatex, bibtex, beamer, or any LaTeX-related workflow.
allowed-tools: Bash(pdflatex *), Bash(xelatex *), Bash(lualatex *), Bash(bibtex *), Bash(biber *), Bash(latexmk *), Read, Write, Glob, Grep
---

# LaTeX Document Creator

Professional LaTeX document generation with support for multiple document types.

## Quick Start

1. Identify what type of document the user needs
2. Read the relevant reference file for detailed templates and instructions
3. Generate the `.tex` file(s) and compile to PDF

## Document Types

Each type has its own reference with templates, best practices, and examples:

| Type | Reference | Use when |
|------|-----------|----------|
| **CV / Resume** | [cv.md](cv.md) | User wants a professional CV, resume, or curriculum vitae |
| **Presentation** | [presentation.md](presentation.md) | User wants slides, a talk, or a Beamer presentation |
| **Academic Report** | [academic-report.md](academic-report.md) | User wants a paper, thesis chapter, technical report, or academic document |
| **BibTeX** | [bibtex.md](bibtex.md) | User needs to manage references, citations, or bibliography |

Read the appropriate reference file before generating any document.

## General LaTeX Principles

- Always use UTF-8 encoding: `\usepackage[utf8]{inputenc}` (pdflatex) or compile with xelatex/lualatex
- Prefer `\usepackage[T1]{fontenc}` for proper font encoding with pdflatex
- Use `\usepackage[brazilian]{babel}` or `\usepackage[english]{babel}` based on the user's language
- Escape special characters: `%`, `$`, `&`, `#`, `_`, `{`, `}`, `~`, `^`
- For multi-file projects, use `\input{}` or `\include{}` to keep things modular

## Compilation Workflow

```bash
# Simple document
pdflatex -interaction=nonstopmode document.tex

# With bibliography
pdflatex document.tex
bibtex document
pdflatex document.tex
pdflatex document.tex

# Or use latexmk for automatic dependency resolution
latexmk -pdf document.tex
```

If compilation fails, read the `.log` file to diagnose — LaTeX error messages point to the exact line.

## File Organization

For any non-trivial project, organize files:

```
project/
├── main.tex          # Main document
├── references.bib    # Bibliography (if needed)
├── sections/         # Chapter/section files (if modular)
├── figures/          # Images and diagrams
└── output/           # Compiled PDFs
```

## Arguments

`$ARGUMENTS` — the user's request describing what document they need. Parse it to determine the document type and specific requirements, then consult the appropriate reference file.
