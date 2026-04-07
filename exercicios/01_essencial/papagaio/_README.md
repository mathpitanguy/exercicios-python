**Tags:** Condicionais, Operadores Lógicos  
**Nível:** Iniciante

## Objetivo

Este exercício trabalha a combinação de condições para tomar decisões com base em múltiplos fatores.

## Especificação

### Verifique se há problema com o papagaio

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deve receber:

- `falando` (booleano)
- `hora` (inteiro entre 0 e 23)

Sua tarefa é retornar `True` se houver problema.

Regras:

- Há problema se o papagaio estiver falando  
- E o horário for antes das 7 (`hora < 7`)  
- Ou depois das 20 (`hora > 20`)  

Caso contrário, retorne `False`.

Exemplos:

- `resposta(True, 6)` → `True`  
- `resposta(True, 21)` → `True`  
- `resposta(True, 10)` → `False`  
- `resposta(False, 6)` → `False`

**Atenção:** utilize `return`, não `print`.