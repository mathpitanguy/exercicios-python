---
Tags: Dicionários
Nível: Iniciante
---

## Objetivo

Praticar a criação de um dicionário com pares **chave: valor**. Dicionários são a forma mais natural de representar um registro com vários campos identificados por nome.

## Especificação

### Montar um dicionário de pessoa

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe os parâmetros `nome`, `idade` e `cidade`. Monte e retorne um dicionário com exatamente estas três chaves: `'nome'`, `'idade'` e `'cidade'`, associadas aos valores recebidos.

Regras:

- As chaves devem ser exatamente `'nome'`, `'idade'` e `'cidade'`.
- Cada chave deve receber o valor correspondente passado para a função.

Exemplos:

- `resposta('Ana', 30, 'Belo Horizonte')` → `{'nome': 'Ana', 'idade': 30, 'cidade': 'Belo Horizonte'}`
- `resposta('João', 25, 'Poços de Caldas')` → `{'nome': 'João', 'idade': 25, 'cidade': 'Poços de Caldas'}`

**Atenção:** utilize `return`, não `print`.
