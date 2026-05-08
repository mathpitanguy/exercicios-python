---
Tags: Variáveis, Operações Aritméticas, Estruturas Condicionais (if), Operadores de Comparação, Tuplas
Nível: Iniciante
---

## Objetivo

Praticar o uso de variáveis, operadores aritméticos e estruturas condicionais para resolver um problema do mundo real. Neste exercício, você irá calcular o excesso de peso de peixes e a multa correspondente, com base em uma regra definida.

## Especificação

### Cálculo de Excesso de Peso e Multa

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber um valor numérico representando o peso de peixes (em quilos) e retornar uma tupla contendo dois valores:

- O excesso de peso (em quilos)
- O valor da multa (em reais)

Regras:

- O limite permitido de peso é 50 kg
- Se o peso for maior que 50 kg:
  - O excesso é a diferença entre o peso e 50
  - A multa é calculada como R$ 4,00 por quilo excedente
- Caso o peso seja menor ou igual a 50 kg:
  - O excesso deve ser 0
  - A multa deve ser 0

Exemplos:

- `resposta(60)` → `(10, 40)`
- `resposta(50)` → `(0, 0)`
- `resposta(45)` → `(0, 0)`

**Atenção:** utilize `return`, não `print`.
