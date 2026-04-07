**Tags:** Strings, Manipulação de Strings  
**Nível:** Iniciante

## Objetivo

Neste exercício, você irá praticar a manipulação de strings removendo caracteres com base em uma posição específica.

## Especificação

### Remova um caractere da string

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deve receber:

- uma string `palavra`
- um inteiro `index`

Sua tarefa é retornar uma nova string sem o caractere da posição `index`.

Regras:

- Se o índice for válido, remova o caractere correspondente  
- Se o índice for maior ou igual ao tamanho da string, retorne a string original  

Exemplos:

- `resposta('batatinha', 1)` → `'btinha'`  
- `resposta('batatinha', 4)` → `'batainha'`

**Atenção:** utilize `return`, não `print`.
