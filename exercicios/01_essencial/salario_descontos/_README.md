---
Tags: Variáveis, Operações Aritméticas, Estruturas Condicionais (if), Tuplas
Nível: Iniciante
---

## Objetivo

Praticar cálculos matemáticos com porcentagens e organização de resultados. Neste exercício, você irá simular o cálculo de um salário com descontos obrigatórios, entendendo como aplicar taxas sobre valores.

## Especificação

### Cálculo de Salário com Descontos

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber dois valores numéricos:

- O valor ganho por hora
- A quantidade de horas trabalhadas no mês

E deverá retornar uma tupla com os seguintes valores:

1. Salário bruto
2. Valor descontado do Imposto de Renda (11%)
3. Valor descontado do INSS (8%)
4. Valor descontado do sindicato (5%)
5. Salário líquido

Regras:

- Salário bruto = valor por hora × horas trabalhadas
- Calcular os descontos:
  - IR: 11% do salário bruto
  - INSS: 8% do salário bruto
  - Sindicato: 5% do salário bruto
- Salário líquido = salário bruto - soma dos descontos
- Todos os valores devem ser retornados na ordem especificada

Exemplos:

- `resposta(10, 160)` → `(1600, 176, 128, 80, 1216)`
- `resposta(20, 100)` → `(2000, 220, 160, 100, 1520)`

**Atenção:** utilize `return`, não `print`.
