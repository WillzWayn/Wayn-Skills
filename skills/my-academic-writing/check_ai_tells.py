#!/usr/bin/env python3
"""
check_ai_tells.py — Deterministic AI-tell detector for academic writing.

Flags characters, words, and structural patterns that are disproportionately
common in AI-generated text and that conflict with William Wayn's writing voice.

Usage:
    python check_ai_tells.py <file.txt>
    cat file.txt | python check_ai_tells.py -
    python check_ai_tells.py <file.txt> --strict   # non-zero exit if any flag found

Rules are drawn from SKILL.md § 4 (Anti-AI Writing Patterns).
"""

import re
import sys
import argparse
from dataclasses import dataclass, field
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Rule definitions
# ---------------------------------------------------------------------------

@dataclass
class Finding:
    rule_id: str
    severity: str          # "error" | "warning" | "info"
    line: int
    col: int
    excerpt: str
    message: str


# Each rule is (rule_id, severity, compiled_regex, message_template)
# The regex may have a named group "match" for the excerpt — otherwise the
# full match is used.

INLINE_RULES: List[Tuple[str, str, re.Pattern, str]] = [
    # -----------------------------------------------------------------------
    # Character-level tells
    # -----------------------------------------------------------------------
    (
        "EM_DASH",
        "warning",
        re.compile(r"—"),
        "Em dash (—) found. William uses commas and semicolons instead; "
        "more than 2 per page is an AI fingerprint.",
    ),
    (
        "CURLY_QUOTE_MISMATCH",
        "info",
        re.compile(r"[\u201c\u201d\u2018\u2019]"),
        "Curly/smart quote found. Some AI tools insert these; verify the "
        "character is intentional and consistent.",
    ),
    (
        "ELLIPSIS_CHAR",
        "info",
        re.compile(r"\u2026"),
        "Unicode ellipsis character (…) found. Prefer three explicit dots (...) "
        "for plain-text consistency.",
    ),

    # -----------------------------------------------------------------------
    # AI vocabulary words (case-insensitive)
    # -----------------------------------------------------------------------
    (
        "AI_VOCAB",
        "error",
        re.compile(
            r"\b(?:delve|foster(?:ing|ed|s)?|garner(?:ing|ed|s)?|groundbreaking"
            r"|tapestry|underscore(?:s|d|ing)?|interplay|intricate(?:ly)?"
            r"|pivotal|vibrant|renowned|showcase(?:s|d|ing)?|nuanced"
            r"|holistic(?:ally)?|paradigm\s+shift|synerg(?:y|ies|istic)"
            r"|leverage(?:s|d|ing)?|robust(?:ly)?|seamless(?:ly)?"
            r"|landscape(?:s)?|realm(?:s)?)\b",
            re.IGNORECASE,
        ),
        "AI vocabulary word. Replace with a simpler, more direct alternative.",
    ),
    (
        "AI_VOCAB_EN_CONNECTOR",
        "warning",
        re.compile(r"\bAdditionally\b", re.IGNORECASE),
        "'Additionally' is overused in AI text. In English use 'Also', 'Besides', "
        "or restructure; in Portuguese prefer 'Além disso' sparingly.",
    ),

    # -----------------------------------------------------------------------
    # Copula avoidance
    # -----------------------------------------------------------------------
    (
        "SERVES_AS",
        "error",
        re.compile(r"\b(?:serves?\s+as|stands?\s+as)\b", re.IGNORECASE),
        "Copula avoidance ('serves as', 'stands as'). Write 'is' or the direct verb.",
    ),

    # -----------------------------------------------------------------------
    # Promotional / significance inflation
    # -----------------------------------------------------------------------
    (
        "SIGNIFICANCE_CLAIM",
        "error",
        re.compile(
            r"\b(?:crucial(?:ly)?|pivotal(?:ly)?|vital(?:ly)?|testament\s+to"
            r"|stands?\s+as\s+a\s+testament)\b",
            re.IGNORECASE,
        ),
        "Generic significance claim. Show importance through consequences, not adjectives.",
    ),
    (
        "PROMOTIONAL_ADJ",
        "warning",
        re.compile(
            r"\b(?:groundbreaking|cutting[- ]edge|state[- ]of[- ]the[- ]art"
            r"|unprecedented|remarkable|extraordinary|fascinating)\b",
            re.IGNORECASE,
        ),
        "Promotional adjective. William's tone is warm but never promotional.",
    ),

    # -----------------------------------------------------------------------
    # Superficial -ing analyses
    # -----------------------------------------------------------------------
    (
        "SUPERFICIAL_ING",
        "warning",
        re.compile(
            r"\b(?:highlight(?:ing|s|ed)\s+the\s+importance\s+of"
            r"|underscore?(?:s|d|ing)\s+the\s+(?:importance|significance)\s+of"
            r"|emphasiz(?:es?|ing|ed)\s+the\s+(?:importance|significance)\s+of)\b",
            re.IGNORECASE,
        ),
        "Superficial -ing analysis. Provide concrete analysis instead of declaring importance.",
    ),

    # -----------------------------------------------------------------------
    # Negative parallelisms
    # -----------------------------------------------------------------------
    (
        "NEG_PARALLELISM",
        "warning",
        re.compile(
            r"\b(?:not\s+only\b.{0,60}\bbut\s+also\b"
            r"|it['']?s\s+not\s+just\s+about\b.{0,60}\bit['']?s\b)",
            re.IGNORECASE,
        ),
        "Negative parallelism ('Not only...but also...'). William doesn't use these constructions.",
    ),

    # -----------------------------------------------------------------------
    # False ranges
    # -----------------------------------------------------------------------
    (
        "FALSE_RANGE",
        "info",
        re.compile(r"\bfrom\s+\w+\s+to\s+\w+\b", re.IGNORECASE),
        "Possible false range ('from X to Y'). Verify X and Y are on a meaningful scale; "
        "otherwise list topics directly.",
    ),

    # -----------------------------------------------------------------------
    # Filler phrases
    # -----------------------------------------------------------------------
    (
        "FILLER_PHRASE",
        "error",
        re.compile(
            r"\b(?:it\s+is\s+(?:important|worth(?:while)?)\s+to\s+note\s+that"
            r"|it\s+goes\s+without\s+saying\s+that"
            r"|it\s+is\s+well\s+known\s+that"
            r"|needless\s+to\s+say"
            r"|due\s+to\s+the\s+fact\s+that"
            r"|in\s+order\s+to\b"
            r"|it\s+should\s+be\s+noted\s+that)\b",
            re.IGNORECASE,
        ),
        "Filler phrase. Cut it or replace with a direct construction.",
    ),

    # -----------------------------------------------------------------------
    # Excessive hedging
    # -----------------------------------------------------------------------
    (
        "EXCESSIVE_HEDGE",
        "warning",
        re.compile(
            r"\bcould\s+potentially\b|\bmay\s+possibly\b"
            r"|\bseems?\s+to\s+(?:suggest|indicate|imply)\b",
            re.IGNORECASE,
        ),
        "Excessive hedging. One qualifier is enough ('podemos estimar', 'suggests').",
    ),

    # -----------------------------------------------------------------------
    # Generic positive conclusions
    # -----------------------------------------------------------------------
    (
        "GENERIC_CONCLUSION",
        "error",
        re.compile(
            r"\b(?:the\s+future\s+(?:looks?|is)\s+(?:bright|promising)"
            r"|exciting\s+times?\s+(?:lie|lay)\s+ahead"
            r"|much\s+remains?\s+to\s+be\s+(?:explored?|discovered?|done)"
            r"|opens?\s+(?:new\s+)?(?:doors?|horizons?|avenues?))\b",
            re.IGNORECASE,
        ),
        "Generic positive conclusion. End with specific results, honest limitations, "
        "or encouragement to consult references.",
    ),

    # -----------------------------------------------------------------------
    # Passive voice indicators (informational — William uses active)
    # -----------------------------------------------------------------------
    (
        "PASSIVE_VOICE",
        "info",
        re.compile(
            r"\b(?:is|are|was|were|be|been|being)\s+"
            r"(?:\w+\s+)?(?:\w+ed|shown|given|found|seen|known|noted|observed)\b",
            re.IGNORECASE,
        ),
        "Possible passive voice. William writes predominantly in active voice ('Podemos calcular').",
    ),
]

# ---------------------------------------------------------------------------
# Document-level rules (operate on the full text, not line by line)
# ---------------------------------------------------------------------------

def check_em_dash_density(text: str, threshold: int = 3) -> List[Finding]:
    """Flag documents where em dashes exceed `threshold` per ~500 words."""
    findings = []
    word_count = len(text.split())
    pages = max(1, round(word_count / 500))
    count = text.count("—")
    if count > threshold * pages:
        findings.append(Finding(
            rule_id="EM_DASH_DENSITY",
            severity="error",
            line=0,
            col=0,
            excerpt=f"{count} em dashes in ~{pages} page(s)",
            message=(
                f"Em dash density too high: {count} occurrences across ~{pages} page(s) "
                f"(threshold: {threshold}/page). This is a strong AI fingerprint. "
                "Replace most with commas, semicolons, or period breaks."
            ),
        ))
    return findings


def check_synonym_cycling(text: str) -> List[Finding]:
    """Detect synonym cycling for common academic nouns."""
    findings = []
    synonym_groups = [
        ("electron", ["electron", "particle", "charge carrier", "quantum entity",
                      "elétron", "partícula", "portador de carga"]),
        ("model", ["model", "framework", "approach", "paradigm",
                   "modelo", "abordagem", "estrutura"]),
        ("result", ["result", "finding", "outcome", "discovery",
                    "resultado", "achado", "descoberta"]),
    ]
    for concept, synonyms in synonym_groups:
        hits = {}
        for syn in synonyms:
            pattern = re.compile(r"\b" + re.escape(syn) + r"\b", re.IGNORECASE)
            count = len(pattern.findall(text))
            if count:
                hits[syn] = count
        if len(hits) >= 3:
            detail = ", ".join(f"'{s}' x{c}" for s, c in hits.items())
            findings.append(Finding(
                rule_id="SYNONYM_CYCLING",
                severity="warning",
                line=0,
                col=0,
                excerpt=detail,
                message=(
                    f"Possible synonym cycling for '{concept}': {detail}. "
                    "William repeats the clearest word rather than cycling synonyms "
                    "to avoid repetition — that avoidance is an AI tell."
                ),
            ))
    return findings


# ---------------------------------------------------------------------------
# Core scanner
# ---------------------------------------------------------------------------

def scan(text: str) -> List[Finding]:
    findings: List[Finding] = []
    lines = text.splitlines()

    for line_no, line in enumerate(lines, start=1):
        for rule_id, severity, pattern, message in INLINE_RULES:
            for match in pattern.finditer(line):
                findings.append(Finding(
                    rule_id=rule_id,
                    severity=severity,
                    line=line_no,
                    col=match.start() + 1,
                    excerpt=match.group(0),
                    message=message,
                ))

    findings.extend(check_em_dash_density(text))
    findings.extend(check_synonym_cycling(text))

    return findings


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------

SEVERITY_ORDER = {"error": 0, "warning": 1, "info": 2}
SEVERITY_LABEL = {"error": "ERROR  ", "warning": "WARN   ", "info": "INFO   "}
SEVERITY_COLOR = {
    "error":   "\033[31m",   # red
    "warning": "\033[33m",   # yellow
    "info":    "\033[36m",   # cyan
}
RESET = "\033[0m"


def format_finding(f: Finding, use_color: bool = True) -> str:
    sev = f.severity
    color = SEVERITY_COLOR[sev] if use_color else ""
    reset = RESET if use_color else ""
    loc = f"line {f.line}:{f.col}" if f.line else "document"
    return (
        f"{color}{SEVERITY_LABEL[sev]}{reset}"
        f"[{f.rule_id}] {loc} — \"{f.excerpt}\"\n"
        f"         {f.message}"
    )


def report(findings: List[Finding], use_color: bool = True) -> None:
    if not findings:
        print("✓ No AI-tell patterns detected.")
        return

    sorted_findings = sorted(findings, key=lambda f: (SEVERITY_ORDER[f.severity], f.line))

    errors   = sum(1 for f in findings if f.severity == "error")
    warnings = sum(1 for f in findings if f.severity == "warning")
    infos    = sum(1 for f in findings if f.severity == "info")

    print(f"\n{'─'*70}")
    print(f"  AI-tell check results: {errors} error(s), {warnings} warning(s), {infos} info(s)")
    print(f"{'─'*70}\n")

    for f in sorted_findings:
        print(format_finding(f, use_color=use_color))
        print()

    print(f"{'─'*70}")
    if errors:
        print("  ✗ FAIL — errors must be fixed before publishing.")
    elif warnings:
        print("  △ REVIEW — warnings indicate likely AI patterns; review carefully.")
    else:
        print("  ✓ PASS — only informational notes remain.")
    print(f"{'─'*70}\n")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic AI-tell detector for academic writing.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "file",
        nargs="?",
        default="-",
        help="Text file to check, or '-' for stdin (default: stdin)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit with code 1 if any finding is detected (useful in CI/hooks).",
    )
    parser.add_argument(
        "--no-color",
        action="store_true",
        help="Disable ANSI color output.",
    )
    parser.add_argument(
        "--only",
        metavar="SEVERITY",
        choices=["error", "warning", "info"],
        help="Show only findings of this severity level.",
    )
    args = parser.parse_args()

    # Read input
    if args.file == "-":
        text = sys.stdin.read()
        source = "<stdin>"
    else:
        try:
            with open(args.file, encoding="utf-8") as fh:
                text = fh.read()
            source = args.file
        except FileNotFoundError:
            print(f"Error: file not found: {args.file}", file=sys.stderr)
            return 2
        except UnicodeDecodeError:
            print(f"Error: could not decode {args.file} as UTF-8.", file=sys.stderr)
            return 2

    print(f"\nChecking: {source}  ({len(text.split())} words)")

    findings = scan(text)

    if args.only:
        findings = [f for f in findings if f.severity == args.only]

    use_color = not args.no_color and sys.stdout.isatty()
    report(findings, use_color=use_color)

    if args.strict and findings:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
