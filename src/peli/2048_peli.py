from random import randint

def voiko_liikkua(vasen: bool, oikea: bool, ylos: bool, alas: bool):
    totuudet = {1: False, 2:False, 3:False, 4:False}
    if vasen:
        a = 0
    elif oikea:
        a = -3
    elif ylos:
        a = 0
    elif alas:



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
    


if __name__ == "__main__":
    main()
    
