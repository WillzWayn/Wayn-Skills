---
# OBRIGATÓRIO (recomendado): Claude usa isto para decidir quando invocar a skill.
# Seja específico: inclua casos de uso reais e palavras que o usuário usaria.
description: >
  Descreva o que a skill faz e quando usá-la.
  Exemplo: "Cria um relatório em PDF. Use quando o usuário pedir para gerar
  um relatório, sumário executivo, ou documento formal."

# OPCIONAL: impede o Claude de invocar automaticamente.
# Use true para skills com efeitos colaterais (deploy, envio de email, etc.)
disable-model-invocation: false

# OPCIONAL: ferramentas que a skill pode usar sem pedir permissão.
# allowed-tools: Bash(pdflatex *), Read, Write

# OPCIONAL: roda em subagente isolado (não acessa histórico da conversa).
# context: fork
# agent: Explore
---

# Nome da Skill

Breve descrição do que esta skill faz.

## Como usar

Invoque com `/plugin-name:my-skill [argumentos]`

O argumento passado fica disponível em `$ARGUMENTS`.

## Instruções

Escreva aqui as instruções passo a passo que o Claude deve seguir.

1. Passo 1
2. Passo 2
3. Passo 3

## Recursos adicionais

- Para detalhes de API, veja [reference.md](reference.md)  ← crie se necessário
- Para exemplos, veja [examples.md](examples.md)           ← crie se necessário
