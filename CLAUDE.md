# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What is this repository

Personal Claude Code Skills library by willzwayn, published as a marketplace at `github.com/willzwayn/skills`. It works simultaneously as:

- **Claude Code Plugin Marketplace** — installable via `/plugin marketplace add willzwayn/skills`
- **skills.sh directory** — installable via `npx skills add willzwayn/skills`

The `SKILL.md` format follows the open standard [agentskills.io](https://agentskills.io), compatible with Claude Code, Cursor, Gemini CLI, OpenAI Codex CLI, and other agents.

---

## Structure and conventions

```
willz-skills/
├── .claude-plugin/
│   └── marketplace.json        ← global index of all plugins
├── plugins/
│   ├── _template/              ← canonical template for new plugins
│   └── <category>/             ← one plugin per category (e.g.: latex, python-tools)
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── <skill-name>/   ← one folder per skill
│               ├── SKILL.md    ← required
│               ├── examples.md ← optional
│               ├── reference.md← optional (long docs go here, not in SKILL.md)
│               └── templates/  ← optional (files used by the skill)
```

**Naming rule**: everything in `kebab-case`. The skill folder name becomes the `/slash-command` within the plugin namespace: `/<plugin>:<skill>`.

---

## How to add a new skill

### 1. New plugin (new category)

```bash
cp -r plugins/_template plugins/<new-category>
```

Edit `plugins/<new-category>/.claude-plugin/plugin.json`:
- `name`: kebab-case, becomes the namespace (`/name:skill`)
- `description`: what the plugin offers
- `version`: semver, starts at `"1.0.0"`

Register in `.claude-plugin/marketplace.json` by adding to the `plugins` array:
```json
{
  "source": "plugins/<new-category>",
  "description": "Short description",
  "category": "<category>",
  "tags": ["tag1", "tag2"]
}
```

### 2. New skill within an existing plugin

```bash
mkdir -p plugins/<category>/skills/<skill-name>
```

Create `SKILL.md` based on `plugins/_template/skills/my-skill/SKILL.md`.

---

## SKILL.md anatomy

```yaml
---
name: skill-name              # optional: if omitted, uses the folder name
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
# Test an isolated plugin
claude --plugin-dir ./plugins/<plugin-name>

# Check which skills skills.sh detects
npx skills add . --list

# Inside Claude Code, reload after edits
/reload-plugins
```

---

## Publish

```bash
git add .
git commit -m "feat(<category>): add <skill-name>"
git push
```

After pushing, available for installation:
```bash
# Claude Code
/plugin marketplace add willzwayn/skills
/plugin install <category>@willzwayn-skills

# skills.sh / any compatible agent
npx skills add willzwayn/skills
```

---

## Existing categories

| Plugin | Skills | Description |
|--------|--------|-------------|
| `latex` | `cv`, `presentation` | Professional LaTeX documents |

---

## Quick reference frontmatter

| Field | Required | Effect |
|-------|----------|--------|
| `name` | no | display name and slash-command (default: folder name) |
| `description` | recommended | Claude uses this to auto-invoke |
| `disable-model-invocation` | no | `true` = only user invokes |
| `user-invocable` | no | `false` = only Claude invokes (background knowledge) |
| `allowed-tools` | no | tools without confirmation when skill is active |
| `model` | no | specific model for this skill |
| `effort` | no | `low/medium/high/max` |
| `context` | no | `fork` = runs in isolated subagent |
| `agent` | no | subagent type (`Explore`, `Plan`, `general-purpose`) |
