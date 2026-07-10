from buscar_com_get.main import resposta
import inspect
import pytest



def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 2, "Assinatura da função deverá receber dois parâmetros"


def test_options_resposta():
    assert resposta({'nome': 'Ana'}, 'nome') == 'Ana', f"Esperado valor 'Ana'"
    assert resposta({'nome': 'Ana'}, 'idade') == None, f"Esperado valor None"
