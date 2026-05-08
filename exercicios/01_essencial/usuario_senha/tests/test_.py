from usuario_senha.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta("a", "a") is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta("a", "a")) == str, "Esperado uma string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta("joao", "1234") == "válido", f"Esperado valor 'valido'"
    assert resposta("maria", "maria") == "erro", f"Esperado valor 'erro'"
