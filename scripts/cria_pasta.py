import argparse
from pathlib import Path

parser = argparse.ArgumentParser()


parser.add_argument("caminho_pasta")
args = parser.parse_args()
# print(args.nome_arquivo, args.caminho_pasta)

conteudo_teste = """from metro_milimetro.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13)) == int or type(resposta(3.2)) == float, "Esperado um inteiro ou float"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(10) == 10000, f"Esperado valor 10000"
    assert resposta(1.2) == 1200, f"Esperado valor 1200"
    assert resposta(0.93) == 930, f"Esperado valor 930"
"""

conteudo_readme = """**Tags:** <lista de temas relacionados>  
**Nível:** <Iniciante | Intermediário | Avançado>

## Objetivo

<Explicação simples do que o exercício treina e por que ele é importante>

## Especificação

### <Título da tarefa>

Abra o arquivo `main.py`. Dentro dele, localize a função `resposta`.

<Explique claramente o que a função deve receber e o que deve retornar>

Regras:

- <Regra 1>
- <Regra 2>
- <Regra 3>

Exemplos:

- <exemplo 1>  
- <exemplo 2>

**Atenção:** utilize `return`, não `print`.

"""

caminho_pasta = Path(args.caminho_pasta)
if not caminho_pasta.parent.is_dir(): 
    print(f'{caminho_pasta.parent} não é um caminho válido.')
else:
    caminho_pasta.mkdir()
    (caminho_pasta / '_README.md').touch()
    (caminho_pasta / '_README.md').write_text(conteudo_readme, encoding="utf-8")
    (caminho_pasta / 'main.py').touch()
    (caminho_pasta / 'main.py').write_text(
    'def resposta():\n' 
    '    pass')
    (caminho_pasta / '__init__.py').touch()
    pasta_testes = caminho_pasta / 'tests'
    pasta_testes.mkdir()
    (pasta_testes/ '__init__.py').touch()
    (pasta_testes/ 'test_.py').touch()
    (pasta_testes/ 'test_.py').write_text(conteudo_teste, encoding="utf-8")