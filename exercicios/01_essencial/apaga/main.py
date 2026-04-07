def resposta (palavra, index):
    palavra = str(palavra)
    index = int(index)

    if index > len(palavra):
        return palavra
    else:
        novapalavra = palavra[:index] + palavra[index+1:]
        return novapalavra
