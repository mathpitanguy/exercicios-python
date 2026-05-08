from crescimento_populacao.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta() is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta()) == int, "Esperado um inteiro"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 0, "Assinatura da função não deverá receber parâmetro"


def test_options_resposta():
    assert resposta() == 63, f"Esperado valor 63"
