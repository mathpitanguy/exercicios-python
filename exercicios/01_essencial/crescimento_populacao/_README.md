---
Tags: Variáveis, Operações Aritméticas, Estruturas Condicionais (if), Operadores de Comparação, Laços de Repetição (while), Funções, Parâmetros, Instrução return
Nível: Intermediário
---

## Objetivo

Praticar o uso de laços de repetição para simular crescimento ao longo do tempo. Neste exercício, você irá calcular quantos anos são necessários para que uma população ultrapasse outra, aplicando taxas de crescimento anuais.

## Especificação

### Crescimento Populacional

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá calcular e retornar um número inteiro representando a quantidade de anos necessários para que a população do país A ultrapasse ou iguale a população do país B.

Considere os seguintes valores fixos:

- População inicial do país A: 80000 habitantes
- Taxa de crescimento anual de A: 3%
- População inicial do país B: 200000 habitantes
- Taxa de crescimento anual de B: 1.5%

Regras:

- A cada ano, atualizar ambas as populações com base em suas taxas de crescimento
- Continuar o cálculo até que a população de A seja maior ou igual à de B
- Contar e retornar o número de anos necessários

**Atenção:** utilize `return`, não `print`.
