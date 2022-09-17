from random import randint

def katso_ylos_alas(suunta: str, taulukko: list):
    totuudet = {1: False, 2:False, 3:False, 4:False}
    if suunta == "ylos":
        a = 0
        b = 4
        c = 1
        d = 1
    elif suunta == "alas":
        a = 3
        b = -1
        c = -1
        d = -1
    for j in range(4):
        k = 1
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
            print(i[j])
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

def voiko_liikkua(vasen: bool, oikea: bool, ylos: bool, alas: bool, taulukko: list):
    if vasen:
        return katso_vasen_oikea("vasen", taulukko)
    elif oikea:
        return katso_vasen_oikea("oikea", taulukko)
    elif ylos:
        return katso_ylos_alas("ylos", taulukko)
    elif alas:
        return katso_ylos_alas("alas", taulukko)

def uusi_peli():
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

def tulosta_taulukko(taulukko):
    for i in taulukko:
        print(i)
    print()

def uusi_palikka(taulukko):
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
    taulukko = uusi_peli()
    tulosta_taulukko(taulukko)
    taulukko = uusi_palikka(taulukko)
    tulosta_taulukko(taulukko)
    taulukko = [[4,2,2,8],[4,0,0,0],[0,0,0,0],[0,0,0,0]]
    print(voiko_liikkua(True, False, False, False, taulukko))
    print(voiko_liikkua(False, True, False, False, taulukko))
    print(voiko_liikkua(False, False, True, False, taulukko))
    print(voiko_liikkua(False, False, False, True, taulukko))

if __name__ == "__main__":
    main()
    
