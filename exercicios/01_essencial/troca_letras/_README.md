**Tags:** Strings, Manipulação de Strings, Condicionais  
**Nível:** Iniciante

## Objetivo

Neste exercício, vamos praticar a manipulação de strings e o acesso a posições específicas de uma palavra. Você irá aprender a construir uma nova string a partir de partes da original.

## Especificação

### Troque a primeira e a última letra

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

Essa função deverá receber uma `String` chamada `s`.

Sua tarefa é retornar uma nova string em que a primeira e a última letras foram trocadas de posição.

Regras:

- Se a string tiver tamanho menor ou igual a 1, retorne a própria string sem alterações.
- Caso contrário, troque a primeira e a última letra da string.

Exemplos:

- `troca('code')` → `'eodc'`  
- `troca('a')` → `'a'`  
- `troca('ab')` → `'ba'`

**Atenção:** utilize `return`, não `print`.