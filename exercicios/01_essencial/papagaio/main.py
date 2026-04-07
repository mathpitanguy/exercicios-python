def resposta(falando, hora):
    falando = bool()
    hora = int(hora)

    if hora < 7 or hora > 20:
        falando = True
    else:
        falando = False
    return falando
