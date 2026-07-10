# Trilha-Dev: Python - Repositório de exercícios Python com testes automatizados

![test status](../coverage-badge/tests.svg?raw=true) ![desafio final](../badge-desafio-final/desafio-final.svg?v=1&raw=true&debug=1)

Repositório de exercícios Python com correções automáticas. Aqui, as soluções propostas para os exercícios recebem feedback instantâneo e automático via testes automatizados.

## Começe agora

Para fazer os exercícios, você precisará copiar o repositório da organização Splor-mg no GitHub para sua conta pessoal. Isso pode ser feito com um `fork` e abaixo está o passo a passo de como isso deve ser feito.

###  Criar o Fork

1. Acesse o [repositório exercicios-python da Splor-mg](https://github.com/splor-mg/exercicios-python/).
2. Clique no botão [Fork](https://github.com/splor-mg/exercicios-python/fork) (canto superior direito).
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

## Setup Local

Certifique-se de ter instalado:

- [Python](https://www.python.org/) 3.8+
- [Poetry](https://python-poetry.org/)

Siga os passos abaixo para configurar o projeto localmente:

1. Clone o repositório:

   ````sh
   git clone git@github.com:SEU-USUARIO/exercicios-python.git
   cd exercicios-python
   ```

2. Ative o ambiente virtual

    ```sh
    eval $(poetry env activate)
    ```

3. Instale as dependências do projeto com Poetry:

   ```sh
   poetry install
   ```

## Setup com Codespaces

1. No seu novo repositório (https://github.com/SEU-USUARIO/exercicios-python) clique no botão "Code" (canto superior direito).
2. Você verá as opções "Local" e "Codespaces" na caixa que será aberta. Clique em "Codespaces".
3. Clique em "Create codespace on main".
4. Aguarde a configuração do novo ambiente que será montado para você (pode demorar alguns minutos).
5. Confira a instalação do Python digitando o comando `python --version` no terminal. Você deverá ver algo parecido com `Python 3.12.1` como resposta. Caso contrário, a instalação ainda não finalizou e você deverá aguardar mais um momento.
6. Confira a instalação do Poetry digitando o comando `poetry --version` no ternimal. Você deverá ver algo parecido com `Poetry (version 2.3.4)` como resposta. Caso contrário, seu codespaces não foi capaz de instalá-lo sozinho. Execute o comando `pipx install poetry` e depois `poetry --version` para conferir novamente. Você deverá ver algo parecido com `Poetry (version 2.3.4)`[^1].
7. Confira a configuração do remote `upstream` digitando o comando `git remote -v`. Você deverá ver listado dois registros para os remotes `origin` e `upstream` respectivamente. Caso contrário, a instalação ainda não finalizou e você deverá aguardar mais um momento.
8. Instale as dependências do projeto digitando o comando `poetry install`.

[^1]: A versão instalada do poetry não pode ser inferior à `2`, sendo assim respostas como `Poetry (version 1.8.5)` estão erradas e não funcionarão. Digite o comando `pipx upgrade poetry` para atualizar e utilizar a versão do Poetry mais atualizada possível.


## Correção automatizada dos exercícios

- Lembre-se ativar o ambiente virtual antes de rodar os comandos.

- Navegue até a pasta do exercício a ser corrigido:

    ```sh
    cd <pasta-exercicio>
    ```

- Executar todos os testes do diretório.
    ```sh
    task test
    ```

### Configurar o repositório original como upstream

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

### Atualizar seu fork no futuro

- Para trazer atualizações do repositório original:

    ```sh
    git fetch upstream
    git checkout main
    git merge upstream/main
    ```


Siga com o setup do projeto e, depois, é mão na massa!
