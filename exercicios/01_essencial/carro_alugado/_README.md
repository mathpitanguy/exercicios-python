**Tags:** Operações Aritméticas, Funções, Parâmetros  
**Nível:** Iniciante

## Objetivo

Neste exercício, você irá aplicar operações matemáticas para resolver um problema do mundo real, calculando o custo de um serviço com base em múltiplos fatores.

## Especificação

### Calcule o valor do aluguel de um carro

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

Originalmente, este programa pediria dados ao usuário usando `input()`. Aqui, você deve implementar a lógica utilizando parâmetros.

A função deverá receber:

- um número representando a **quantidade de quilômetros percorridos**
- um número representando a **quantidade de dias de aluguel**

Sua tarefa é **retornar o preço total a pagar**.

Regras:

- O custo é composto por:
  - R$ 60,00 por dia  
  - R$ 0,15 por quilômetro rodado  

Exemplos:

- `resposta(100, 2)` → `135.0`  
- `resposta(0, 1)` → `60.0`  

**Atenção:** utilize `return`, não `print`.