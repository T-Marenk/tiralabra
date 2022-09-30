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

def maksimi(taulukko, z, tod, alpha, beta):
    """Funktio, jolla käydään läpi max-solmujen mahdolliset arvot ja palautetaan niistä paras

    Args:
        taulukko: peli-ruudukko
        z: nykyinen syvyys
    Returns:
        tuplen, joka kertoo parhaan pistemäärän ja liikuttavan suunnan
    """

    isoin = (-float('inf'), None)
    liikkeet = mahdolliset_liikkeet(taulukko)
    if liikkeet["vasen"]:
        taulukko_k1 = Taulukko.kopioi(taulukko)
        pisteet = mahdollisuus(liiku_vasen(taulukko_k1), z, tod, alpha, beta)
        if pisteet > isoin[0]:
            isoin = (pisteet, "vasen")
        if isoin[0] >= beta:
            return isoin
        if isoin[0] > alpha:
            alpha = isoin[0]
    if liikkeet["oikea"]:
        taulukko_k2 = Taulukko.kopioi(taulukko)
        pisteet = mahdollisuus(liiku_oikea(taulukko_k2), z, tod, alpha, beta)
        if pisteet > isoin[0]:
            isoin = (pisteet, "oikea")
        if isoin[0] >= beta:
            return isoin
        if isoin[0] > alpha:
            alpha = isoin[0]
    if liikkeet["ylos"]:
        taulukko_k3 = Taulukko.kopioi(taulukko)
        pisteet = mahdollisuus(liiku_ylos(taulukko_k3), z, tod, alpha, beta)
        if pisteet > isoin[0]:
            isoin = (pisteet, "ylos") 
        if isoin[0] >= beta:
            return isoin
        if isoin[0] > alpha:
            alpha = isoin[0]
    if liikkeet["alas"]:
        taulukko_k4 = Taulukko.kopioi(taulukko)
        pisteet = mahdollisuus(liiku_alas(taulukko_k4), z, tod, alpha, beta)
        if pisteet > isoin[0]:
            isoin = (pisteet, "alas") 
        if isoin[0] >= beta:
            return isoin
        if isoin[0] > alpha:
            alpha = isoin[0]
    return isoin

def mahdollisuus(taulukko, z, tod, alpha, beta):
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
    if z == 6:
        return kay_lapi(taulukko)
    if maara == 0:
        liikkeet = mahdolliset_liikkeet(taulukko)
        voi_liikkua = False
        suunnat = ["vasen", "oikea", "ylos", "alas"]
        for suunta in suunnat:
            if liikkeet[suunta]:
               voi_liikkua = True 
        if voi_liikkua:
            return maksimi(taulukko, z+1)
        else:
            return kay_lapi(taulukko)

    huonoin = float('inf')

    for tyhja in tyhat_paikat:
        keskiarvo = 0
        yht_tod_keskiarvolle = 0
    
        ruudukon_tod = (0.9 * (1/maara)) * tod
        if ruudukon_tod < 0.0001:
            pass
        else:
            t = Taulukko.kopioi(taulukko)
            t[tyhja[0]][tyhja[1]] = 2
            paras = maksimi(t, z+1, ruudukon_tod, alpha, beta)
            keskiarvo += paras[0] * 0.9 * (1/maara)
            yht_tod_keskiarvolle += 0.9 * (1/maara)

        ruudukon_tod = (0.1 * (1/maara)) * tod
        if ruudukon_tod < 0.0001:
            pass
        else:
            t = Taulukko.kopioi(taulukko)
            t[tyhja[0]][tyhja[1]] = 4
            paras = maksimi(t,z+1, ruudukon_tod, alpha, beta)
            keskiarvo += paras[0] * 0.1 *(1/maara)
            yht_tod_keskiarvolle += 0.1 * (1/maara)
        if yht_tod_keskiarvolle == 0:
            keskiarvo = kay_lapi(taulukko)
        else:
            keskiarvo /= yht_tod_keskiarvolle
        if keskiarvo < huonoin:
            huonoin = keskiarvo
        if huonoin <= alpha:
            return huonoin
        if huonoin < beta:
            beta = huonoin
    return huonoin


def tee_paatos(taulukko: list, mahdollisuudet: dict):
    """Ratkojan aloittava funktio

    Args:
        taulukko: peli-ruudukko
        mahdollisuudet: mahdollisten liikkeiden sanakirja
    Returns:
        Parhaan liikkumissuunnan
    """

    start = time() 
    alpha = -float('inf')
    beta = float('inf')
    suunta = maksimi(taulukko, 1, 1, alpha, beta)[1]
    end = time()
    print(end-start, "sekuntia")
    if suunta is not None:
        return suunta
    else:
        return "lopeta"

if __name__ == "__main__":
    taulukko = [[2048, 128, 64, 2],
                [1024, 256, 4, 16],
                [16, 128, 16, 4],
                [0, 2, 2, 2]]

 