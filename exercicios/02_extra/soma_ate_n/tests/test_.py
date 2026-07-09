from soma_ate_n.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(10)) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(5) == 15, f"Esperado valor 15"
    assert resposta(5.2) == 15, f"Esperado valor 15"
    assert resposta(0) == 0, f"Esperado valor 0"
    assert resposta(1) == 1, f"Esperado valor 1"
