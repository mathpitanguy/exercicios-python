---
Tags: Variáveis, Operações Aritméticas, Operadores de Comparação, Laços de Repetição (while)
Nível: Intermediário
---

## Objetivo

Praticar o uso de laços de repetição e lógica matemática para resolver problemas clássicos. Neste exercício, você irá aplicar o algoritmo de Euclides para encontrar o máximo divisor comum (MDC) entre dois números.

## Especificação

### Cálculo do Máximo Divisor Comum (MDC)

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber dois números inteiros positivos e retornar o valor do máximo divisor comum (MDC) entre eles.

Regras:

- Utilizar o algoritmo de Euclides:
  - Enquanto o segundo número for diferente de zero:
    - Substituir o primeiro número pelo segundo
    - Substituir o segundo número pelo resto da divisão entre o primeiro e o segundo
- Quando o segundo número for zero, o primeiro número será o MDC
- Retornar o valor encontrado

Exemplos:

- `resposta(12, 8)` → `4`
- `resposta(15, 5)` → `5`
- `resposta(21, 14)` → `7`

**Atenção:** utilize `return`, não `print`.
