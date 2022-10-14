"""Ratkojasta vastaava koodi
"""

from time import time
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from peli.liiku import mahdolliset_liikkeet
from ratkoja.taulukko import Taulukko

isoin_pisteet = [[65536, 32768, 16384, 8192], [
    512, 1024, 2048, 4096], [256, 128, 64, 32], [2, 4, 8, 16]]
tyhja_pisteet = [[2048, 4096, 6144, 8192], [16384, 14336, 12288, 10240], [18432, 20480, 22528, 24576], [32768, 30720, 28672, 26624]]


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
                pisteet += tyhja_pisteet[i][j]
                tyhjat += 1
                continue
            pisteet += nykyinen_arvo * isoin_pisteet[i][j]
    pisteet += tyhjat * 512
    return pisteet


def maksimi(taulukko, syvyys, tod, alpha, beta):
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

    liikefunktiot = {"oikea": liiku_oikea, "vasen": liiku_vasen,
                     "ylos": liiku_ylos, "alas": liiku_alas}
    isoin = (-float('inf'), None)
    liikkeet = mahdolliset_liikkeet(taulukko)
    for liike in liikkeet.items():
        if liike[1]:
            taulukko_kopio = Taulukko.kopioi(taulukko)
            pisteet = mahdollisuus(liikefunktiot[liike[0]](
                taulukko_kopio), syvyys, tod, alpha, beta)
            if pisteet > isoin[0]:
                isoin = (pisteet, liike[0])
            if isoin[0] >= beta:
                return isoin
            if isoin[0] > alpha:
                alpha = isoin[0]
    return isoin


def mahdollinen_loppu(taulukko, syvyys, tod, alpha, beta):
    """Funktio, joka katsoo, onko nykyinen ruudukko häviö

    Args:
        taulukko: peli-ruudukko
        syvyys: nykyinen syvyys
        tod: ruudukon todennäköisyys
        alpha: suurin löydetty mahdollinen arvo
        beta: pienin löydetty mahdollinen arvo

    """
    paikka, _ = Taulukko.tyhjat(taulukko)
    tyhja = paikka[0]
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
        return maksimi(taulukko_kopio, syvyys+1, tod, alpha, beta)[0] * 0.9 \
            + maksimi(taulukko_kopio_1, syvyys+1,
                      tod, alpha, beta)[0] * 0.1
    if voi_liikkua_1:
        return maksimi(taulukko_kopio, syvyys+1, tod, alpha, beta)[0]
    if voi_liikkua_2:
        return maksimi(taulukko_kopio_1, syvyys+1, tod, alpha, beta)[0]
    return kay_lapi(taulukko)


def mahdollisuus(taulukko, syvyys, tod, alpha, beta):
    """Funktio, jolla käydään läpi chance-solmujen arvot sekä kutsutaan
       pisteytysfunktiota oikealla syvyydellä

    Args:
        taulukko: peli-ruudukko
        z: nykyinen syvyys
        tod: Todennäköisyys nykyiselle ruudukolle
        alpha: Suurin löydetty mahdollinen arvo
        beta: Pienin löydetty mahdollinen arvo
    Returns:
        Nykyisen ruudukon pisteet tai painotetun keskiarvon tulevien max-solmujen pisteistä
    """

    tyhjat_paikat, maara = Taulukko.tyhjat(taulukko)
    if syvyys >= 4 and maara >= 8:
        return kay_lapi(taulukko)
    if syvyys >= 6:
        return kay_lapi(taulukko)
    if maara == 1:
        return mahdollinen_loppu(taulukko, syvyys, tod, alpha, beta)

    pienin = float('inf')

    for tyhja in tyhjat_paikat:
        pisteet = 0
        yht_tod_keskiarvolle = 0
        for uusi in [(2, 0.9), (4, 0.1)]:
            ruudukon_tod = (uusi[1] * (1/maara)) * tod
            if ruudukon_tod < 0.001:
                continue
            taulukko_kopio = Taulukko.kopioi(taulukko)
            taulukko_kopio[tyhja[0]][tyhja[1]] = uusi[0]
            paras = maksimi(taulukko_kopio, syvyys+1,
                            ruudukon_tod, alpha, beta)
            pisteet += paras[0] * uusi[1]
            yht_tod_keskiarvolle += uusi[1]

        if pisteet == 0:
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
    loppu = time()
    aika = loppu-alku
    print("Päätökseen kulunut aika: ", aika, "s")
    print("")
    if suunta is not None:
        return suunta, aika
    return "lopeta", aika
