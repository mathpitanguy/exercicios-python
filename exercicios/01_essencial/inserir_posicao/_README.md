---
Tags: Métodos de Lista, Listas
Nível: Iniciante
---

## Objetivo

Praticar o método `insert`, que adiciona um item em uma **posição específica** da lista, deslocando os demais para a direita. Diferente do `append`, ele permite controlar exatamente onde o novo item entra.

## Especificação

### Inserir item em uma posição

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe os parâmetros `lista` (uma lista), `indice` (um número inteiro) e `item` (o valor a ser inserido). Insira o `item` na posição indicada por `indice` e retorne a lista resultante. Os itens que estavam a partir dessa posição devem ser deslocados para a direita.

Regras:

- Utilize o método `insert`;
- O `indice` indica a posição em que o novo item deve ficar;
- Considere que o `indice` informado é sempre válido para a lista.

Exemplos:

- `resposta(['banana', 'manga'], 1, 'laranja')` → `['banana', 'laranja', 'manga']`
- `resposta(['b', 'c'], 0, 'a')` → `['a', 'b', 'c']`

**Atenção:** utilize `return`, não `print`.
