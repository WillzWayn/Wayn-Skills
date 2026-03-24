# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is this repository

Personal Claude Code Skills library by willzwayn, published as a marketplace at `github.com/WillzWayn/Wayn-Skills`. It works simultaneously as:

- **Claude Code Plugin Marketplace** — installable via `/install-plugin WillzWayn/Wayn-Skills`
- **skills.sh directory** — installable via `npx skills add WillzWayn/Wayn-Skills`

The `SKILL.md` format follows the open standard [agentskills.io](https://agentskills.io), compatible with Claude Code, Cursor, Gemini CLI, OpenAI Codex CLI, and other agents.

---

## Structure and conventions

```
Wayn-Skills/
├── .claude-plugin/
│   └── marketplace.json        ← global index of all plugins and skills
├── skills/
│   └── <skill-name>/           ← one folder per skill
│       ├── SKILL.md            ← required
│       ├── examples.md         ← optional
│       ├── reference.md        ← optional (long docs go here, not in SKILL.md)
│       └── templates/          ← optional (files used by the skill)
└── README.md
```

**Naming rule**: everything in `kebab-case`. The skill folder name becomes the `/slash-command` within the plugin namespace: `/<plugin>:<skill>`.

---

## How to add a new skill

### 1. Create the skill folder

```bash
mkdir -p skills/<skill-name>
```

### 2. Write the `SKILL.md`

Create `skills/<skill-name>/SKILL.md` with the appropriate frontmatter and instructions.

### 3. Register in the marketplace

Open `.claude-plugin/marketplace.json` and add the skill path to the appropriate plugin's `skills` array:

```json
{
  "name": "my-plugin",
  "source": "./",
  "description": "Short description",
  "strict": false,
  "skills": [
    "./skills/<skill-name>"
  ]
}
```

Or create a new plugin entry if it belongs to a new category.

---

## SKILL.md anatomy

```yaml
---
name: skill-name              # REQUIRED for skills.sh compatibility
description: >                # CRITICAL — Claude uses this to auto-invoke
  What the skill does and when to use it. Be specific, mention keywords
  the user would naturally use.
disable-model-invocation: false  # true = only the user can invoke (/name)
allowed-tools: Read, Write       # optional: tools without confirmation
context: fork                    # optional: runs in an isolated subagent
agent: Explore                   # optional: subagent type (with context: fork)
---
```

**Quality rules:**

- `description` is the most important field — without it, the skill will never be auto-invoked
- Keep `SKILL.md` under 500 lines — move long docs to `reference.md`
- Use `disable-model-invocation: true` for skills with side effects (deploy, email, etc.)
- Reference support files explicitly in the body: `see [reference.md](reference.md)`
- User arguments are available via `$ARGUMENTS`, `$0`, `$1`, etc.

---

## Test locally before publishing

```bash
# Check which skills skills.sh detects
npx skills add . --list

# Inside Claude Code, reload after edits
/reload-plugins
```

---

## Publish

```bash
git add .
git commit -m "feat: add <skill-name>"
git push
```

After pushing, available for installation:

```bash
# Claude Code
/install-plugin WillzWayn/Wayn-Skills

# skills.sh / any compatible agent
npx skills add WillzWayn/Wayn-Skills
```

---

## Existing skills

| Plugin | Skills | Description |
|--------|--------|-------------|
| `latex-skills` | `latex` | Professional LaTeX documents (CVs, presentations, academic reports, BibTeX) |
| `writing-skills` | `my-academic-writing` | Replicates William Wayn's personal academic writing voice and argumentation style |

---

## Quick reference frontmatter

| Field | Required | Effect |
|-------|----------|--------|
| `name` | **yes** | display name and slash-command — required for `npx skills` compatibility |
| `description` | recommended | Claude uses this to auto-invoke |
| `disable-model-invocation` | no | `true` = only user invokes |
| `user-invocable` | no | `false` = only Claude invokes (background knowledge) |
| `allowed-tools` | no | tools without confirmation when skill is active |
| `model` | no | specific model for this skill |
| `effort` | no | `low/medium/high/max` |
| `context` | no | `fork` = runs in isolated subagent |
| `agent` | no | subagent type (`Explore`, `Plan`, `general-purpose`) |
