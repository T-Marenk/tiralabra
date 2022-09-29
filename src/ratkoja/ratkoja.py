"""Ratkojasta vastaava koodi
"""

from time import time
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from peli.liiku import mahdolliset_liikkeet
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
    for rivi in range(3):
        for paikka in range(3):
            nykyinen_arvo = taulukko[rivi][paikka]  # Nykyinen arvo
            if nykyinen_arvo == 0: 
                pisteet += .1
                continue
            oikea_arvo = taulukko[rivi][paikka+1]  # Oikealla oleva
            if oikea_arvo == 0:
                pass
            elif oikea_arvo == nykyinen_arvo/2:
                pisteet += .4
            elif nykyinen_arvo == oikea_arvo or nykyinen_arvo >= oikea_arvo:
                pisteet += .2
            else:
                pisteet -= .6
            ala_arvo = taulukko[rivi+1][paikka]  # Alla oleva
            if ala_arvo == nykyinen_arvo:
                pisteet += .3
            if nykyinen_arvo > isoin:
                isoin_paikka = isoin_pisteet[rivi][paikka]
                isoin = nykyinen_arvo 
    for rivi in range(3):
        i = taulukko[rivi]
        nykyinen_arvo = i[3]
        if nykyinen_arvo == 0:
            pisteet += .1
            continue
        ala_arvo = taulukko[rivi+1][paikka]  # Alla oleva
        if ala_arvo == nykyinen_arvo:
            pisteet += .3
        if nykyinen_arvo > isoin:
            isoin_paikka = isoin_pisteet[rivi][3]
            isoin = nykyinen_arvo
    for paikka in range(3):
        nykyinen_arvo = taulukko[3][paikka]
        if nykyinen_arvo == 0:
            pisteet += .1
            continue
        oikea_arvo = taulukko[3][paikka+1]  # Oikealla oleva
        if oikea_arvo == 0:
            pass
        elif oikea_arvo == nykyinen_arvo/2:
            pisteet += .4
        elif nykyinen_arvo == oikea_arvo or nykyinen_arvo >= oikea_arvo:
            pisteet += .2
        else:
            pisteet -= .6
        if nykyinen_arvo > isoin:
            isoin_paikka = isoin_pisteet[3][paikka]
            isoin = nykyinen_arvo
    nykyinen_arvo = taulukko[3][3]
    if nykyinen_arvo == 0:
        pisteet += .1
    elif nykyinen_arvo > isoin:
        isoin_paikka = isoin_pisteet[3][3]
    pisteet += isoin_paikka
    return pisteet

def maksimoi(taulukko, z):
    """Funktio, jolla käydään läpi max-solmujen mahdolliset arvot ja palautetaan niistä paras

    Args:
        taulukko: peli-ruudukko
        z: nykyinen syvyys
    Returns:
        tuplen, joka kertoo parhaan pistemäärän ja liikuttavan suunnan
    """

    pisteet = [0, 0, 0, 0]
    isoin = (0, None)
    t1, t2, t3, t4 = Taulukko.listat_kopioi(taulukko)
    liikkeet = mahdolliset_liikkeet(taulukko)
    if liikkeet["vasen"]:
        pisteet[0] = mahdollisuus(liiku_vasen(t1), z)
        if pisteet[0] > isoin[0]:
            isoin = (pisteet[0], "vasen")
    if liikkeet["oikea"]:
        pisteet[1] = mahdollisuus(liiku_oikea(t2), z)
        if pisteet[1] > isoin[0]:
            isoin = (pisteet[1], "oikea")
    if liikkeet["ylos"]:
        pisteet[2] = mahdollisuus(liiku_ylos(t3), z)
        if pisteet[2] > isoin[0]:
            isoin = (pisteet[2], "ylos") 
    if liikkeet["alas"]:
        pisteet[3] = mahdollisuus(liiku_alas(t4), z)
        if pisteet[3] > isoin[0]:
            isoin = (pisteet[3], "alas")
    return isoin

def mahdollisuus(taulukko, z):
    """Funktio, jolla käydään läpi chance-solmujen arvot sekä kutsutaan pisteytysfunktiota oikealla syvyydellä

    Args:
        taulukko: peli-ruudukko
        z: nykyinen syvyys
    Returns:
        Nykyisen ruudukon pisteet tai painotetun keskiarvon tulevien max-solmujen pisteistä
    """ 

    tyhat_paikat, maara = Taulukko.tyhjat(taulukko)

    if z >= 3 and maara >= 5:
        return kay_lapi(taulukko)
    if z >= 4:
        return kay_lapi(taulukko)
    if maara == 0:
        return maksimoi(taulukko, z+1) 

    keskiarvo = 0

    for tyhja in tyhat_paikat:
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 2
        keskiarvo += maksimoi(t, z+1)[0] * (0.9 * (1/maara))
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 4
        keskiarvo += maksimoi(t,z+1)[0] * (0.1 * (1/maara)) 
    return keskiarvo


def tee_paatos(taulukko: list, mahdollisuudet: dict):
    """Ratkojan aloittava funktio

    Args:
        taulukko: peli-ruudukko
        mahdollisuudet: mahdollisten liikkeiden sanakirja
    Returns:
        Parhaan liikkumissuunnan
    """

    #start = time() 
    suunta = maksimoi(taulukko, 1)[1]
    #end = time()
    #print(end-start, "sekuntia")
    if suunta is not None:
        return suunta
    else:
        return "lopeta"