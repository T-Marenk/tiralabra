"""Kutsuu pelin netti version ratkojalle
"""

import os
from configparser import ConfigParser
from peli.netti_peli import main as run
from config import AIKA_TIEDOSTO_POLKU

def main():
    """Kutsuu pelin
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    config = ConfigParser()
    config.read("config.ini")
    URL = config.get("website", "url")
    CHROME_DRIVER_POLKU = config.get("driver", "path")
    hyv = False
    while not hyv:  
        kerrat = (input("Montako kertaa haluat suorittaa ratkojan?\n"))
        try:
            kerrat = int(kerrat)
        except Exception as e:
            print("Anna positiivinen kokonaisluku")
            continue
        if kerrat > 0:
            hyv = True
        else:
            print("Anna positiivinen kokonaisluku")
    print("Suoritusta aloitetaan...")
    suurimmat = []
    s_ajat = []
    p_ajat = []
    keskiarvot = []
    for i in range(kerrat):
        suurin_palikka, suurin, pienin, keskiarvo = run(i+1, CHROME_DRIVER_POLKU, URL)
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
