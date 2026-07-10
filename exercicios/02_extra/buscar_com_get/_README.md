---
Tags: Dicionários
Nível: Iniciante
---

## Objetivo

Praticar o acesso seguro a valores de um dicionário com o método `get`. Diferente do acesso por colchetes, o `get` não gera erro quando a chave não existe, o que torna o código mais robusto.

## Especificação

### Buscar um valor de forma segura

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe os parâmetros `dicionario` (um dicionário) e `chave`. Retorne o valor associado a essa chave. Se a chave **não existir** no dicionário, retorne `None`.

Regras:

- Utilize o método `get` para acessar o valor;

Exemplos:

- `resposta({'nome': 'Ana'}, 'nome')` → `'Ana'`
- `resposta({'nome': 'Ana'}, 'idade')` → `None`

**Atenção:** utilize `return`, não `print`.
