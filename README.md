# Wayn-Skills

Personal Claude Code Skills marketplace.
Published at `github.com/WillzWayn/Wayn-Skills`.

---

## Repository structure

```
Wayn-Skills/
├── .claude-plugin/
│   └── marketplace.json        ← index of all plugins and skills
├── skills/
│   └── latex/                  ← LaTeX document skills
│       ├── SKILL.md
│       ├── cv.md
│       ├── presentation.md
│       ├── academic-report.md
│       └── bibtex.md
└── README.md
```

---

## How to use (installation)

### 1. Install the plugin in Claude Code

```bash
/install-plugin WillzWayn/Wayn-Skills
```

### 2. Invoke a skill

```bash
/latex-skills:latex
```

### 3. Update the plugin

```bash
/update-plugin WillzWayn/Wayn-Skills
```

---

## How to create a new skill (step by step)

### Step 1 — Create the skill folder

```bash
mkdir -p skills/my-new-skill
```

### Step 2 — Write the `SKILL.md`

Create `skills/my-new-skill/SKILL.md` with frontmatter and instructions.

Important rules:

- `name` and `description` are **required** in the frontmatter — without both, `npx skills add` won't detect the skill
- `description` is what Claude uses to decide when to automatically invoke the skill
- Be specific: mention real use cases and keywords the user would use
- Keep `SKILL.md` under 500 lines; move detailed docs to `reference.md`

### Step 3 — Register in the marketplace

Open `.claude-plugin/marketplace.json` and either add the skill path to an existing plugin's `skills` array, or create a new plugin entry:

```json
{
  "name": "my-plugin",
  "source": "./",
  "description": "Short plugin description",
  "strict": false,
  "skills": [
    "./skills/my-new-skill"
  ]
}
```

### Step 4 — Test locally

```bash
npx skills add . --list
```

### Step 5 — Commit and push

```bash
git add .
git commit -m "feat: add my-new-skill"
git push
```

Done. Anyone can install with `/install-plugin WillzWayn/Wayn-Skills`.

---

## References

- [Official Skills Documentation](https://code.claude.com/docs/en/skills)
- [Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Creating Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [agentskills.io open standard](https://agentskills.io)
- [anthropics/skills (official repository)](https://github.com/anthropics/skills)
