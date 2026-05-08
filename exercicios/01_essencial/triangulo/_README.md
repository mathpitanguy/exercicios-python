---
Tags: Estruturas Condicionais (if), Operadores Lógicos, Operadores de Comparação
Nível: Iniciante
---

## Objetivo

Praticar o uso de estruturas condicionais para validar regras matemáticas e classificar dados. Neste exercício, você irá verificar se três valores podem formar um triângulo e, caso possam, identificar seu tipo.

## Especificação

### Validação e Classificação de Triângulo

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber três valores numéricos (representando os lados de um triângulo) e retornar uma string informando:

- Se os valores **não formam um triângulo**
- Ou, caso formem, qual é o tipo:
  - `"equilátero"` (todos os lados iguais)
  - `"isósceles"` (dois lados iguais)
  - `"escaleno"` (todos os lados diferentes)

Regras:

- Para formar um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro lado
- Se não atender essa condição, retornar `"não forma triângulo"`
- Se formar:
  - Três lados iguais → `"equilátero"`
  - Dois lados iguais → `"isósceles"`
  - Todos diferentes → `"escaleno"`

Exemplos:

- `resposta(3, 3, 3)` → `"equilátero"`
- `resposta(3, 4, 5)` → `"escaleno"`
- `resposta(2, 2, 3)` → `"isósceles"`
- `resposta(1, 2, 3)` → `"não forma triângulo"`

**Atenção:** utilize `return`, não `print`.
