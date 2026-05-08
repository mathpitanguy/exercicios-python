---
Tags: Variáveis, Operações Aritméticas, Funções Matemáticas, Estruturas Condicionais (if), Tuplas
Nível: Iniciante
---

## Objetivo

Praticar cálculos matemáticos aplicados a problemas do mundo real, incluindo arredondamento e divisão. Neste exercício, você irá calcular a quantidade de tinta necessária para pintar uma área e o custo total da compra.

## Especificação

### Cálculo de Tinta Necessária

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber um valor numérico representando o tamanho da área a ser pintada (em metros quadrados) e retornar uma tupla contendo:

- A quantidade de latas de tinta a serem compradas
- O preço total da compra

Regras:

- 1 litro de tinta cobre 3 m²
- Cada lata possui 18 litros
- Cada lata custa R$ 80,00
- Calcular a quantidade total de litros necessários
- Calcular a quantidade de latas necessárias (arredondando sempre para cima, pois só é possível comprar latas inteiras)
- Calcular o preço total com base na quantidade de latas

Exemplos:

- `resposta(54)` → `(1, 80)`
- `resposta(60)` → `(2, 160)`

**Atenção:** utilize `return`, não `print`.
