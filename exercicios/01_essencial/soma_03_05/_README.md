## Objetivo

Este exercício trabalha raciocínio matemático e iteração. A ideia é somar todos os números menores que n que sejam múltiplos de 3 ou de 5 — um desafio clássico usado em cursos e entrevistas para treinar loops e condições.

## Especificação
### Some os múltiplos de 3 ou 5 abaixo de n

Abra o arquivo `main.py` e localize a função `resposta`.
Sua função deverá receber um inteiro positivo n e retornar a soma de todos os múltiplos de 3 ou de 5 abaixo desse número.

Siga estas regras:

- Considere apenas os valores estritamente menores que n.
- Inclua na soma números múltiplos de 3, de 5 ou de ambos.

Alguns exemplos:

- soma(5) → 3
- soma(10) → 23 (3 + 5 + 6 + 9)
- soma(20) → 78 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18)

Use sempre return, não print.