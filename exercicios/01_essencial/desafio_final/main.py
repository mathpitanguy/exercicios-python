def resposta(mensagem, chave):
    
    resultado = ""
    for char in mensagem:
        if char.isalpha():
            posicao = (ord(char) - ord('A') - chave) % 26
            nova_letra = chr(posicao + ord('A'))
            resultado += nova_letra
        else:
            resultado += char
    return posicao


mensagem_decodificada = resposta('KVMVWZIN, HVOCZPN! QJXZ XJIXGPDP J XPMNJ OMDGCV YZQ KTOCJI.',21 )
print (mensagem_decodificada)