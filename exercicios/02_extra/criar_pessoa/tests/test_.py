from criar_pessoa.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta('Ana', 30, 'Belo Horizonte') is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta('Ana', 30, 'Belo Horizonte')) == dict, "Esperado um dicionário"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 3, "Assinatura da função deverá receber três parâmetros"


def test_options_resposta():
    assert resposta('Ana', 30, 'Belo Horizonte') == {'nome': 'Ana', 'idade': 30, 'cidade': 'Belo Horizonte'}, f"Esperado valor {'nome': 'Ana', 'idade': 30, 'cidade': 'Belo Horizonte'}"
    assert resposta('João', 25, 'Poços de Caldas') == {'nome': 'João', 'idade': 25, 'cidade': 'Poços de Caldas'}, f"Esperado valor {'nome': 'João', 'idade': 25, 'cidade': 'Poços de Caldas'}"
