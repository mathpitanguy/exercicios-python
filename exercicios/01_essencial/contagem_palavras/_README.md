---
Tags: Strings, Métodos de String, Dicionários, Laços de Repetição (for)
Nível: Intermediário
---

## Objetivo

Praticar manipulação de strings e uso de dicionários para contagem de dados. Neste exercício, você irá analisar um texto e contar quantas vezes cada palavra aparece.

## Especificação

### Contagem de Palavras

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber uma string e retornar um dicionário onde:

- As chaves são as palavras encontradas no texto
- Os valores são a quantidade de vezes que cada palavra aparece

Regras:

- Converter o texto para minúsculas
- Separar as palavras utilizando `split()`
- Contar quantas vezes cada palavra aparece
- Retornar um dicionário com o resultado

Exemplos:

- `resposta("hoje foi um dia bom hoje foi especial")` → `{'hoje': 2, 'foi': 2, 'um': 1, 'dia': 1, 'bom': 1, 'especial': 1}`
- `resposta("não pare de acreditar")` → `{'não': 1, 'pare': 1, 'de': 1, 'acreditar': 1}`

**Atenção:** utilize `return`, não `print`.
