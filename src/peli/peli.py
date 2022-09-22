from random import randint
from peli.liiku import liiku_vasen, liiku_oikea, liiku_ylos, liiku_alas
from ratkoja.ratkoja import tee_paatos

"""2048-pelin rungosta vastaava koodi
"""

def uusi_peli():
    """Funktio, joka luo uuden pelin
    
    Returns:
        Uuden peli-ruudukon
    """
    taulukko = [[0]*4 for i in range(4)]
    edellinen = None
    for i in range(2):
        while True:
            sijoitus_y = randint(0,3)
            sijoitus_x = randint(0,3)
            valinta = randint(1, 10)
            if valinta == 9:
                uusi = 4
            else:
                uusi = 2
            if edellinen:
                if (sijoitus_y,sijoitus_x)==edellinen:
                    continue
                else:
                    taulukko[sijoitus_y][sijoitus_x] = uusi
                    break
            else:
                taulukko[sijoitus_y][sijoitus_x] = uusi
                edellinen = (sijoitus_y,sijoitus_x) 
                break
    return taulukko

def katso_ylos_alas(suunta: str, taulukko: list):
    """Fuktio, joka katsoo, voiko ruudukkoa liikuttaa ylös tai alas

    Args:
        suunta: Suunta, johon ruudukon liikkuvuus tarkistetaan
        taulukko: Peli ruudukko
    
    Returns:
        Totuusarvon siitä, voiko ruudukkoa liikuttaa kyseiseen suuntaan
    """

    totuudet = {1: False, 2:False, 3:False, 4:False}
    if suunta == "ylos":
        a = 0
        b = 4
        c = 1
    elif suunta == "alas":
        a = 3
        b = -1
        c = -1
    k = 1
    for j in range(4):
        edellinen = None
        for i in range(a,b,c):
            i = taulukko[i]
            if i[j] == 0:
                totuudet[k] = True
                continue
            elif edellinen == None:
                edellinen = i[j]
                if totuudet[k]:
                    return True
                continue
            else:
                if i[j] == edellinen:
                    return True
                elif totuudet[k]:
                    return True
                edellinen = i[j]
        k += 1
    return False

def katso_vasen_oikea(suunta: str, taulukko: list):
    """Funktio, joka katsoo, voiko ruudukkoa liikuttaa vasemmalle tai oikealle

    Args:
        suunta: Suunta, johon ruudukon liikkuvuus tarkistetaan
        taulukko: Peli ruudukko
    
    Returns:
        Totuusarvon siitä, voiko ruudukkoa liikuttaa tarkistettavaan suuntaan
    """

    totuudet = {1: False, 2:False, 3:False, 4:False}
    if suunta == "vasen":
        a = 0
        b = 4
        c = 1
    elif suunta == "oikea":
        a = 3
        b = -1
        c = -1
    k = 1
    for i in taulukko:
        edellinen = None
        for j in range(a,b,c):
            if i[j] == 0:
                totuudet[k] = True
            elif edellinen == None:
                edellinen = i[j]
                if totuudet[k]:
                    return True
                continue
            else:
                if i[j] == edellinen:
                    return True
                elif totuudet[k]:
                    return True
                edellinen = i[j]
        k += 1
    return False

def tulosta_taulukko(taulukko):
    """Funktio, joka tulostaa peli-ruudukon

    Args:
        taulukko: Peli-ruudukko
    """

    for i in taulukko:
        print(i)
    print()

def uusi_palikka(taulukko):
    """Funktio, joka lisää peli-ruudukkoon uuden palikan
    
    Args:
        taulukko: Peli-ruudukko
    Returns:
        Peli-ruudukon, johon on lisätty uusi palikka
    """

    mahdolliset = []
    maara = 0
    a = 0
    for i in taulukko:
        b = 0
        for j in i:
            if j == 0:
                maara += 1
                mahdolliset.append((a,b))
            b += 1
        a += 1
    sijoitus = randint(0, maara-1)
    valinta = randint(1, 10)
    if valinta == 9:
        uusi = 4
    else:
        uusi = 2
    paikka = mahdolliset[sijoitus]
    taulukko[paikka[0]][paikka[1]] = uusi
    return taulukko


def main():
    """Peliä pyörittävä funktio
    """

    taulukko = uusi_peli()
    while True:
        tulosta_taulukko(taulukko)
        mahdollisuudet = {}
        mahdollisuudet["vasen"] = katso_vasen_oikea("vasen", taulukko)
        mahdollisuudet["oikea"] = katso_vasen_oikea("oikea", taulukko)
        mahdollisuudet["ylos"] = katso_ylos_alas("ylos", taulukko)
        mahdollisuudet["alas"] = katso_ylos_alas("alas", taulukko)
        komento = input("Komento: ")
        if komento == "uusi":
            taulukko = uusi_peli()
            continue
        elif komento == "vasen":
            if not mahdollisuudet["vasen"]:
                continue
            taulukko = liiku_vasen(taulukko)
        elif komento == "oikea":
            if not mahdollisuudet["oikea"]:
                continue
            taulukko = liiku_oikea(taulukko)
        elif komento == "ylos":
            if not mahdollisuudet["ylos"]:
                continue
            taulukko = liiku_ylos(taulukko)
        elif komento == "alas":
            if not mahdollisuudet["alas"]:
                continue
            taulukko = liiku_alas(taulukko)
        elif komento == "lopeta":
            break
        uusi_palikka(taulukko)

def main_ratkoja():
    """Ratkojan peliä pyörittävä funktio
    """
    
    taulukko = uusi_peli()
    while True:
        tulosta_taulukko(taulukko)
        mahdollisuudet = {}
        mahdollisuudet["vasen"] = katso_vasen_oikea("vasen", taulukko)
        mahdollisuudet["oikea"] = katso_vasen_oikea("oikea", taulukko)
        mahdollisuudet["ylos"] = katso_ylos_alas("ylos", taulukko)
        mahdollisuudet["alas"] = katso_ylos_alas("alas", taulukko)
        komento = tee_paatos(taulukko.copy(), mahdollisuudet)
        if komento == "uusi":
            taulukko = uusi_peli()
            continue
        elif komento == "vasen":
            if not mahdollisuudet["vasen"]:
                continue
            taulukko = liiku_vasen(taulukko)
        elif komento == "oikea":
            if not mahdollisuudet["oikea"]:
                continue
            taulukko = liiku_oikea(taulukko)
        elif komento == "ylos":
            if not mahdollisuudet["ylos"]:
                continue
            taulukko = liiku_ylos(taulukko)
        elif komento == "alas":
            if not mahdollisuudet["alas"]:
                continue
            taulukko = liiku_alas(taulukko)
        elif komento == "lopeta":
            break
        uusi_palikka(taulukko)