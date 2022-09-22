from random import randint
from peli.liiku import liiku_alas, liiku_oikea, liiku_vasen, liiku_ylos
"""Ratkojasta vastaava koodi
"""

isoin_pisteet = [[7,6,5,4], [6,5,4,3], [5,4,3,2], [4,3,2,1]]

def kay_lapi(taulukko: list):
    pisteet = 0
    isoin = 0
    isoin_paikka = None
    tyhjat_paikat = []
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
                tyhjat_paikat.append((x,y))
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
    uudet_taulukot = []
    for a in tyhjat_paikat:
        u2_taulukko = []
        u4_taulukko = []
        for i in range(4):
            u2_taulukko.append(taulukko[i].copy())
            u4_taulukko.append(taulukko[i].copy())
        u2_taulukko[a[1]][a[0]] = 2
        u4_taulukko[a[1]][a[0]] = 4
        uudet_taulukot.append(u2_taulukko)
        uudet_taulukot.append(u4_taulukko)
    pisteet += isoin_paikka
    return pisteet, uudet_taulukot

def arvo(taulukko, z):
    pisteet, uudet_taulukot = kay_lapi(taulukko)
    if z == 0:
        return pisteet
    else:
        t2_arvot = 0
        i = 0
        for t in uudet_taulukot:
            if i % 2 != 0:
                i += 1
                continue
            t2_arvot += arvo(liiku_vasen(t.copy()), z-1)
            t2_arvot += arvo(liiku_oikea(t.copy()), z-1)
            t2_arvot += arvo(liiku_ylos(t.copy()), z-1)
            t2_arvot += arvo(liiku_alas(t.copy()), z-1)
            i += 1
        t4_arvot = 0
        j = 0
        for t in uudet_taulukot:
            if j % 2 == 0:
                j += 1
                continue
            t4_arvot += arvo(liiku_vasen(t.copy()), z-1)
            t4_arvot += arvo(liiku_oikea(t.copy()), z-1)
            t4_arvot += arvo(liiku_ylos(t.copy()), z-1)
            t4_arvot += arvo(liiku_alas(t.copy()), z-1)
            j += 1
        return 0.9*(t2_arvot/i*4)+0.1*(t4_arvot/j*4)
    

def tee_paatos(taulukko: list, mahdollisuudet: dict):
    liikkeet = [0,0,0,0]
    liikkeet[0] = arvo(liiku_vasen(taulukko.copy()), 3)
    print(0)
    liikkeet[1] = arvo(liiku_oikea(taulukko.copy()), 3)
    print(1)
    liikkeet[2] = arvo(liiku_ylos(taulukko.copy()), 3)
    print(2)
    liikkeet[3] = arvo(liiku_alas(taulukko.copy()), 3)
    print(3)
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