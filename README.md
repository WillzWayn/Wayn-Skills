# willz-skills

Marketplace pessoal de Claude Code Skills.
Publicado em `github.com/willzwayn/skills`.

---

## Estrutura do repositório

```
willz-skills/
├── .claude-plugin/
│   └── marketplace.json        ← índice de todos os plugins
├── plugins/
│   ├── _template/              ← copie este para criar um novo plugin
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   └── skills/
│   │       └── my-skill/
│   │           └── SKILL.md
│   └── latex/                  ← plugin de exemplo (LaTeX)
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

## Como usar (instalação)

### 1. Adicionar o marketplace ao Claude Code

```bash
/plugin marketplace add willzwayn/skills
```

### 2. Instalar um plugin específico

```bash
/plugin install latex@willzwayn-skills
```

### 3. Invocar uma skill

```bash
/latex:cv
/latex:presentation
```

### 4. Atualizar plugins

```bash
/plugin update latex@willzwayn-skills
```

---

## Como criar um novo plugin (passo a passo)

### Passo 1 — Copie o template

```bash
cp -r plugins/_template plugins/meu-novo-plugin
```

### Passo 2 — Edite o `plugin.json`

Abra `plugins/meu-novo-plugin/.claude-plugin/plugin.json` e preencha:
- `name`: identificador único (kebab-case, ex: `latex`, `python-tools`)
- `description`: o que o plugin faz
- `version`: comece em `"1.0.0"`

### Passo 3 — Crie as skills

Dentro de `plugins/meu-novo-plugin/skills/`, cada pasta vira uma skill:

```
skills/
└── minha-skill/          ← nome do /slash-command
    ├── SKILL.md          ← obrigatório
    ├── examples.md       ← opcional: exemplos de uso
    ├── reference.md      ← opcional: docs detalhadas
    └── templates/        ← opcional: arquivos de template
        └── template.txt
```

### Passo 4 — Escreva o `SKILL.md`

Veja o template em `plugins/_template/skills/my-skill/SKILL.md`.

Regras importantes:
- `description` é o campo mais crítico — o Claude usa ele para decidir quando invocar a skill automaticamente
- Seja específico: mencione casos de uso reais e palavras-chave que o usuário usaria
- Mantenha o `SKILL.md` abaixo de 500 linhas; mova docs detalhadas para `reference.md`

### Passo 5 — Registre no marketplace

Abra `.claude-plugin/marketplace.json` e adicione uma entrada no array `plugins`:

```json
{
  "source": "plugins/meu-novo-plugin",
  "description": "Descrição curta do plugin",
  "category": "development"
}
```

### Passo 6 — Teste localmente

```bash
claude --plugin-dir ./plugins/meu-novo-plugin
```

Dentro do Claude Code:
```bash
/meu-novo-plugin:minha-skill
```

### Passo 7 — Commit e push

```bash
git add .
git commit -m "feat: add meu-novo-plugin"
git push
```

Pronto. Qualquer pessoa pode instalar com `/plugin marketplace add willzwayn/skills`.

---

## Referências

- [Documentação oficial de Skills](https://code.claude.com/docs/en/skills)
- [Documentação de Plugins](https://code.claude.com/docs/en/plugins)
- [Criar Marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Padrão aberto agentskills.io](https://agentskills.io)
- [anthropics/skills (repositório oficial)](https://github.com/anthropics/skills)
