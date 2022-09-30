"""Ratkojasta vastaava koodi
"""

from time import time
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from peli.liiku import mahdolliset_liikkeet
from ratkoja.taulukko import Taulukko


isoin_pisteet = [[7, 6, 5, 4], [6, 5, 4, 3], [5, 4, 3, 2], [4, 3, 2, 1]]    

def kay_lapi(taulukko: list):
    """Funktio, joka käy läpi nykyisen peli-ruudukon ja pisteyttää sen
    
    Args:
        taulukko: peli-ruudukko
    Returns:
        Pisteet nykyisestä peliruudukosta
    """

    tyhjat = 0
    pisteet = 0
    for i in range(4):
        for j in range(4):
            nykyinen_arvo = taulukko[i][j]
            if nykyinen_arvo == 0:
                tyhjat += 1
                continue
            pisteet += nykyinen_arvo * isoin_pisteet[i][j]
    pisteet += tyhjat * 16
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
    liikkeet = mahdolliset_liikkeet(taulukko)
    if liikkeet["vasen"]:
        taulukko_k1 = Taulukko.kopioi(taulukko)
        pisteet[0] = mahdollisuus(liiku_vasen(taulukko_k1), z)
        if pisteet[0] > isoin[0]:
            isoin = (pisteet[0], "vasen")
    if liikkeet["oikea"]:
        taulukko_k2 = Taulukko.kopioi(taulukko)
        pisteet[1] = mahdollisuus(liiku_oikea(taulukko_k2), z)
        if pisteet[1] > isoin[0]:
            isoin = (pisteet[1], "oikea")
    if liikkeet["ylos"]:
        taulukko_k3 = Taulukko.kopioi(taulukko)
        pisteet[2] = mahdollisuus(liiku_ylos(taulukko_k3), z)
        if pisteet[2] > isoin[0]:
            isoin = (pisteet[2], "ylos") 
    if liikkeet["alas"]:
        taulukko_k4 = Taulukko.kopioi(taulukko)
        pisteet[3] = mahdollisuus(liiku_alas(taulukko_k4), z)
        if pisteet[3] > isoin[0]:
            isoin = (pisteet[3], "alas")
    if z == 1:
        print(pisteet)
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

    if z == 3 and maara >= 6:
        return kay_lapi(taulukko)
    if z >= 4 and maara >= 2:
        return kay_lapi(taulukko)
    if z == 6:
        return kay_lapi(taulukko)
    #if z >= 5:
    #    return kay_lapi(taulukko)
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

    start = time() 
    suunta = maksimoi(taulukko, 1)[1]
    end = time()
    print(end-start, "sekuntia")
    if suunta is not None:
        return suunta
    else:
        return "lopeta"