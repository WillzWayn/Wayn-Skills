# Presentations with Beamer

## When to Use

User wants to create slides, a talk, a lecture, or any kind of presentation in LaTeX.

## Recommended Approach

Beamer is the standard LaTeX class for presentations. It supports themes, overlays (incremental reveals), and integrates naturally with LaTeX math, figures, and BibTeX.

## Template: Clean Presentation

```latex
\documentclass[aspectratio=169]{beamer}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{amsmath}

% Theme
\usetheme{Madrid}
\usecolortheme{default}

% Remove navigation symbols (they clutter slides)
\setbeamertemplate{navigation symbols}{}

% Metadata
\title{Presentation Title}
\subtitle{Optional Subtitle}
\author{Author Name}
\institute{Institution / Company}
\date{\today}

\begin{document}

\begin{frame}
  \titlepage
\end{frame}

\begin{frame}{Outline}
  \tableofcontents
\end{frame}

\section{Introduction}

\begin{frame}{Motivation}
  \begin{itemize}
    \item First point about the problem
    \item Why it matters
    \item What we propose
  \end{itemize}
\end{frame}

\section{Methodology}

\begin{frame}{Approach}
  \begin{columns}
    \column{0.5\textwidth}
    \begin{itemize}
      \item Step 1: Data collection
      \item Step 2: Processing
      \item Step 3: Analysis
    \end{itemize}

    \column{0.5\textwidth}
    \begin{figure}
      \centering
      % \includegraphics[width=\textwidth]{diagram.png}
      \caption{System overview}
    \end{figure}
  \end{columns}
\end{frame}

\begin{frame}{Key Equation}
  The loss function is defined as:
  \begin{equation}
    \mathcal{L} = -\sum_{i=1}^{N} y_i \log(\hat{y}_i)
  \end{equation}
\end{frame}

\section{Results}

\begin{frame}{Results Table}
  \begin{table}
    \centering
    \begin{tabular}{lcc}
      \toprule
      Method & Accuracy & F1 Score \\
      \midrule
      Baseline & 0.82 & 0.79 \\
      Ours & \textbf{0.91} & \textbf{0.88} \\
      \bottomrule
    \end{tabular}
    \caption{Comparison of methods}
  \end{table}
\end{frame}

\section{Conclusion}

\begin{frame}{Takeaways}
  \begin{enumerate}
    \item Main contribution
    \item Impact
    \item Future work
  \end{enumerate}
\end{frame}

\begin{frame}{}
  \centering
  \Huge Thank you! \\[1em]
  \normalsize Questions?
\end{frame}

\end{document}
```

## Popular Themes

| Theme | Style | Best for |
|-------|-------|----------|
| `Madrid` | Clean, professional | Business, conferences |
| `metropolis` | Modern, minimal | Tech talks, academia |
| `CambridgeUS` | Traditional | Academic conferences |
| `Bergen` | Sidebar navigation | Longer lectures |
| `default` | Bare bones | Full customization |

To use `metropolis` (highly recommended for modern look):
```latex
\documentclass[aspectratio=169]{beamer}
\usetheme{metropolis}
```
Install if needed: `tlmgr install beamertheme-metropolis`

## Overlays (Incremental Reveals)

```latex
% Items appear one at a time
\begin{frame}{Step by Step}
  \begin{itemize}
    \item<1-> First point (visible from slide 1)
    \item<2-> Second point (visible from slide 2)
    \item<3-> Third point (visible from slide 3)
  \end{itemize}
\end{frame}

% Shorthand: \pause
\begin{frame}{With Pause}
  First part visible.
  \pause
  Second part appears after click.
\end{frame}
```

## Aspect Ratio

- `aspectratio=169` — widescreen (16:9), modern default
- `aspectratio=43` — classic (4:3), for old projectors
- `aspectratio=1610` — 16:10, some laptops

## Adding Figures

```latex
\begin{frame}{Results}
  \begin{figure}
    \centering
    \includegraphics[width=0.8\textwidth]{plot.pdf}
    \caption{Performance comparison}
  \end{figure}
\end{frame}
```

Prefer PDF or PNG for figures. PDF gives the best quality for vector graphics.

## Speaker Notes

```latex
% In preamble
\setbeameroption{show notes on second screen=right}

% In a frame
\begin{frame}{Title}
  Content on slide.
  \note{These are my speaker notes — only visible in presenter mode.}
\end{frame}
```

## Best Practices

- **One idea per slide** — don't cram everything
- **Minimal text** — use bullet points, not paragraphs
- **Large fonts** — if you need to shrink text to fit, you have too much
- **High-contrast colors** — readability from the back of the room
- **Number your slides** — helps during Q&A ("go back to slide 7")
- **Test your aspect ratio** — match the projector/screen you'll use

## Compilation

```bash
pdflatex -interaction=nonstopmode presentation.tex

# With citations
pdflatex presentation.tex && bibtex presentation && pdflatex presentation.tex && pdflatex presentation.tex
```
