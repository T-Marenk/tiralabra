"""2048-pelin liikkumisesta vastaava koodi
"""

def liiku_vasen(taulukko: list):
    k = 0
    for i in taulukko:
        edellinen = None
        e_paikka = None
        tyhja = None
        for j in range(4):
            if i[j] == 0:
                if tyhja == None:
                    tyhja = j
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = j
                if tyhja != None:
                    taulukko[k][tyhja] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja += 1
            else:
                if tyhja != None and tyhja < e_paikka:
                    taulukko[k][tyhja] = i[j] * 2
                    edellinen = None
                    taulukko[k][e_paikka] = 0
                    taulukko[k][j] = 0
                    tyhja += 1
                elif tyhja != None and tyhja > e_paikka:
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
    k = 0
    for i in taulukko:
        edellinen = None
        e_paikka = None
        tyhja = None
        for j in range(3,-1,-1):
            if i[j] == 0:
                if tyhja == None:
                    tyhja = j
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = j
                if tyhja != None:
                    taulukko[k][tyhja] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja -= 1
            else:
                if tyhja != None and tyhja > e_paikka:
                    taulukko[k][tyhja] = i[j] * 2
                    edellinen = None
                    taulukko[k][e_paikka] = 0
                    taulukko[k][j] = 0
                    tyhja -= 1
                elif tyhja != None and tyhja < e_paikka:
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
    for j in range(4):
        edellinen = None
        e_paikka = None
        tyhja = None
        for k in range(4):
            i = taulukko[k]
            if i[j] == 0:
                if tyhja == None:
                    tyhja = k
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = k
                if tyhja != None:
                    taulukko[tyhja][j] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja += 1
            else:
                if tyhja != None and tyhja < e_paikka:
                    taulukko[tyhja][j] = i[j] * 2
                    edellinen = None
                    taulukko[e_paikka][j] = 0
                    taulukko[k][j] = 0
                    tyhja += 1
                elif tyhja != None and tyhja > e_paikka:
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
    for j in range(4):
        edellinen = None
        e_paikka = None
        tyhja = None
        for k in range(3, -1, -1):
            i = taulukko[k]
            if i[j] == 0:
                if tyhja == None:
                    tyhja = k
            elif edellinen != i[j]:
                edellinen = i[j]
                e_paikka = k
                if tyhja != None:
                    taulukko[tyhja][j] = i[j]
                    taulukko[k][j] = 0
                    e_paikka = tyhja
                    tyhja -= 1
            else:
                if tyhja != None and tyhja > e_paikka:
                    taulukko[tyhja][j] = i[j] * 2
                    edellinen = None
                    taulukko[e_paikka][j] = 0
                    taulukko[k][j] = 0
                    tyhja -= 1
                elif tyhja != None and tyhja < e_paikka:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                else:
                    taulukko[e_paikka][j] = i[j] * 2
                    edellinen = None
                    taulukko[k][j] = 0
                    tyhja = k
    return taulukko