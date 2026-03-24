# willz-skills

Personal Claude Code Skills marketplace.
Published at `github.com/willzwayn/skills`.

---

## Repository structure

```
willz-skills/
├── .claude-plugin/
│   └── marketplace.json        ← index of all plugins
├── plugins/
│   ├── _template/              ← copy this to create a new plugin
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   │       └── my-skill/
│   │           └── SKILL.md
│   └── latex/                  ← example plugin (LaTeX)
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           ├── presentation/
│           │   └── SKILL.md
│           └── cv/
│               └── SKILL.md
└── README.md
```

---

## How to use (installation)

### 1. Add the marketplace to Claude Code

```bash
/plugin marketplace add willzwayn/skills
```

### 2. Install a specific plugin

```bash
/plugin install latex@willzwayn-skills
```

### 3. Invoke a skill

```bash
/latex:cv
/latex:presentation
```

### 4. Update plugins

```bash
/plugin update latex@willzwayn-skills
```

---

## How to create a new plugin (step by step)

### Step 1 — Copy the template

```bash
cp -r plugins/_template plugins/my-new-plugin
```

### Step 2 — Edit the `plugin.json`

Open `plugins/my-new-plugin/.claude-plugin/plugin.json` and fill in:
- `name`: unique identifier (kebab-case, e.g.: `latex`, `python-tools`)
- `description`: what the plugin does
- `version`: start at `"1.0.0"`

### Step 3 — Create the skills

Inside `plugins/my-new-plugin/skills/`, each folder becomes a skill:

```
skills/
└── my-skill/             ← name of the /slash-command
    ├── SKILL.md          ← required
    ├── examples.md       ← optional: usage examples
    ├── reference.md      ← optional: detailed docs
    └── templates/        ← optional: template files
        └── template.txt
```

### Step 4 — Write the `SKILL.md`

See the template at `plugins/_template/skills/my-skill/SKILL.md`.

Important rules:
- `description` is the most critical field — Claude uses it to decide when to automatically invoke the skill
- Be specific: mention real use cases and keywords the user would use
- Keep `SKILL.md` under 500 lines; move detailed docs to `reference.md`

### Step 5 — Register in the marketplace

Open `.claude-plugin/marketplace.json` and add an entry to the `plugins` array:

```json
{
  "source": "plugins/my-new-plugin",
  "description": "Short plugin description",
  "category": "development"
}
```

### Step 6 — Test locally

```bash
claude --plugin-dir ./plugins/my-new-plugin
```

Inside Claude Code:
```bash
/my-new-plugin:my-skill
```

### Step 7 — Commit and push

```bash
git add .
git commit -m "feat: add my-new-plugin"
git push
```

Done. Anyone can install with `/plugin marketplace add willzwayn/skills`.

---

## References

- [Official Skills Documentation](https://code.claude.com/docs/en/skills)
- [Plugins Documentation](https://code.claude.com/docs/en/plugins)
- [Creating Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [agentskills.io open standard](https://agentskills.io)
- [anthropics/skills (official repository)](https://github.com/anthropics/skills)
