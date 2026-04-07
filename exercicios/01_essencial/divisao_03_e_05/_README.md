**Tags:** Condicionais, Operadores de Comparação, Operadores Lógicos  
**Nível:** Iniciante

## Objetivo

O desafio FizzBuzz é um exercício clássico utilizado para treinar lógica condicional. Ele ajuda a desenvolver o raciocínio necessário para trabalhar com múltiplas regras ao mesmo tempo.

## Especificação

### Implemente o FizzBuzz

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deve receber um inteiro positivo `n` e retornar:

Regras:

- `'Fizz'` se `n` for divisível por 3  
- `'Buzz'` se `n` for divisível por 5  
- `'FizzBuzz'` se `n` for divisível por 3 e por 5  
- O próprio número `n` nos demais casos

Exemplos:

- `resposta(3)` → `'Fizz'`  
- `resposta(5)` → `'Buzz'`  
- `resposta(15)` → `'FizzBuzz'`  
- `resposta(7)` → `7`

**Atenção:** utilize `return`, não `print`.