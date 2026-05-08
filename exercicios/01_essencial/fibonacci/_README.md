---
Tags: Variáveis, Operações Aritméticas, Estruturas Condicionais (if), Laços de Repetição (for), Funções, Parâmetros, Instrução return
Nível: Intermediário
---

## Objetivo

Praticar o uso de laços de repetição e lógica sequencial para gerar uma sequência numérica. Neste exercício, você irá construir a sequência de Fibonacci, onde cada número é a soma dos dois anteriores.

## Especificação

### Geração da Sequência de Fibonacci

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

 A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de Fibonacci. A função deverá receber um número inteiro positivo `n` e retornar o inteiro correspondente `n`da sequência de Fibonacci.

Regras:

- A sequência de Fibonacci começa com:
  - 1, 1
- Cada elemento seguinte é a soma dos dois anteriores
- Se `n` for 1, retornar `[1]`
- Retornar o inteiro `n` da sequência Fibonacci

Exemplos:

- `resposta(1)` → 1
- `resposta(2)` → 1
- `resposta(5)` → 5
- `resposta(7)` → 13

**Atenção:** utilize `return`, não `print`.
