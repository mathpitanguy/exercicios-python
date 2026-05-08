from fibonacci.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13)) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(1) == 1, f"Esperado valor 1"
    assert resposta(10) == 55, f"Esperado valor 55"
    assert resposta(3) == 2, f"Esperado valor 2"
