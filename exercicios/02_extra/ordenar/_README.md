---
Tags: Métodos de Lista, Listas
Nível: Iniciante
---

## Objetivo

Praticar a ordenação de listas com o método `sort`. Ordenar dados é essencial para gerar relatórios legíveis, encontrar mínimos e máximos e organizar resultados.

## Especificação

### Ordenar uma lista

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe o parâmetro `lista` e deve retorná-la com os elementos em **ordem crescente**. Para listas de texto, a ordem crescente é a ordem alfabética.

Regras:

- Utilize o método `sort` (que ordena a lista) ou a função `sorted`;
- Lembre-se de que `sort` altera a lista no lugar e retorna `None` - a função deve retornar a lista ordenada, não o resultado de `sort`.

Exemplos:

- `resposta([3, 1, 2])` → `[1, 2, 3]`
- `resposta(['banana', 'abacaxi', 'manga'])` → `['abacaxi', 'banana', 'manga']`

**Atenção:** utilize `return`, não `print`.
