from metro_milimetro.main import resposta
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
