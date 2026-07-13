def resposta(mensagem, chave):

    resultado = ""
    for char in mensagem:
        if char.isalpha():
            posicao = (ord(char) - ord('A') - chave) % 26
            nova_letra = chr(posicao + ord('A'))
            resultado += nova_letra
        else:
            resultado += char
    return resultado


mensagem_decodificada = resposta('RCTCDGPU, OCVJGWU! XQEG GUVC XQCPFQ DCKZQ.',2 )
print (mensagem_decodificada)
