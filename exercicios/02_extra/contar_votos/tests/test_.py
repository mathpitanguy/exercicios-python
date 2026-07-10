from contar_votos.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta([10, 20]) is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta([10, 20])) == dict, "Esperado um dicionário"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    assert resposta([10, 20]) == {'10': 1, '20': 1}, f"Esperado valor {{'10': 1, '20': 1}}"
    assert resposta([]) == {}, f"Esperado valor '{{}}'"
    assert resposta(['A', 'B', 'A', 'C', 'A']) == {'A': 3, 'B': 1, 'C': 1}, f"Esperado valor {{'A': 3, 'B': 1, 'C': 1}}"
