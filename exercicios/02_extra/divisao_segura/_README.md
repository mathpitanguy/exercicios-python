---
Tags: Tratamento de Exceções, Operações Aritméticas
Nível: Intermediário
---

## Objetivo

Praticar o tratamento de erros com `try` e `except`. Em vez de deixar o programa quebrar diante de uma operação inválida, aprendemos a capturar o erro e a devolver uma resposta controlada.

## Especificação

### Divisão segura

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe os parâmetros `a` e `b` (dois números) e deve retornar o resultado da divisão de `a` por `b`. Como a divisão por zero gera um erro, proteja a operação: se `b` for `0`, capture o erro e retorne `None`.

Regras:

- Coloque a divisão dentro de um bloco `try`;
- No `except`, capture o erro `ZeroDivisionError`;
- Em caso de divisão por zero, retorne `None`.

Exemplos:

- `resposta(10, 2)` → `5.0`
- `resposta(9, 3)` → `3.0`
- `resposta(5, 0)` → `None`

**Atenção:** utilize `return`, não `print`.
