from divisao_segura.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta(10, 2) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta(13, 13)) == int or type(resposta(3, 2)) == float or type(resposta(12, 0) == str), "Esperado um inteiro, float ou string"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta(10, 2) == 5, f"Esperado valor 5"
    assert resposta(1, 2) == 0.5 , f"Esperado valor 0.5"
    assert resposta(9, 0) == 'Valores inválidos', f"Esperado valor 'Valores inválidos'"
