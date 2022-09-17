from random import randint
from tkinter import W
from liiku import liiku_vasen, liiku_oikea, liiku_ylos, liiku_alas

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
            print(i[j])
            if i[j] == 0:
                totuudet[k] = True
                edellinen = i[j]
                continue
            elif edellinen == None:
                edellinen = i[j]
                continue
            else:
                if i[j] == edellinen and i[j] != 0:
                    return True
                elif totuudet[k] == True:
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
        a = 1
        b = 0
        c = 4
        d = 1
    elif suunta == "oikea":
        a = 1
        b = 3
        c = -1
        d = -1
    for i in taulukko:
        k = 1
        edellinen = None
        for j in range(b,c,d):
            if i[j] == 0:
                totuudet[k] = True
            elif edellinen == None:
                edellinen = i[j]
                continue
            else:
                if i[j] == edellinen:
                    return True
                elif totuudet[k] == True:
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

    pass

if __name__ == "__main__":
    #taulukko = uusi_peli()
    #tulosta_taulukko(taulukko)
    #taulukko = uusi_palikka(taulukko)
    #tulosta_taulukko(taulukko)
    taulukko = [[4,2,2,8],[8,0,4,0],[4,4,8,8],[2,0,16,16]]
    #print(katso_vasen_oikea("vasen", taulukko))
    #print(katso_vasen_oikea("oikea", taulukko))
    #print(katso_ylos_alas("ylos", taulukko))
    #print(katso_ylos_alas("alas", taulukko))
    tulosta_taulukko(taulukko)
    taulukko = liiku_alas(taulukko)
    tulosta_taulukko(taulukko)

