# CV / Resume in LaTeX

## When to Use

User wants a professional CV, resume, or curriculum vitae — for job applications, academic positions, or personal branding.

## Recommended Approach

Use the `moderncv` package for clean, professional CVs. It handles layout, typography, and spacing out of the box, so you focus on content.

Alternative: for a more minimalist or custom look, build from scratch with `article` class + `geometry` + `titlesec`.

## Template: moderncv

```latex
\documentclass[11pt,a4paper,sans]{moderncv}

% Style options: 'casual', 'classic', 'banking', 'oldstyle', 'fancy'
\moderncvstyle{banking}

% Color options: 'black', 'blue', 'burgundy', 'green', 'grey', 'orange', 'purple', 'red'
\moderncvcolor{blue}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[scale=0.85]{geometry}

% Personal data
\name{First}{Last}
\title{Professional Title}
\address{Street}{City, State}{Country}
\phone[mobile]{+55~(11)~99999-0000}
\email{email@example.com}
\social[linkedin]{linkedin-username}
\social[github]{github-username}

\begin{document}
\makecvtitle

\section{Education}
\cventry{2020--2024}{B.Sc. Computer Science}{University Name}{City}{\textit{GPA: 3.8/4.0}}{}

\section{Experience}
\cventry{2023--Present}{Software Engineer}{Company Name}{City}{}{
  \begin{itemize}
    \item Led migration of monolith to microservices, reducing deploy time by 60\%
    \item Built real-time data pipeline processing 10M+ events/day
  \end{itemize}
}

\section{Skills}
\cvitem{Languages}{Python, Go, TypeScript, SQL}
\cvitem{Tools}{Docker, Kubernetes, AWS, Terraform}

\section{Languages}
\cvitemwithcomment{Portuguese}{Native}{}
\cvitemwithcomment{English}{Fluent}{TOEFL 110}

\end{document}
```

## Template: Minimal Custom CV

For users who want full control over the layout:

```latex
\documentclass[11pt,a4paper]{article}

\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage[margin=1.5cm]{geometry}
\usepackage{titlesec}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}

\definecolor{accent}{HTML}{2B6CB0}

% Remove page numbers
\pagestyle{empty}

% Section formatting
\titleformat{\section}{\large\bfseries\color{accent}}{}{0em}{}[\titlerule]
\titlespacing*{\section}{0pt}{12pt}{6pt}

% Custom commands
\newcommand{\entry}[4]{
  \noindent\textbf{#1} \hfill #2 \\
  \textit{#3} \hfill \textit{#4} \par\vspace{4pt}
}

\begin{document}

\begin{center}
  {\LARGE\bfseries First Last} \\[4pt]
  email@example.com \quad | \quad +55 11 99999-0000 \quad | \quad
  \href{https://github.com/username}{github.com/username}
\end{center}

\section{Experience}
\entry{Software Engineer}{Jan 2023 -- Present}{Company Name}{City, Brazil}
\begin{itemize}[nosep, leftmargin=1.5em]
  \item Accomplishment with measurable impact
  \item Another key contribution
\end{itemize}

\section{Education}
\entry{B.Sc. Computer Science}{2020 -- 2024}{University Name}{City, Brazil}

\section{Skills}
\noindent Python, Go, TypeScript, Docker, Kubernetes, AWS, PostgreSQL, Redis

\end{document}
```

## Best Practices

- **Quantify achievements**: "Reduced latency by 40%" beats "Improved performance"
- **One page** for most professionals; two pages only if 10+ years of experience
- **Consistent date format**: pick one style and stick with it
- **PDF output**: always compile to PDF for sharing — never send `.tex` files
- **ATS-friendly**: if the user mentions applicant tracking systems, keep formatting simple (no tables for layout, no multi-column tricks)

## Common Customizations

### Adding a photo (moderncv)
```latex
\photo[64pt][0.4pt]{photo.jpg}
```

### Two-column skills section
```latex
\usepackage{multicol}
\begin{multicols}{2}
  \cvitem{Python}{Advanced}
  \cvitem{Go}{Intermediate}
\end{multicols}
```

### Custom colors
```latex
\definecolor{myblue}{HTML}{1A365D}
\moderncvcolor{myblue}  % Won't work — moderncv uses predefined colors
% Instead, redefine:
\colorlet{color1}{myblue}
```

## Compilation

```bash
pdflatex -interaction=nonstopmode cv.tex
# moderncv doesn't need bibtex unless you add a publications section
```

If `moderncv` is not installed, install it:
```bash
# macOS (MacTeX)
tlmgr install moderncv

# Ubuntu/Debian
sudo apt-get install texlive-latex-extra
```
