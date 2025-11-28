from _hello_world.main import resposta
import inspect
import pytest

def test_not_none():
    assert resposta() is not None, "Esperado valor diferente de 'None'"

def test_type():
    assert type(resposta()) == str and len(resposta()) == 9, "Esperado string com 9 caracteres"

def test_parameters():
    assert len(inspect.getfullargspec(resposta).args) == 0, "Assinatura da função não poderá receber nenhum parâmetro"

def test_options_resposta():
    possible_anwsers = [
                        "Olá Mundo",
                        "Olá mundo",
                        "Ola Mundo",
                        "olá mundo",
                        "ola mundo",
                        "OLÁ MUNDO",
                        "OLA MUNDO",
                        ]
    assert resposta() in possible_anwsers , f"Esperado {possible_anwsers}"