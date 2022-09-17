from random import randint

"""Ratkojasta vastaava koodi
"""

def tee_paatos(mahdollisuudet: dict):
    mahdollisuudet = mahdollisuudet.values()
    if True not in mahdollisuudet:
        return "lopeta"
    suunta = randint(1,4)
    if suunta == 1:
        return "vasen"
    elif suunta == 2:
        return "oikea"
    elif suunta == 3:
        return "ylos"
    elif suunta == 4:
        return "alas"
