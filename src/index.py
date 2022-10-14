"""Kutsuu pelin netti version ratkojalle
"""

from peli.netti_peli import main as run
from config import AIKA_TIEDOSTO_POLKU

def main():
    """Kutsuu pelin
    """
    
    kerrat = int(input("Montako kertaa haluat ajaa ratkojan?\n"))
    suurimmat = []
    s_ajat = []
    p_ajat = []
    keskiarvot = []
    for i in range(kerrat):
        print("Kerta", i+1)
        suurin_palikka, suurin, pienin, keskiarvo = run()
        with open(AIKA_TIEDOSTO_POLKU, "a") as tie:
            tie.write(f"Suurin laatta: {suurin_palikka}\nSuurin aika: {suurin} s\nPienin aika: {pienin} s\nKeskiarvot ajoista: {keskiarvo}\n\n")
        suurimmat.append(suurin_palikka)
        s_ajat.append(suurin)
        p_ajat.append(pienin)
        keskiarvot.append(keskiarvo)

    print("Suurimmat", suurimmat)
    print("Suurimmat ajat", s_ajat)
    print("Pienimmät ajat", p_ajat)
    print("Keskiarvot ajoista", keskiarvot)


if __name__ == "__main__":
    main()
