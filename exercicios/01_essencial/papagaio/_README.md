## Objetivo

Neste exercício, vamos treinar lógica condicional avaliando duas informações ao mesmo tempo: um comportamento (o papagaio estar falando ou não) e um horário específico do dia. O objetivo é determinar quando isso representa um problema.

## Especificação
### Verifique se há problema com o papagaio

Abra o arquivo `main.py`. Nele, você encontrará a função `resposta`.
Essa função deverá receber dois parâmetros:

- falando — um valor booleano (True ou False) indicando se o papagaio está falando.
- hora — um inteiro entre 0 e 23, representando o horário do dia.

Sua tarefa é retornar True se estivermos com problemas, seguindo as regras abaixo:

Há problema se o papagaio estiver falando:

- E o horário for antes das 7
- Ou depois das 20

Nos demais casos, retorne `False`.

Use sempre return, não print.