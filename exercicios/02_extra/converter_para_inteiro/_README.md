---
Tags: Tratamento de Exceções, Conversão de Tipos
Nível: Intermediário
---

## Objetivo

Praticar `try` e `except` ao converter texto em número. Conversões a partir de dados digitados podem falhar quando o texto não representa um número, e tratar essa falha evita que o programa quebre.

## Especificação

### Converter texto para inteiro com segurança

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe o parâmetro `texto` (uma string). Tente convertê-lo para um número inteiro com `int()`. Se a conversão for bem-sucedida, retorne o número inteiro. Se o texto não representar um inteiro válido, capture o erro e retorne `"Valor inválido"`.


Regras:

- Coloque a conversão dentro de um bloco `try`;
- No `except`, capture o erro `ValueError`;
- Se a conversão falhar, retorne `"Valor inválido"`.

Exemplos:

- `resposta('2020')` → `2020`
- `resposta('abc')` → `"Valor inválido"`
- `resposta('12.5')` → `"Valor inválido"`

**Atenção:** utilize `return`, não `print`.
