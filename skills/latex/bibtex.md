# BibTeX Reference Management

## When to Use

User needs to manage references, add citations, create a bibliography, or work with `.bib` files.

## How BibTeX Works

1. You maintain a `.bib` file with all your references
2. In the `.tex` document, use `\cite{key}` to reference entries
3. Compile: `pdflatex → bibtex → pdflatex → pdflatex` (the triple pass resolves all references)

## .bib File Format

Each entry has a type, a citation key, and fields:

```bibtex
@article{silva2024bandits,
  author    = {Silva, João and Santos, Maria},
  title     = {Contextual Bandits for A/B Testing},
  journal   = {Journal of Machine Learning Research},
  volume    = {25},
  number    = {3},
  pages     = {1--42},
  year      = {2024},
  doi       = {10.xxxx/jmlr.v25.24-0001}
}

@inproceedings{chen2023transformer,
  author    = {Chen, Wei and Li, Hong},
  title     = {Efficient Transformers for Low-Resource NLP},
  booktitle = {Proceedings of ACL 2023},
  pages     = {1234--1245},
  year      = {2023},
  publisher = {Association for Computational Linguistics}
}

@book{bishop2006pattern,
  author    = {Bishop, Christopher M.},
  title     = {Pattern Recognition and Machine Learning},
  publisher = {Springer},
  year      = {2006},
  isbn      = {978-0-387-31073-2}
}

@misc{vaswani2017attention,
  author    = {Vaswani, Ashish and others},
  title     = {Attention Is All You Need},
  year      = {2017},
  eprint    = {1706.03762},
  archiveprefix = {arXiv},
  primaryclass  = {cs.CL}
}

@phdthesis{doe2023thesis,
  author  = {Doe, Jane},
  title   = {Deep Learning for Medical Imaging},
  school  = {Stanford University},
  year    = {2023}
}

@online{python2024docs,
  author  = {{Python Software Foundation}},
  title   = {Python 3.12 Documentation},
  url     = {https://docs.python.org/3.12/},
  urldate = {2024-01-15},
  year    = {2024}
}
```

## Common Entry Types

| Type | Use for |
|------|---------|
| `@article` | Journal papers |
| `@inproceedings` | Conference papers |
| `@book` | Books |
| `@incollection` | Book chapters |
| `@misc` | arXiv preprints, software, datasets |
| `@phdthesis` / `@mastersthesis` | Dissertations |
| `@online` | Websites (requires `biblatex`) |
| `@techreport` | Technical reports |

## Citation Commands

### With natbib (recommended for most papers)

```latex
\usepackage[numbers]{natbib}  % numeric style
% or
\usepackage{natbib}           % author-year style

\citet{silva2024bandits}     % Silva et al. (2024)
\citep{silva2024bandits}     % (Silva et al., 2024)
\citep[see][]{silva2024bandits}  % (see Silva et al., 2024)
\citep{silva2024bandits,chen2023transformer}  % (Silva et al., 2024; Chen & Li, 2023)
```

### With biblatex (more modern, more features)

```latex
\usepackage[backend=biber, style=authoryear]{biblatex}
\addbibresource{references.bib}

\textcite{silva2024bandits}   % Silva et al. (2024)
\parencite{silva2024bandits}  % (Silva et al., 2024)
\fullcite{silva2024bandits}   % Full inline citation

% At end of document:
\printbibliography
```

### natbib vs biblatex

| Feature | natbib | biblatex |
|---------|--------|----------|
| Simplicity | Simpler | More setup |
| Styles | `plainnat`, `abbrvnat`, `unsrtnat` | Huge variety |
| URLs | Needs `url` package | Built-in |
| Sorting | Basic | Highly configurable |
| Backend | `bibtex` | `biber` (better Unicode) |
| Conference templates | Usually expect natbib | Less common |

**Rule of thumb**: use natbib for conference/journal submissions (they often provide a `.bst` file). Use biblatex for theses, reports, and personal projects.

## Bibliography Styles

### natbib styles
```latex
\bibliographystyle{plainnat}   % Author (Year). Full names, sorted alphabetically
\bibliographystyle{abbrvnat}   % Abbreviated first names
\bibliographystyle{unsrtnat}   % Order of citation (not alphabetical)
\bibliographystyle{IEEEtranN}  % IEEE style (numeric)
```

### biblatex styles
```latex
style=authoryear    % (Author, Year)
style=numeric       % [1], [2], [3]
style=alphabetic    % [Sil24], [Che23]
style=ieee          % IEEE format
style=apa           % APA format
```

## Citation Key Conventions

Use a consistent naming scheme. The most common:

```
authorYEARfirstword
```

Examples:
- `silva2024bandits` — Silva et al., 2024, "Contextual Bandits..."
- `bishop2006pattern` — Bishop, 2006, "Pattern Recognition..."
- `vaswani2017attention` — Vaswani et al., 2017, "Attention Is All You Need"

This makes keys predictable and easy to remember while writing.

## Getting BibTeX Entries

Instead of typing entries manually:

1. **Google Scholar** — search the paper → click "Cite" → "BibTeX"
2. **DOI** — `https://doi.org/<doi>` with Accept header `application/x-bibtex`
3. **DBLP** — `dblp.org` has clean BibTeX for CS papers
4. **Semantic Scholar** — good for ML/AI papers
5. **Zotero / Mendeley** — reference managers that export `.bib` files

Always verify the exported entry — Google Scholar entries often have errors (wrong accents, missing fields, inconsistent capitalization).

## Common Issues and Fixes

### "Citation undefined"
Run the compilation cycle: `pdflatex → bibtex → pdflatex → pdflatex`. All three passes are necessary.

### Title capitalization changes
BibTeX lowercases titles based on the style. Protect words that must stay capitalized:
```bibtex
title = {Attention Is All You Need}          % may become "attention is all you need"
title = {{Attention} Is {All} You {Need}}    % protected
title = {{Attention Is All You Need}}        % whole title protected
```

### Special characters in names
```bibtex
author = {M{\"u}ller, Hans and Gonz{\'a}lez, Pedro}
```

### Multiple authors
Use `and` between authors, not commas:
```bibtex
author = {Silva, João and Santos, Maria and Chen, Wei}
```

## Compilation

### With natbib + bibtex
```bash
pdflatex main.tex
bibtex main        # processes the .aux file, not .tex
pdflatex main.tex
pdflatex main.tex
```

### With biblatex + biber
```bash
pdflatex main.tex
biber main
pdflatex main.tex
pdflatex main.tex
```

### With latexmk (handles everything)
```bash
latexmk -pdf main.tex
```
