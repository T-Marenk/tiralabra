from random import randint
from peli.liiku import liiku_vasen, liiku_oikea, liiku_ylos, liiku_alas
from peli.liiku import mahdolliset_liikkeet 
from ratkoja.ratkoja import tee_paatos

"""2048-pelin rungosta vastaava koodi
"""


def uusi_peli():
    """Funktio, joka luo uuden pelin

    Returns:
        Uuden peli-ruudukon
    """
    taulukko = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] #np.array([(0,0,0,0), (0,0,0,0), (0,0,0,0), (0,0,0,0)])
    edellinen = None
    while True:
        sijoitus_y = randint(0, 3)
        sijoitus_x = randint(0, 3)
        valinta = randint(1, 10)
        if valinta == 9:
            uusi = 4
        else:
            uusi = 2
        if edellinen:
            if (sijoitus_y, sijoitus_x) == edellinen:
                continue
            taulukko[sijoitus_y][sijoitus_x] = uusi
            break
        taulukko[sijoitus_y][sijoitus_x] = uusi
        edellinen = (sijoitus_y, sijoitus_x)
    return taulukko


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
    for rivi in range(4):
        paikka = 0
        for paikka in range(4):
            nykyinen = taulukko[rivi][paikka]
            if nykyinen == 0:
                maara += 1
                mahdolliset.append((rivi, paikka))
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
        mahdollisuudet = mahdolliset_liikkeet(taulukko)
        komento = input("Komento: ")
        if komento == "uusi":
            taulukko = uusi_peli()
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
        taulukko_kopio = []
        for i in taulukko:
            taulukko_kopio.append(i.copy())
        komento = tee_paatos(taulukko_kopio)
        if komento == "uusi":
            taulukko = uusi_peli()
            continue
        if komento == "vasen":
            taulukko = liiku_vasen(taulukko)
        elif komento == "oikea":
            taulukko = liiku_oikea(taulukko)
        elif komento == "ylos":
            taulukko = liiku_ylos(taulukko)
        elif komento == "alas":
            taulukko = liiku_alas(taulukko)
        elif komento == "lopeta":
            return taulukko
        uusi_palikka(taulukko)
