---
Tags: Laços de Repetição (while), Operações Aritméticas, Operadores de Comparação
Nível: Intermediário
---

## Objetivo

Praticar laços de repetição para simular crescimento ao longo do tempo. Neste exercício, você irá calcular em quantos anos uma população alcança outra, aplicando taxas de crescimento anuais e repetindo o cálculo com um laço `while`.

## Especificação

### Crescimento Populacional

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe quatro parâmetros: `populacao_a` e `taxa_a` (a população inicial e a taxa de crescimento anual, em %, do país A) e `populacao_b` e `taxa_b` (os mesmos dados do país B). Ela deve retornar um número inteiro com a quantidade de anos necessários para que a população de A se torne **maior ou igual** à de B.

A cada ano, cada população cresce conforme a sua taxa. Por exemplo, uma população de `1000` com taxa de `3` (3%) passa a `1000 * (1 + 3/100) = 1030` no ano seguinte.

Regras:

- A cada ano, atualize as duas populações com base em suas taxas de crescimento;
- Utilize um laço `while` que continue enquanto a população de A for menor que a de B;
- Conte e retorne o número de anos necessários;
- Se a população de A já for maior ou igual à de B no início, retorne `0`;
- Considere que a taxa de A é maior que a de B, de modo que A sempre alcança B.

Exemplos:

- `resposta(80000, 3, 200000, 1.5)` → `63`
- `resposta(1000, 10, 5000, 2)` → `22`
- `resposta(500, 4, 300, 2)` → `0`

**Atenção:** utilize `return`, não `print`.
