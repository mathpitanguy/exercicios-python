---
Tags: Strings, Condicionais, Aleatoriedade
Nível: Iniciante
---

## Objetivo

Neste desafio, você vai praticar manipulação de strings e implementar a **Cifra de César**, um dos métodos de criptografia mais antigos que existem, para decodificar uma mensagem secreta.

## Contexto

A Cifra de César funciona deslocando cada letra do alfabeto um número fixo de posições. Por exemplo, com uma chave `3`, a letra `A` vira `D`, `B` vira `E`, e assim por diante. Para decodificar, o processo é inverso: desloca-se as letras para trás, na mesma quantidade.

Você receberá, no comentário desta Issue, uma **mensagem codificada** e uma **chave** (um número inteiro). Sua tarefa é escrever o código que reverte a cifra e recupera a mensagem original.

## Especificação

### Decodifique a mensagem

Abra o arquivo `main.py`. Dentro dele, localize a função `decodificar`.

A função deve receber:
- uma string `mensagem` com o texto codificado (sempre em caixa alta, sem acentos)
- um número inteiro `chave`

Sua tarefa é retornar a mensagem decodificada como string, seguindo os passos abaixo:

Passo 1 — Percorra a mensagem*
- Use um loop `for` para percorrer cada caractere de `mensagem`

Passo 2 — Trate letras e outros caracteres separadamente
- Se o caractere for uma letra (`.isalpha()`), aplique a fórmula de decodificação da Cifra de César:

- Se não for uma letra (espaço, vírgula, `!`), mantenha o caractere como está, sem nenhuma alteração

Passo 3 — Monte e retorne o resultado

- Vá concatenando cada caractere processado em uma nova string
- Retorne essa string ao final da função

Atenção: utilize `return`,

### Por que usamos `% 26`?

O alfabeto tem 26 letras (A a Z), e cada letra pode ser representada por um número de `0` a `25` (a posição dela no alfabeto, começando do zero). Fazemos isso com `ord(char) - ord('A')`: como `ord('A')` é o próprio início do alfabeto, subtrair ele "zera" a régua e nos diz a posição da letra dentro do intervalo 0-25.

Ao decodificar, subtraímos a `chave` dessa posição — e é aqui que mora o problema: **esse resultado pode ficar negativo**. Por exemplo:

```python
letra = 'B'   # posição 1
chave = 5
posicao = 1 - 5   # -4 -> não existe posição -4 no alfabeto!
```

Se você tentasse converter `-4` diretamente de volta para letra com `chr()`, o resultado seria um caractere fora do alfabeto, sem nenhum sentido — não existe "a 4ª letra antes do A".

É aqui que entra o `% 26` (operador módulo, o resto da divisão): em Python, o operador `%` sempre retorna um resultado **não negativo** quando o divisor é positivo, mesmo que o número original seja negativo. Ele faz o valor "dar a volta" pelo final do alfabeto, como um relógio que, ao passar de 0h, volta para 23h em vez de virar "-1h":

```python
-4 % 26   # resultado: 22 -> posição 22 é a letra 'W'
```

Ou seja, `B` deslocado 5 posições para trás vira `W`, porque ao "passar" do `A`, o alfabeto recomeça do `Z` e conta pra trás a partir dali. Sem o `% 26`, o programa geraria um erro ou um caractere inválido ao tentar usar `chr()` com um número negativo.


Se todos os testes passarem, você verá a mensagem decodificada no terminal. Copie e cole no comentário do Issue!
