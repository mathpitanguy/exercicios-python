---
Tags: Laços de Repetição (while), Listas
Nível: Iniciante
---

## Objetivo

Praticar o laço `while` controlado por um contador que diminui a cada repetição. Saber montar a condição de parada de um `while` é a base para qualquer rotina que precise repetir uma ação um número definido de vezes.

## Especificação

### Contagem regressiva

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe o parâmetro `n` (um número inteiro) e deve retornar uma **lista** com os números de `n` até `1`, em ordem decrescente. A lista deve ser construída usando um laço `while`.

Regras:

- Utilize obrigatoriamente o laço `while`;
- Não utilize `range()` nem o laço `for`;
- Se `n` for menor que `1`, retorne uma lista vazia (`[]`).

Exemplos:

- `resposta(5)` → `[5, 4, 3, 2, 1]`
- `resposta(1)` → `[1]`
- `resposta(0)` → `[]`

**Atenção:** utilize `return`, não `print`.
