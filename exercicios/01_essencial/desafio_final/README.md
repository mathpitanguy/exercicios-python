---
Tags: Strings, Listas, Funções, Condicionais, Módulos
Nível: Iniciante
---

## Objetivo

Neste desafio, você vai praticar manipulação de listas, strings, condicionais e uso de módulos criando o seu **card de conclusão** do curso.

## Especificação

### Gere o seu card de conclusão

Abra o arquivo `main.py`. Dentro dele, localize a função `gerar_card`.

A função deve receber:
- uma lista `emails` com e-mails de participantes
- uma string `email` com o seu e-mail
- uma string `frase` com uma frase sua sobre o curso

Sua tarefa é retornar o card formatado como string seguindo os passos abaixo:

**Passo 1 — Adicione seu e-mail à lista**
- Use `.append()` para adicionar o parâmetro `email` ao final da lista `emails`

**Passo 2 — Trate os e-mails da lista**
- Percorra a lista com um loop `for`
- Para cada e-mail, corte o texto antes do `@`
- Substitua o `.` por espaço com `.replace()`
- Coloque em caixa alta com `.upper()`
- Armazene os resultados em uma nova lista chamada `nomes_tratados`

**Passo 3 — Pegue o seu nome pelo índice**
- Seu e-mail foi o último adicionado, então seu nome é o último da lista
- Armazene em uma variável chamada `nome`

**Passo 4 — Verifique o status**
- Se `nome` estiver na lista `concluintes` → `status = "Curso TrilhaDev Concluído"`
- Caso contrário → `status = "Curso TrilhaDev em Andamento"`

**Passo 5 — Capture a data de hoje**
- Use `datetime.now()` para obter a data atual
- Formate como `"DD/MM/AAAA"` com `.strftime()`
- Armazene em uma variável chamada `data`

**Passo 6 — Monte e retorne o card**

O card deve seguir exatamente este formato:

```
NOME: JOAO SILVA
STATUS: Curso TrilhaDev Concluído
FRASE: Python mudou a forma como eu trabalho!
DATA DE CONCLUSÃO: 18/06/2026
```

Exemplos:
- `gerar_card(emails, "joao.silva@prefeitura.gov.br", "Python é incrível!")` → card com `NOME: JOAO SILVA` e `STATUS: Curso TrilhaDev Concluído`
- `gerar_card(emails, "carlos.lima@gmail.com", "Ainda aprendendo!")` → card com `NOME: CARLOS LIMA` e `STATUS: Curso TrilhaDev em Andamento`

**Atenção:** utilize `return`, não `print`.

## Como testar

Execute no terminal:

```bash
pytest tests/ -v -s
```

Se todos os testes passarem, o seu card será exibido no terminal. Copie e cole nos comentários do curso! 🏆
