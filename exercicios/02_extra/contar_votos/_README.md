---
Tags: Dicionários, Listas, Laços de Repetição (for)
Nível: Intermediário
---

## Objetivo

Praticar o uso de um dicionário como **contador**, combinando dicionários com a varredura de uma lista. Contar quantas vezes cada item aparece é um padrão muito usado em apuração de dados e estatísticas simples.

## Especificação

### Contar a frequência de cada opção

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe o parâmetro `votos` (uma lista de textos). Retorne um dicionário em que cada **chave** é uma opção que apareceu na lista e cada **valor** é a quantidade de vezes que essa opção apareceu.

Regras:

- Percorra a lista e vá montando o dicionário de contagem;
- Uma opção que aparece pela primeira vez começa com contagem `1`;
- Se a lista estiver vazia, retorne um dicionário vazio (`{}`).

Exemplos:

- `resposta(['A', 'B', 'A', 'C', 'A'])` → `{'A': 3, 'B': 1, 'C': 1}`
- `resposta(['sim', 'sim', 'não'])` → `{'sim': 2, 'não': 1}`
- `resposta([])` → `{}`

**Atenção:** utilize `return`, não `print`.
