import inspect

from desafio_final.main import resposta


def test_parametros_sao_mensagem_e_chave():
    args = inspect.getfullargspec(resposta).args
    assert len(args) == 2, "A função deve receber dois parâmetros: mensagem e chave"


def test_retorno_e_string():
    resultado = resposta("EBWDJFHI", 4)
    assert isinstance(resultado, str), "A função deve retornar uma string"


def test_decodificacao_com_modulo_negativo():
    # 'A' com chave 1 precisa "dar a volta" pelo fim do alfabeto e virar 'Z'
    resultado = resposta("A", 1)
    assert resultado == "Z", \
        "Quando o resultado do deslocamento é negativo, o alfabeto deve dar a volta (uso do % 26)"

def test_decodificacao_com_pontuacao_e_modulo_26():
    assert resposta("IFU, NOXI VYG?", 20) == "OLA, TUDO BEM?", \
        f"Esperado valor 'OLA, TUDO BEM?'"