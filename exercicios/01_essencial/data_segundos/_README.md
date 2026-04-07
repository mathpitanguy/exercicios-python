**Tags:** Operações Aritméticas, Funções, Parâmetros  
**Nível:** Iniciante

## Objetivo

Neste exercício, você irá praticar operações matemáticas básicas e o uso de funções para transformar diferentes unidades de tempo em um único valor.

## Especificação

### Converta uma data para segundos

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

Essa função deverá receber:

- um `int` representando **dias**
- um `int` representando **horas**
- um `int` representando **minutos**
- um `int` representando **segundos**

Sua tarefa é **retornar o total de segundos correspondente à soma desses valores**.

Regras:

- Considere que:
  - 1 dia = 24 horas  
  - 1 hora = 60 minutos  
  - 1 minuto = 60 segundos  

Exemplos:

- `resposta(0, 0, 1, 0)` → `60`  
- `resposta(0, 1, 0, 0)` → `3600`  
- `resposta(1, 0, 0, 0)` → `86400`  

**Atenção:** utilize `return`, não `print`.