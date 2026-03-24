# Academic Reports and Papers

## When to Use

User wants to write an academic paper, thesis chapter, technical report, journal article, conference submission, or any formal academic document.

## Recommended Approach

Use the `article` class for most papers and reports. For theses, use `report` or `book`. For specific conferences/journals, check if they provide a `.cls` file (e.g., IEEE, ACM, Springer LNCS).

## Template: General Academic Paper

```latex
\documentclass[12pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=2.5cm]{geometry}
\usepackage{amsmath, amssymb, amsthm}
\usepackage{graphicx}
\usepackage{booktabs}
\usepackage{hyperref}
\usepackage{cleveref}
\usepackage[numbers]{natbib}
\usepackage{algorithm}
\usepackage{algpseudocode}
\usepackage{listings}
\usepackage{xcolor}

% Theorem environments
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{corollary}[theorem]{Corollary}

% Code listing style
\lstset{
  basicstyle=\ttfamily\small,
  keywordstyle=\color{blue},
  commentstyle=\color{gray},
  stringstyle=\color{red},
  numbers=left,
  numberstyle=\tiny\color{gray},
  breaklines=true,
  frame=single
}

\title{Paper Title: A Subtitle if Needed}
\author{
  Author One\thanks{affiliation@university.edu} \and
  Author Two\thanks{other@institution.org}
}
\date{\today}

\begin{document}

\maketitle

\begin{abstract}
  Brief summary of the problem, approach, key results, and implications.
  Keep it under 250 words for most venues.
\end{abstract}

\textbf{Keywords:} keyword one, keyword two, keyword three

\section{Introduction}
\label{sec:intro}

Context and motivation. What problem are we solving? Why does it matter?

The main contributions of this work are:
\begin{enumerate}
  \item First contribution
  \item Second contribution
  \item Third contribution
\end{enumerate}

\section{Related Work}
\label{sec:related}

Previous approaches and how they differ from ours.
\citet{author2023} proposed X, but it lacks Y. In contrast, our method...

\section{Methodology}
\label{sec:method}

\subsection{Problem Formulation}

Given a dataset $\mathcal{D} = \{(x_i, y_i)\}_{i=1}^{N}$, we aim to...

\begin{definition}[Formal Problem]
  Define the problem precisely using mathematical notation.
\end{definition}

\subsection{Proposed Approach}

\begin{algorithm}
\caption{Our Algorithm}
\label{alg:main}
\begin{algorithmic}[1]
  \Require Input data $X$, parameters $\theta$
  \Ensure Trained model $f_\theta$
  \State Initialize $\theta$ randomly
  \For{epoch $= 1$ to $E$}
    \For{batch $B$ in $X$}
      \State $\mathcal{L} \gets \text{ComputeLoss}(f_\theta(B), y_B)$
      \State $\theta \gets \theta - \eta \nabla_\theta \mathcal{L}$
    \EndFor
  \EndFor
  \State \Return $f_\theta$
\end{algorithmic}
\end{algorithm}

\section{Experiments}
\label{sec:experiments}

\subsection{Setup}

Describe datasets, baselines, metrics, and hyperparameters.

\subsection{Results}

\begin{table}[ht]
  \centering
  \caption{Main results on benchmark dataset}
  \label{tab:results}
  \begin{tabular}{lccc}
    \toprule
    Method & Precision & Recall & F1 \\
    \midrule
    Baseline A & 0.82 & 0.78 & 0.80 \\
    Baseline B & 0.85 & 0.81 & 0.83 \\
    \textbf{Ours} & \textbf{0.91} & \textbf{0.88} & \textbf{0.89} \\
    \bottomrule
  \end{tabular}
\end{table}

As shown in \Cref{tab:results}, our method outperforms...

\begin{figure}[ht]
  \centering
  % \includegraphics[width=0.7\textwidth]{results_plot.pdf}
  \caption{Performance across different dataset sizes}
  \label{fig:results}
\end{figure}

\section{Discussion}
\label{sec:discussion}

Interpret results, limitations, and implications.

\section{Conclusion}
\label{sec:conclusion}

Summary and future work.

\bibliographystyle{plainnat}
\bibliography{references}

\appendix
\section{Additional Experiments}
\label{app:additional}

Supplementary material goes here.

\end{document}
```

## Conference-Specific Templates

### IEEE
```latex
\documentclass[conference]{IEEEtran}
\usepackage{cite}
\usepackage{amsmath}
\usepackage{graphicx}
```

### ACM
```latex
\documentclass[sigconf]{acmart}
% ACM template handles most formatting automatically
```

### Springer LNCS
```latex
\documentclass{llncs}
\usepackage{graphicx}
```

For any of these, download the official template from the venue's website — they update frequently and reviewers notice format violations.

## Useful Packages by Need

| Need | Package | Why |
|------|---------|-----|
| Smart cross-references | `cleveref` | Writes "Figure 1" automatically instead of manual "Figure~\ref{}" |
| Better citations | `natbib` | Author-year or numeric, `\citet` and `\citep` |
| Professional tables | `booktabs` | `\toprule`, `\midrule`, `\bottomrule` — no vertical lines |
| Subfigures | `subcaption` | `\begin{subfigure}` for side-by-side figures |
| Algorithms | `algorithm` + `algpseudocode` | Clean pseudocode blocks |
| Code listings | `listings` or `minted` | Syntax-highlighted source code |
| SI units | `siunitx` | Consistent formatting: `\SI{3.14}{\meter\per\second}` |
| To-do notes | `todonotes` | `\todo{Fix this}` margin notes during drafting |

## Writing Tips

- **Use `\label` and `\cref` everywhere** — never hardcode "Table 1" or "Section 3"
- **One sentence per line** in the source — makes git diffs readable
- **Define macros for repeated notation**: `\newcommand{\loss}{\mathcal{L}}`
- **Separate content from presentation** — don't tweak spacing until the final draft
- **Use `\input{}` for sections** in longer documents to keep files manageable

## Compilation

```bash
# Standard compilation with bibliography
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex

# Or all-in-one
latexmk -pdf main.tex
```
