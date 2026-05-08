---
Tags: Variáveis, Operações Aritméticas
Nível: Iniciante
---

## Objetivo

Praticar conversão de valores utilizando fórmulas matemáticas. Neste exercício, você irá converter temperaturas entre as escalas Celsius e Fahrenheit.

## Especificação

### Conversão de Temperatura

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber dois valores:

- Um valor numérico representando a temperatura
- Uma string indicando o tipo de conversão:
  - `"C"` para converter de Celsius para Fahrenheit
  - `"F"` para converter de Fahrenheit para Celsius

E deverá retornar o valor da temperatura convertida.

Regras:

- Para converter de Celsius para Fahrenheit:
  - F = (9 × C / 5) + 32
- Para converter de Fahrenheit para Celsius:
  - C = (F - 32) × 5 / 9
- A função deve verificar o tipo de conversão informado
- Retornar apenas o valor convertido

Exemplos:

- `resposta(0, "C")` → `32`
- `resposta(32, "F")` → `0`
- `resposta(100, "C")` → `212`

**Atenção:** utilize `return`, não `print`.
