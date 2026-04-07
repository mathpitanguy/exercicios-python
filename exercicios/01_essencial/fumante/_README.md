**Tags:** Operações Aritméticas, Funções, Parâmetros  
**Nível:** Iniciante

## Objetivo

Este exercício trabalha a transformação de unidades e a aplicação de cálculos acumulativos ao longo do tempo.

## Especificação

### Calcule a perda de dias de vida de um fumante

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

Originalmente, este programa pediria dados ao usuário usando `input()`. Aqui, você deve implementar a lógica utilizando parâmetros.

A função deverá receber:

- um inteiro representando a **quantidade de cigarros fumados por dia**
- um inteiro representando a **quantidade de anos que a pessoa fumou**

Sua tarefa é **retornar um inteiro correspondente ao total de dias de vida perdidos**.

Regras:

- Considere que:
  - Cada cigarro reduz **10 minutos de vida**
  - 1 dia possui **1440 minutos**
- Calcule o total de minutos perdidos e converta para dias

Exemplos:

- `resposta(10, 1)` → `25` (valor aproximado)  

**Atenção:** utilize `return`, não `print`.

