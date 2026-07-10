---
Tags: Strings, Métodos de String, Laços de Repetição (for), Estruturas Condicionais (if), Funções
Nível: Iniciante
---
# DESAFIO FINAL

## Objetivo
 
Praticar manipulação de strings implementando a **Cifra de César** para decodificar uma mensagem secreta.
 
## Contexto
 
A Cifra de César desloca cada letra do alfabeto um número fixo de posições. Com chave `3`, `A` vira `D`, `B` vira `E`, e assim por diante. Para decodificar, o processo é inverso: desloca-se as letras para trás, na mesma quantidade.
 
Você recebeu, no comentário do Issue, uma **mensagem codificada** e uma **chave** (um número inteiro). Sua tarefa é escrever o código que reverte a cifra e recupera a mensagem original.
 
## Especificação
 
Abra o arquivo `desafio_final/main.py` e localize a função `resposta`.
 
A função espera receber dois parâmetros: `mensagem`, uma string com o texto codificado (sempre em caixa alta, sem acentos), e `chave`, um número inteiro com a quantidade de posições do deslocamento.
 
Passos:
 
1. Percorra a  `mensagem`.
2. Se o caractere for uma letra (`.isalpha()`), aplique a fórmula de decodificação da Cifra de César; se não for (espaço, vírgula, `!`), mantenha como está.
3. Concatene o resultado numa nova string e retorne-a com `return resultado` ao final.

### Dica: 
 
O alfabeto tem 26 letras (posições `0` a `25`, via `ord(char) - ord('A')`). Ao subtrair a `chave`, o resultado pode ficar negativo (ex.: posição `1 - 5 = -4`, que não existe). O operador `% 26` resolve isso fazendo o valor "dar a volta" pelo fim do alfabeto — em Python, `%` sempre devolve um resultado não negativo quando o divisor é positivo (`-4 % 26` = `22`, ou seja, a letra `W`). Sem o `% 26`, `chr()` geraria um caractere inválido.
 
### Hora de decifrar sua mensagem secreta:
 
Se os testes passaram, seu decodificador está pronto, chegou a hora de usá-lo na missão de verdade: a mensagem que você recebeu na Issue.
 
No final do `main.py`, fora da função, chame a `resposta` com os valores reais:
 
```python
mensagem_decodificada = resposta(mensagem, chave)
print(mensagem_decodificada)
```
 
Rode o arquivo, tire um print do terminal mostrando a frase decodificada e cole esse print como comentário na Issue do desafio.