def resposta(mensagem, chave):
    resultado = ""

    for char in mensagem:
        if char.isalpha():
            posicao = (ord(char) - ord('A') - chave) % 26
            nova_letra = chr(posicao + ord('A'))
            resultado += nova_letra
        else:
            resultado += char

    return resposta('ZKBKLOXC, WKDROEC! FYMO MYXMVESE Y MEBCY DBSVRK NOF ZIDRYX', 10)
