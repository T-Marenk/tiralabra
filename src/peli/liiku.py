"""2048-pelin liikkumisesta vastaava koodi
"""


def liiku_vasen(taulukko: list):
    """Liikuttaa peliruutua vasemmalle

    Args:
        taulukko: peli-ruudukko
    Returns:
        Liikutetun peliruudun
    """

    k = 0
    for i in taulukko:
        edellinen = None
        e_paikka = None
        tyhja = None
        for j in range(4):
            if i[j] == 0:
                if tyhja is None:
                    tyhja = j
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = j
                if tyhja is not None:
                    taulukko[k][tyhja] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja += 1
            else:
                if tyhja is not None and tyhja > e_paikka:
                    taulukko[k][e_paikka] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                else:
                    taulukko[k][e_paikka] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                    tyhja = j
        k += 1
    return taulukko


def liiku_oikea(taulukko: list):
    """Liikuttaa peliruutua oikealle

    Args:
        taulukko: peli-ruudukko
    Returns:
        Liikutetun peliruudun
    """

    k = 0
    for i in taulukko:
        edellinen = None
        e_paikka = None
        tyhja = None
        for j in range(3, -1, -1):
            if i[j] == 0:
                if tyhja is None:
                    tyhja = j
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = j
                if tyhja is not None:
                    taulukko[k][tyhja] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja -= 1
            else:
                if tyhja is not None and tyhja < e_paikka:
                    taulukko[k][e_paikka] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                else:
                    taulukko[k][e_paikka] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                    tyhja = j
        k += 1
    return taulukko


def liiku_ylos(taulukko: list):
    """Liikuttaa peliruudukko ylös

    Args:
        taulukko: peliruudukko
    Returns:
        liikutetun peliruudukon
    """

    for j in range(4):
        edellinen = None
        e_paikka = None
        tyhja = None
        for k in range(4):
            i = taulukko[k]
            if i[j] == 0:
                if tyhja is None:
                    tyhja = k
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = k
                if tyhja is not None:
                    taulukko[tyhja][j] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja += 1
            else: 
                if tyhja is not None and tyhja > e_paikka:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                else:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                    tyhja = k
    return taulukko


def liiku_alas(taulukko: list):
    """Liikuttaa peliruudukko alas

    Args:
        taulukko: peliruudukko
    Returns:
        liikutetun peliruudukon
    """

    for j in range(4):
        edellinen = None
        e_paikka = None
        tyhja = None
        for k in range(3, -1, -1):
            i = taulukko[k]
            if i[j] == 0:
                if tyhja is None:
                    tyhja = k
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = k
                if tyhja is not None:
                    taulukko[tyhja][j] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja -= 1
            else: 
                if tyhja is not None and tyhja < e_paikka:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                else:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                    tyhja = k
    return taulukko


def mahdolliset_liikkeet(taulukko):
    """Katsoo mahdolliset nykyisestä peliruudusta

    Args:
        taulukko: peliruudukko
    Returns:
        sanakirjan, joka kertoo, mihin suuntiin on mahdollista liikkua
    """

    sarake_0 = [False, False, False, False]
    sarake_ei_0 = [False, False, False, False]
    sarake_edellinen = [None, None, None, None]
    liikkeet = {"vasen": False, "oikea": False, "ylos": False, "alas": False}

    for i in range(4):
        rivi_0 = False
        rivi_ei_0 = False
        rivi_edellinen = None

        for j in range(4):
            nykyinen = taulukko[i][j]

            if nykyinen == 0:
                rivi_0 = True
                sarake_0[j] = True

                if rivi_ei_0:
                    liikkeet["oikea"] = True
                if sarake_ei_0[j]:
                    liikkeet["alas"] = True

            else:
                rivi_ei_0 = True
                sarake_ei_0[j] = True

                if rivi_0:
                    liikkeet["vasen"] = True
                if sarake_0[j]:
                    liikkeet["ylos"] = True

                if rivi_edellinen is not None and rivi_edellinen == nykyinen:
                    liikkeet["vasen"] = True
                    liikkeet["oikea"] = True
                rivi_edellinen = nykyinen
                if sarake_edellinen[j] is not None and sarake_edellinen[j] == nykyinen:
                    liikkeet["ylos"] = True
                    liikkeet["alas"] = True
                sarake_edellinen[j] = nykyinen
    return liikkeet


def tulosta_taulukko(taulukko): # pragma: no cover
    """Funktio, joka tulostaa peli-ruudukon

    Args:
        taulukko: Peli-ruudukko
    """

    for i in taulukko:
        print(i)
    print("")
