def resposta(preço, desconto):
    preço = int (preço)
    desconto = preço * (desconto / 100)
    precofinal = preço - desconto

    return (desconto,precofinal)
