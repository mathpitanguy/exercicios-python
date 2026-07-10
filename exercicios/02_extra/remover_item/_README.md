---
Tags: Métodos de Lista, Listas, Estruturas Condicionais (if), Operadores de Comparação
Nível: Iniciante
---

## Objetivo

Praticar a remoção de itens com o método `remove` e a verificação de existência com o operador `in`. Checar se um item existe antes de removê-lo evita erros em tempo de execução.

## Especificação

### Remover a primeira ocorrência de um item

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função recebe os parâmetros `lista` (uma lista) e `item` (o valor a ser removido). Remova a **primeira ocorrência** desse item e retorne a lista resultante. Se o item não estiver na lista, retorne a lista sem nenhuma alteração.

Regras:

- Antes de remover, verifique se o item existe na lista usando o operador `in`;
- Utilize o método `remove`;
- Remova apenas a primeira ocorrência, mesmo que o item apareça mais de uma vez.

Exemplos:

- `resposta(['a', 'b', 'a'], 'a')` → `['b', 'a']`
- `resposta(['x', 'y'], 'z')` → `['x', 'y']`

**Atenção:** utilize `return`, não `print`.
