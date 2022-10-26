"""Kutsuu pelin netti version ratkojalle
"""

import os
import time
from configparser import ConfigParser
from peli.netti_peli import main as run
from config import AIKA_TIEDOSTO_POLKU


def main():
    """Kutsuu pelin
    """

    os.system('cls' if os.name == 'nt' else 'clear')
    config = ConfigParser()
    config.read("config.ini")
    url = config.get("website", "url")
    chrome_driver_polku = config.get("driver", "path")
    hyv = False
    while not hyv:
        kerrat = (input("Montako kertaa haluat suorittaa ratkojan?\n"))
        try:
            kerrat = int(kerrat)
        except ValueError:
            print("Anna positiivinen kokonaisluku")
            continue
        if kerrat > 0:
            hyv = True
        else:
            print("Anna positiivinen kokonaisluku")
    print("Suoritusta aloitetaan...")
    for i in range(kerrat):
        suurin_palikka, suurin, pienin, keskiarvo = run(
            i+1, chrome_driver_polku, url)
        with open(AIKA_TIEDOSTO_POLKU, "a", encoding="utf-8") as tie:
            tie.write(
                f"Suurin laatta: {suurin_palikka}\nSuurin aika: {suurin} s\n"
                "Pienin aika: {pienin} s\nKeskiarvot ajoista: {keskiarvo}\n\n")
        print("Suurin:", suurin_palikka)
        print("Suurin aika", suurin)
        print("Pienin aika", pienin)
        print("Keskiarvo ajoista", keskiarvo)
        time.sleep(5)


if __name__ == "__main__":
    main()
