"""Ratkojasta vastaava koodi
"""

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
                pisteet += 1
                continue
            if paikka < 3:
                if oikea_arvo == 0:
                    continue
                if oikea_arvo == nykyinen_arvo/2:
                    pisteet += 3
                elif nykyinen_arvo == oikea_arvo or nykyinen_arvo >= oikea_arvo:
                    pisteet += 2
                else:
                    pisteet -= 3
            if rivi < 3 and ala_arvo == nykyinen_arvo:
                pisteet += 2
    pisteet += isoin_paikka
    return pisteet


def arvo(taulukko, z):
    """Funktio, jolla kutsutaan seuraavien taulukoiden läpikäynti ja kutsutaan taulukon pisteytys

    Args:
        taulukko: peli-ruudukko
    Returns:
        Nykyisen ruudukon pisteet tai painotetun keskiarvon tulevien ruudukoiden pisteistä
    """
    if z == 0:
        b = kay_lapi(taulukko)
        return b

    tyhat_paikat = Taulukko.tyhjat(taulukko)
    uudet_taulukot = []
    for tyhja in tyhat_paikat:
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 2
        uudet_taulukot.append(t)
        t = Taulukko.kopioi(taulukko)
        t[tyhja[0]][tyhja[1]] = 4
        uudet_taulukot.append(t)
    t2_arvot = 0
    t4_arvot = 0
    i = 0
    for t in uudet_taulukot:
        if i % 2 != 0:
            t1, t2, t3, t4 = Taulukko.listat_kopioi(t)
            if katso_vasen_oikea("vasen", t1):
                t4_arvot += arvo(liiku_vasen(t1), z-1)
            if katso_vasen_oikea("oikea", t2):
                t4_arvot += arvo(liiku_oikea(t2), z-1)
            if katso_ylos_alas("ylos", t3):
                t4_arvot += arvo(liiku_ylos(t3), z-1)
            if katso_ylos_alas("alas", t4):
                t4_arvot += arvo(liiku_alas(t4), z-1)
        else:
            t1, t2, t3, t4 = Taulukko.listat_kopioi(t)
            if katso_vasen_oikea("vasen", t1):
                t2_arvot += arvo(liiku_vasen(t1), z-1)
            if katso_vasen_oikea("oikea", t2):
                t2_arvot += arvo(liiku_oikea(t2), z-1)
            if katso_ylos_alas("ylos", t3):
                t2_arvot += arvo(liiku_ylos(t3), z-1)
            if katso_ylos_alas("alas", t4):
                t2_arvot += arvo(liiku_alas(t4), z-1)
        i += 1
    return 0.9*(t2_arvot/(i*4))+0.1*(t4_arvot/(i*4))


def tee_paatos(taulukko: list, mahdollisuudet: dict):
    """Ratkojan aloittava funktio

    Args:
        taulukko: peli-ruudukko
        mahdollisuudet: mahdollisten liikkeiden sanakirja
    Returns:
        Parhaan liikkumissuunnan
    """

    liikkeet = [0, 0, 0, 0]
    t1, t2, t3, t4 = Taulukko.listat_kopioi(taulukko)
    if mahdollisuudet["vasen"]:
        liikkeet[0] = arvo(liiku_vasen(t1), 2)
    if mahdollisuudet["oikea"]:
        liikkeet[1] = arvo(liiku_oikea(t2), 2)
    if mahdollisuudet["ylos"]:
        liikkeet[2] = arvo(liiku_ylos(t3), 2)
    if mahdollisuudet["alas"]:
        liikkeet[3] = arvo(liiku_alas(t4), 2)
    isoin = max(liikkeet)
    if isoin > 0:
        suunta = liikkeet.index(isoin)
    else:
        suunta = 4
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
