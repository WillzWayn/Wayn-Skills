# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## O que é este repositório

Biblioteca pessoal de Claude Code Skills de willzwayn, publicada como marketplace em `github.com/willzwayn/skills`. Funciona simultaneamente como:

- **Claude Code Plugin Marketplace** — instalável via `/plugin marketplace add willzwayn/skills`
- **skills.sh directory** — instalável via `npx skills add willzwayn/skills`

O formato `SKILL.md` segue o padrão aberto [agentskills.io](https://agentskills.io), compatível com Claude Code, Cursor, Gemini CLI, OpenAI Codex CLI e outros agentes.

---

## Estrutura e convenções

```
willz-skills/
├── .claude-plugin/
│   └── marketplace.json        ← índice global de todos os plugins
├── plugins/
│   ├── _template/              ← template canônico para novos plugins
│   └── <categoria>/            ← um plugin por categoria (ex: latex, python-tools)
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── <nome-skill>/   ← uma pasta por skill
│               ├── SKILL.md    ← obrigatório
│               ├── examples.md ← opcional
│               ├── reference.md← opcional (docs longas vão aqui, não no SKILL.md)
│               └── templates/  ← opcional (arquivos usados pela skill)
```

**Regra de nomes**: tudo em `kebab-case`. O nome da pasta da skill vira o `/slash-command` dentro do namespace do plugin: `/<plugin>:<skill>`.

---

## Como adicionar uma nova skill

### 1. Novo plugin (nova categoria)

```bash
cp -r plugins/_template plugins/<nova-categoria>
```

Edite `plugins/<nova-categoria>/.claude-plugin/plugin.json`:
- `name`: kebab-case, vira o namespace (`/nome:skill`)
- `description`: o que o plugin oferece
- `version`: semver, começa em `"1.0.0"`

Registre em `.claude-plugin/marketplace.json` adicionando ao array `plugins`:
```json
{
  "source": "plugins/<nova-categoria>",
  "description": "Descrição curta",
  "category": "<categoria>",
  "tags": ["tag1", "tag2"]
}
```

### 2. Nova skill dentro de plugin existente

```bash
mkdir -p plugins/<categoria>/skills/<nome-skill>
```

Crie `SKILL.md` baseado em `plugins/_template/skills/my-skill/SKILL.md`.

---

## Anatomia do SKILL.md

```yaml
---
name: nome-da-skill           # opcional: se omitido, usa o nome da pasta
description: >                # CRÍTICO — Claude usa isto para auto-invocar
  O que a skill faz e quando usar. Seja específico, mencione palavras-chave
  que o usuário usaria naturalmente.
disable-model-invocation: false  # true = só o usuário pode invocar (/nome)
allowed-tools: Read, Write       # opcional: ferramentas sem confirmação
context: fork                    # opcional: roda em subagente isolado
agent: Explore                   # opcional: tipo do subagente (com context: fork)
---
```

**Regras de qualidade:**
- `description` é o campo mais importante — sem ele, a skill nunca será invocada automaticamente
- Mantenha `SKILL.md` abaixo de 500 linhas — mova docs longas para `reference.md`
- Use `disable-model-invocation: true` para skills com efeitos colaterais (deploy, email, etc.)
- Referencie arquivos de suporte explicitamente no corpo: `veja [reference.md](reference.md)`
- Argumentos do usuário ficam disponíveis via `$ARGUMENTS`, `$0`, `$1`, etc.

---

## Testar localmente antes de publicar

```bash
# Testar um plugin isolado
claude --plugin-dir ./plugins/<nome-plugin>

# Verificar quais skills o skills.sh detecta
npx skills add . --list

# Dentro do Claude Code, recarregar após edições
/reload-plugins
```

---

## Publicar

```bash
git add .
git commit -m "feat(<categoria>): add <nome-skill>"
git push
```

Após o push, disponível para instalação:
```bash
# Claude Code
/plugin marketplace add willzwayn/skills
/plugin install <categoria>@willzwayn-skills

# skills.sh / qualquer agente compatível
npx skills add willzwayn/skills
```

---

## Categorias existentes

| Plugin | Skills | Descrição |
|--------|--------|-----------|
| `latex` | `cv`, `presentation` | Documentos LaTeX profissionais |

---

## Frontmatter de referência rápida

| Campo | Obrigatório | Efeito |
|-------|-------------|--------|
| `name` | não | display name e slash-command (padrão: nome da pasta) |
| `description` | recomendado | Claude usa para auto-invocar |
| `disable-model-invocation` | não | `true` = só usuário invoca |
| `user-invocable` | não | `false` = só Claude invoca (background knowledge) |
| `allowed-tools` | não | ferramentas sem confirmação quando a skill está ativa |
| `model` | não | modelo específico para esta skill |
| `effort` | não | `low/medium/high/max` |
| `context` | não | `fork` = roda em subagente isolado |
| `agent` | não | tipo do subagente (`Explore`, `Plan`, `general-purpose`) |
