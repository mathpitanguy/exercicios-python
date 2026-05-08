---
Tags: Variáveis, Strings, Estruturas Condicionais (if), Operadores de Comparação, Laços de Repetição (while)
Nível: Iniciante
---

## Objetivo

Praticar validação de dados utilizando estruturas condicionais e laços de repetição. Neste exercício, você irá garantir que uma senha seja diferente do nome de usuário, reforçando regras básicas de validação.

## Especificação

### Validação de Usuário e Senha

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

A função deverá receber dois valores do tipo string:

- Nome de usuário
- Senha

E deverá retornar uma string indicando:

- `"válido"` caso a senha seja diferente do nome de usuário
- `"erro"` caso a senha seja igual ao nome de usuário

Regras:

- Comparar o nome de usuário com a senha
- Se forem iguais, retornar `"erro"`
- Se forem diferentes, retornar `"válido"`

Exemplos:

- `resposta("joao", "1234")` → `"válido"`
- `resposta("maria", "maria")` → `"erro"`

**Atenção:** utilize `return`, não `print`.
