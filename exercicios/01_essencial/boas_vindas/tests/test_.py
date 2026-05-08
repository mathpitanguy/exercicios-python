from boas_vindas.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta("Ana") is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta("Ana")) ==str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta("João") == "Bem-vindo, João!", f'Esperado valor "Bem-vindo, João!"'
    assert resposta('Maria') == 'Bem-vindo, Maria!', f'Esperado valor "Bem-vindo, Maria!"'
