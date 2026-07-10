---
Tags: Laços de Repetição (while), Listas, Estruturas Condicionais (if)
Nível: Intermediário
---

## Objetivo

Praticar o `while` com uma **condição de parada por sentinela** - o laço continua repetindo até encontrar um valor especial que sinaliza o fim. Esse padrão é a base de menus e leituras que se repetem até o usuário decidir parar.

## Especificação

### Soma até o valor de parada

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe o parâmetro `numeros` (uma lista de números inteiros). Percorra a lista com um laço `while`, somando os valores, e **pare assim que encontrar o número `0`**. O `0` funciona como sinal de parada e **não** deve ser incluído na soma. A função deve retornar a soma obtida.


Regras:

- Utilize obrigatoriamente o laço `while`;
- Pare ao encontrar o **primeiro** `0` e não some esse `0`;
- Se a lista não contiver nenhum `0`, some todos os elementos.

Exemplos:

- `resposta([4, 7, 2, 0, 9])` → `13`
- `resposta([1, 2, 3])` → `6`
- `resposta([0, 5])` → `0`

**Atenção:** utilize `return`, não `print`.
