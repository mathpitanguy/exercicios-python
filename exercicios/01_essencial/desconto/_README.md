---
Tags: Variáveis, Operações Aritméticas, Tuplas
Nível: Iniciante
---

## Objetivo

Praticar cálculos com porcentagem e manipulação de valores numéricos. Neste exercício, você irá calcular o valor de desconto aplicado a um produto e o preço final a ser pago.

## Especificação

### Cálculo de Desconto

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber dois valores numéricos:

- O preço da mercadoria
- O percentual de desconto

E deverá retornar uma tupla contendo:

- O valor do desconto
- O preço final a pagar

Regras:

- Calcular o valor do desconto:
  - desconto = preço × (percentual / 100)
- Calcular o preço final:
  - preço final = preço - desconto
- Retornar os dois valores na ordem especificada

Exemplos:

- `resposta(100, 10)` → `(10, 90)`
- `resposta(200, 25)` → `(50, 150)`

**Atenção:** utilize `return`, não `print`.
