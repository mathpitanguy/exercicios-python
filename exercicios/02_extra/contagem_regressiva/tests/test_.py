from contagem_regressiva.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13)) == list, "Esperado uma lista"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta(10) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1], f"Esperado valor '[10, 9, 8, 7, 6, 5, 4, 3, 2, 1]'"
    assert resposta(1) == [1], f"Esperado valor '[1]'"
    assert resposta(0) == [], f"Esperado valor '[0]'"
