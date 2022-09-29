"""Ratkojasta vastaava koodi
"""

from time import time
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from peli.liiku import katso_vasen_oikea, katso_ylos_alas
from ratkoja.taulukko import Taulukko


isoin_pisteet = [[7, 6, 5, 4], [6, 5, 4, 3], [5, 4, 3, 2], [4, 3, 2, 1]]


def kay_lapi(taulukko: list):
    """Funktio, joka pisteyttää nykyisen ruudukon

    Args:
        taulukko: peli-ruudukko
    Returns:
        Ruudukon pisteet sekä uudet listat
    """

    pisteet = 0
    isoin = 0
    isoin_paikka = None
    for rivi in range(4):
        i = taulukko[rivi]
        if rivi < 3:
            seuraava_rivi = taulukko[rivi+1]
        for paikka in range(4):
            nykyinen_arvo = i[paikka]  # Nykyinen arvo
            if paikka < 3:
                oikea_arvo = i[paikka+1]  # Oikealla oleva
            if rivi < 3:
                ala_arvo = seuraava_rivi[paikka]  # Alla oleva
            if nykyinen_arvo > isoin:
                isoin_paikka = isoin_pisteet[rivi][paikka]
                isoin = nykyinen_arvo
            elif nykyinen_arvo == 0:
                pisteet += .1
                continue
            if paikka < 3:
                if oikea_arvo == 0:
                    continue
                if oikea_arvo == nykyinen_arvo/2:
                    pisteet += .4
                elif nykyinen_arvo == oikea_arvo or nykyinen_arvo >= oikea_arvo:
                    pisteet += .2
                else:
                    pisteet -= .6
            if rivi < 3 and ala_arvo == nykyinen_arvo:
                pisteet += .3
    pisteet += isoin_paikka
    return pisteet

def maksimoi(taulukko, z):
    pisteet = [0, 0, 0, 0]
    isoin = (0, None)
    t1, t2, t3, t4 = Taulukko.listat_kopioi(taulukko)
    if katso_vasen_oikea("vasen", t1):
        pisteet[0] = mahdollisuus(liiku_vasen(t1), z+1)
        if pisteet[0] > isoin[0]:
            isoin = (pisteet[0], "vasen")
    if katso_vasen_oikea("oikea", t2):
        pisteet[1] = mahdollisuus(liiku_oikea(t2), z+1)
        if pisteet[1] > isoin[0]:
            isoin = (pisteet[1], "oikea")
    if katso_ylos_alas("ylos", t3):
        pisteet[2] = mahdollisuus(liiku_ylos(t3), z+1)
        if pisteet[2] > isoin[0]:
            isoin = (pisteet[2], "ylos") 
    if katso_ylos_alas("alas", t4):
        pisteet[3] = mahdollisuus(liiku_alas(t4), z+1)
        if pisteet[3] > isoin[0]:
            isoin = (pisteet[3], "alas")
    return isoin

def mahdollisuus(taulukko, z):
    """Funktio, jolla kutsutaan seuraavien taulukoiden läpikäynti ja kutsutaan taulukon pisteytys

    Args:
        taulukko: peli-ruudukko
    Returns:
        Nykyisen ruudukon pisteet tai painotetun keskiarvon tulevien ruudukoiden pisteistä
    """ 

    tyhat_paikat, maara = Taulukko.tyhjat(taulukko)

    if z >= 3 and maara >= 6:
        return kay_lapi(taulukko)
    if z >= 4:
        return kay_lapi(taulukko)
    if maara == 0:
        return maksimoi(taulukko, z) 

    keskiarvo = 0

    for tyhja in tyhat_paikat:
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 2
        keskiarvo += maksimoi(t, z)[0] * (0.9 * (1/maara))
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 4
        keskiarvo += maksimoi(t,z)[0] * (0.1 * (1/maara)) 
    return keskiarvo


def tee_paatos(taulukko: list, mahdollisuudet: dict):
    """Ratkojan aloittava funktio

    Args:
        taulukko: peli-ruudukko
        mahdollisuudet: mahdollisten liikkeiden sanakirja
    Returns:
        Parhaan liikkumissuunnan
    """

    start = time()
    liikkeet = [0, 0, 0, 0]
    t1, t2, t3, t4 = Taulukko.listat_kopioi(taulukko)
    if mahdollisuudet["vasen"]:
        liikkeet[0] = mahdollisuus(liiku_vasen(t1), 1)
    if mahdollisuudet["oikea"]:
        liikkeet[1] = mahdollisuus(liiku_oikea(t2), 1)
    if mahdollisuudet["ylos"]:
        liikkeet[2] = mahdollisuus(liiku_ylos(t3), 1)
    if mahdollisuudet["alas"]:
        liikkeet[3] = mahdollisuus(liiku_alas(t4), 1)
    isoin = max(liikkeet)
    if isoin > 0:
        suunta = liikkeet.index(isoin)
    else:
        suunta = 4
    end = time()
    print(end-start, "sekuntia")
    if suunta == 0:
        return "vasen"
    elif suunta == 1:
        return "oikea"
    elif suunta == 2:
        return "ylos"
    elif suunta == 3:
        return "alas"
    else:
        return "lopeta"
