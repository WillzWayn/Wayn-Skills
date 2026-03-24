---
# REQUIRED (recommended): Claude uses this to decide when to invoke the skill.
# Be specific: include real use cases and words the user would use.
description: >
  Describe what the skill does and when to use it.
  Example: "Creates a PDF report. Use when the user asks to generate
  a report, executive summary, or formal document."

# OPTIONAL: prevents Claude from invoking automatically.
# Use true for skills with side effects (deploy, sending email, etc.)
disable-model-invocation: false

# OPTIONAL: tools the skill can use without asking permission.
# allowed-tools: Bash(pdflatex *), Read, Write

# OPTIONAL: runs in an isolated subagent (no access to conversation history).
# context: fork
# agent: Explore
---

# Skill Name

Brief description of what this skill does.

## How to use

Invoke with `/plugin-name:my-skill [arguments]`

The argument passed is available in `$ARGUMENTS`.

## Instructions

Write step-by-step instructions for Claude to follow here.

1. Step 1
2. Step 2
3. Step 3

## Additional resources

- For API details, see [reference.md](reference.md)  ← create if needed
- For examples, see [examples.md](examples.md)        ← create if needed
