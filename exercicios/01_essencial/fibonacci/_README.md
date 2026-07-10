---
Tags: Laços de Repetição (for), Operações Aritméticas
Nível: Intermediário
---

## Objetivo

Praticar o uso de laços de repetição e lógica sequencial para gerar uma sequência numérica. Neste exercício, você irá construir a sequência de Fibonacci, em que cada número é a soma dos dois anteriores.

## Especificação

### Geração da Sequência de Fibonacci

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A sequência de Fibonacci é: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... A regra de formação é simples: os dois primeiros elementos valem 1 e, a partir daí, cada elemento é a soma dos dois anteriores.

A função recebe o parâmetro `n` (um número inteiro positivo) e deve retornar o **n-ésimo** número da sequência, ou seja, o elemento que está na posição `n`. Por exemplo, o 7º elemento da sequência é `13`.

Regras:

- Os dois primeiros elementos da sequência (posições 1 e 2) valem `1`
- Cada elemento seguinte é a soma dos dois anteriores
- Considere que `n` é sempre um inteiro positivo (`n >= 1`)
- Retorne um número inteiro (o elemento na posição `n`), e não uma lista

Exemplos:

- `resposta(1)` → `1`
- `resposta(2)` → `1`
- `resposta(5)` → `5`
- `resposta(7)` → `13`
- `resposta(10)` → `55`

**Atenção:** utilize `return`, não `print`.
