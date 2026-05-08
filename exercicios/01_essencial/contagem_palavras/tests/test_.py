from contagem_palavras.main import resposta
import inspect
import pytest


def test_not_none():
    assert resposta("Teste teste teste") is not None, "Esperado valor diferente de 'None'"


def test_type():
    assert type(resposta("Teste teste teste")) == dict, "Esperado um dicionário"


def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 1, "Assinatura da função deverá receber um parâmetro"


def test_options_resposta():
    esperado1 = {'hoje': 2, 'foi': 2, 'um': 1, 'dia': 1, 'bom': 1, 'especial': 1}
    esperado2 = {'não': 1, 'pare': 1, 'de': 1, 'acreditar': 1}

    assert resposta("hoje foi um dia bom hoje foi especial") == esperado1, f"Esperado valor {esperado1}"
    assert resposta("não pare de acreditar") == esperado2, f"Esperado valor {esperado2}"
