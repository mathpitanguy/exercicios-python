from desafio_final.main import resposta
import inspect


def test_parametros_sao_mensagem_e_chave():
    args = inspect.getfullargspec(resposta).args
    assert len(args) == 2, "A função deve receber dois parâmetros: mensagem e chave"


def test_retorno_e_string():
    resultado = resposta("EBWDJFHI", 4)
    assert isinstance(resultado, str), "A função deve retornar uma string"


from desafio_final.main import resposta
import inspect


def test_parametros_sao_mensagem_e_chave():
    args = inspect.getfullargspec(resposta).args
    assert len(args) == 2, "A função deve receber dois parâmetros: mensagem e chave"


def test_retorno_e_string():
    resultado = resposta("EBWDJFHI", 4)
    assert isinstance(resultado, str), "A função deve retornar uma string"


def test_decodificacao_com_pontuacao_e_modulo_26():
    # "IFU, NOXI VYG?" com chave 20 deve virar "OLA, TUDO BEM?"
    mensagem = "IFU, NOXI VYG?"
    chave = 20

    resultado = resposta(mensagem, chave)

    print("\nMensagem enviada:", mensagem)
    print("Chave utilizada:", chave)
    print("Resultado:", resultado)

    assert resultado == "OLA, TUDO BEM?", \
        "Esperado 'OLA, TUDO BEM?' ao decodificar a mensagem com chave 20"
