from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
from ratkoja.taulukko import Taulukko

"""Ratkojasta vastaava koodi
"""

isoin_pisteet = [[7,6,5,4], [6,5,4,3], [5,4,3,2], [4,3,2,1]]

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
    for y in range(4):
        i = taulukko[y]
        if y < 3:
            h = taulukko[y+1]
        for x in range(4):
            a = i[x] # Nykyinen arvo
            if x < 3:
                b = i[x+1] # Oikealla oleva
            if y < 3:
                c = h[x] # Alla oleva
            if a > isoin:
                isoin_paikka = isoin_pisteet[y][x]
                isoin = a
            elif a == 0:
                pisteet += 1
                continue
            if x < 3:
                if b == 0:
                    continue
                elif b == a/2:
                    pisteet += 3
                elif a == b or a >= b:
                    pisteet += 2
                else:
                    pisteet -= 3
            if y < 3 and c == a:
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
        return kay_lapi(taulukko)
    
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
            t1,t2,t3,t4 = Taulukko.listat_kopioi(t)
            t4_arvot += arvo(liiku_vasen(t1), z-1)
            t4_arvot += arvo(liiku_oikea(t2), z-1)
            t4_arvot += arvo(liiku_ylos(t3), z-1)
            t4_arvot += arvo(liiku_alas(t4), z-1)
        else:
            t1,t2,t3,t4 = Taulukko.listat_kopioi(t)
            t2_arvot += arvo(liiku_vasen(t1), z-1)
            t2_arvot += arvo(liiku_oikea(t2), z-1)
            t2_arvot += arvo(liiku_ylos(t3), z-1)
            t2_arvot += arvo(liiku_alas(t4), z-1)
        i += 1
    return 0.9*(t2_arvot/i*4)+0.1*(t4_arvot/i*4)

def tee_paatos(taulukko: list, mahdollisuudet: dict):
    """Ratkojan aloittava funktio
    
    Args:
        taulukko: peli-ruudukko
        mahdollisuudet: mahdollisten liikkeiden sanakirja
    Returns:
        Parhaan liikkumissuunnan
    """

    liikkeet = [0,0,0,0]
    t1,t2,t3,t4 = Taulukko.listat_kopioi(taulukko)    
    liikkeet[0] = arvo(liiku_vasen(t1), 3)
    liikkeet[1] = arvo(liiku_oikea(t2), 3)
    liikkeet[2] = arvo(liiku_ylos(t3), 3)
    liikkeet[3] = arvo(liiku_alas(t4), 3)
    isoin = max(liikkeet)
    suunta = liikkeet.index(isoin)
    if suunta == 0:
        return "vasen"
    elif suunta == 1:
        return "oikea"
    elif suunta == 2:
        return "ylos"
    elif suunta == 3:
        return "alas"