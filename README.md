# Trilha-Dev: Python - Repositório de exercícios Python com testes automatizados

## Setup

Certifique-se de ter instalado:

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/)

### Configuração Inicial

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:

   ```sh
   git clone git@github.com:splor-mg/exercicios-python.git
   cd exercicios-python
   ```

2. Instale as dependências do projeto com Poetry:

   ```sh
   poetry install
   ```

## Comandos importantes

- Executar todos os testes do diretório. 
    ```sh
    task test 
    ```

- Criar nova pasta de exercício.
    ```sh
    task new-exec [nome_pasta]
    ```
## Orientações para realizar os alunos Trilha - Dev: Python

Para fazer os exercícios, você precisará copiar o repositório da organização Splor-mg no GitHub para sua conta pessoal. Isso pode ser feito com um `fork` e abaixo está o passo a passo de como isso deve ser feito.

Este guia mostra como criar uma cópia de um repositório de uma organização para sua conta pessoal usando a funcionalidade de Fork do GitHub.

###  Criar o Fork

1. Acesse o repositório exercicios-python da Splor-mg
2. Clique no botão Fork (canto superior direito).
3. Escolha sua conta pessoal como destino.
4. Confirme a criação.

O GitHub criará automaticamente uma cópia do repositório na sua conta.

### Verificar o repositório na sua conta

- Agora você terá algo como:

    ```sh
    https://github.com/SEU-USUARIO/exercicios-python
    ```

- Na parte superior da página aparecerá a indicação:

    ```sh
    forked from splor-mg/exercicios-python
    ```

### (Opcional) Clonar o seu fork para sua máquina

1. No terminal:

    ```sh
    git clone git@github.com:SEU-USUARIO/exercicios-python.git
    ```

2. Entre na pasta:

    ```sh
    cd exercicios-python
    ```

### (Opcional) Configurar o repositório original como upstream

Isso permite atualizar seu fork com mudanças feitas pela organização.

1. Adicione o repositório original como upstream:

    ```sh
    git remote add upstream git@github.com:splor-mg/exercicios-python.git
    ```

2. Verifique os remotes:

    ```sh
    git remote -v
    ```

- Saída esperada:

    ```sh
    origin    git@github.com:SEU-USUARIO/exercicios-python.git (fetch)
    origin    git@github.com:SEU-USUARIO/exercicios-python.git (push)
    upstream  git@github.com:splor-mg/exercicios-python.git (fetch)
    upstream  git@github.com:splor-mg/exercicios-python.git (push)
    ```

### (Opcional) Atualizar seu fork no futuro

- Para trazer atualizações do repositório original:

    ```sh
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```


Siga com o setup do projeto e, depois, é mão na massa!