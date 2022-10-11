"""Ratkojasta vastaava koodi
"""

from time import time
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from peli.liiku import mahdolliset_liikkeet
from ratkoja.taulukko import Taulukko


isoin_pisteet = [[7, 6, 5, 4], [6, 5, 4, 3], [5, 4, 3, 2], [4, 3, 2, 1]]    
# isoin_pisteet = [[16, 9, 8, 1], [15, 10, 7, 2], [14, 11, 6, 3], [13, 12, 5, 4]]    

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
        tod: Todennäköisyys nykyiselle ruudukolle
        alpha: Suurin löydetty mahdollinen arvo
        beta: Pienin löydetty mahdollinen arvo
    Returns:
        tuplen, joka kertoo parhaan pistemäärän ja liikuttavan suunnan
    """
    liikefunktiot = {"oikea": liiku_oikea, "vasen": liiku_vasen, "ylos": liiku_ylos, "alas": liiku_alas}
    isoin = (-float('inf'), None)
    liikkeet = mahdolliset_liikkeet(taulukko)
    for liike in liikkeet:
        if liikkeet[liike]:
            taulukko_kopio = Taulukko.kopioi(taulukko)
            pisteet = mahdollisuus(liikefunktiot[liike](taulukko_kopio), z, tod, alpha, beta)
            if pisteet > isoin[0]:
                isoin = (pisteet, liike)
            if isoin[0] >= beta:
                return isoin
            if isoin[0] > alpha:
                alpha = isoin[0]
    return isoin
    """
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
    """

def mahdollisuus(taulukko, z, tod, alpha, beta):
    """Funktio, jolla käydään läpi chance-solmujen arvot sekä kutsutaan pisteytysfunktiota oikealla syvyydellä

    Args:
        taulukko: peli-ruudukko
        z: nykyinen syvyys
        tod: Todennäköisyys nykyiselle ruudukolle
        alpha: Suurin löydetty mahdollinen arvo
        beta: Pienin löydetty mahdollinen arvo
    Returns:
        Nykyisen ruudukon pisteet tai painotetun keskiarvon tulevien max-solmujen pisteistä
    """ 

    tyhat_paikat, maara = Taulukko.tyhjat(taulukko)
    if z >= 3 and maara >= 5:
        return kay_lapi(taulukko)
    if z == 5:
        return kay_lapi(taulukko)
    if maara == 1:
        tyhja = tyhat_paikat[0]
        taulukko_kopio = Taulukko.kopioi(taulukko)
        taulukko_kopio[tyhja[0]][tyhja[1]] = 2

        liikkeet_1 = mahdolliset_liikkeet(taulukko_kopio)
        voi_liikkua_1 = False
        suunnat = ["vasen", "oikea", "ylos", "alas"]
        for suunta in suunnat:
            if liikkeet_1[suunta]:
               voi_liikkua_1 = True 
        
        taulukko_kopio_1 = Taulukko.kopioi(taulukko)
        taulukko_kopio_1[tyhja[0]][tyhja[1]] = 4

        liikkeet_1 = mahdolliset_liikkeet(taulukko_kopio_1)
        voi_liikkua_2 = False
        suunnat = ["vasen", "oikea", "ylos", "alas"]
        for suunta in suunnat:
            if liikkeet_1[suunta]:
               voi_liikkua_2 = True 

        if voi_liikkua_1 and voi_liikkua_2:
            return maksimi(taulukko_kopio, z+1, tod, alpha, beta)[0] * 0.9 + maksimi(taulukko_kopio_1, z+1, tod, alpha, beta)[0] * 0.1
        elif voi_liikkua_1: 
            return maksimi(taulukko_kopio, z+1, tod, alpha, beta)[0]
        elif voi_liikkua_2:
            return maksimi(taulukko_kopio_1, z+1, tod, alpha, beta)[0]
        else:
            return kay_lapi(taulukko) 

    pienin = float('inf')

    for tyhja in tyhat_paikat:
        pisteet = 0
        yht_tod_keskiarvolle = 0
    
        ruudukon_tod = (0.9 * (1/maara)) * tod
        if ruudukon_tod < 0.001:
            pass
        else:
            t = Taulukko.kopioi(taulukko)
            t[tyhja[0]][tyhja[1]] = 2
            paras = maksimi(t, z+1, ruudukon_tod, alpha, beta)
            pisteet += paras[0] * 0.9
            yht_tod_keskiarvolle += 0.9

        ruudukon_tod = (0.1 * (1/maara)) * tod
        if ruudukon_tod < 0.001:
            pass
        else:
            t = Taulukko.kopioi(taulukko)
            t[tyhja[0]][tyhja[1]] = 4
            paras = maksimi(t,z+1, ruudukon_tod, alpha, beta)
            pisteet += paras[0] * 0.1
            yht_tod_keskiarvolle += 0.1

        if yht_tod_keskiarvolle == 0:
            pisteet = kay_lapi(taulukko)
        else:
            pisteet /= yht_tod_keskiarvolle
        if pisteet < pienin:
            pienin = pisteet
        if pienin <= alpha:
            return pienin
        if pienin < beta:
            beta = pienin
    return pienin


def tee_paatos(taulukko: list):
    """Ratkojan aloittava funktio

    Args:
        taulukko: peli-ruudukko
    Returns:
        Parhaan liikkumissuunnan
    """

    alku = time() 
    alpha = -float('inf')
    beta = float('inf')
    suunta = maksimi(taulukko, 1, 1, alpha, beta)[1]
    print(suunta)
    loppu = time()
    aika = loppu-alku
    print("Päätökseen kulunut aika: ", aika, "s")
    print("")
    if suunta is not None:
        return suunta, aika
    else:
        return "lopeta", aika

if __name__ == "__main__":
    taulukko = [[2048, 128, 64, 2],
                [1024, 256, 4, 16],
                [16, 128, 16, 4],
                [0, 2, 2, 2]]
"""
[2048, 128, 4, 2]
[1024, 256, 8, 4]
[128, 64, 32, 2]
[16, 2, 4, 0]
"""