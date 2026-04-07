def resposta(cigarros, anos):
    cigarros = int(cigarros)
    anos = int (anos)

    minutos = (cigarros * 10) * (365 * anos)

    morte = minutos/1440
    dias = round (morte)
    return int(morte)
