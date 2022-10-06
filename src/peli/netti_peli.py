"""Välikäännös, joka antaa ratkojan pelata 2048-peliä internetissä"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time, random
from ratkoja.ratkoja import tee_paatos

def getGrid(driver):
        matriisi = [[0 for i in range(4)] for j in range(4)]
        ruudut = driver.find_elements(By.CLASS_NAME, 'tile')

        for ruutu in ruudut:
            luokka = ruutu.get_attribute('class')
            sarake, rivi = luokka.split('tile-position-')[1].split(' ')[0].split('-')
            sarake, rivi = int(sarake)-1, int(rivi)-1
            numero = int(luokka.split('tile tile-')[1].split(' ')[0])
            if numero > matriisi[rivi][sarake]:
                matriisi[rivi][sarake] = numero

        return matriisi

def main():
    url = 'https://gabrielecirulli.github.io/2048/'
    driver = webdriver.Chrome('assets/chromedriver')
    driver.get(url)

    body = driver.find_element(By.TAG_NAME, 'body')    

    ajat = []
    komento = None

    while komento != "lopeta":
        taulukko = getGrid(driver)
        komento, aika = tee_paatos(taulukko)
        ajat.append(aika)
        if komento == "vasen":
            body.send_keys(Keys.ARROW_LEFT)
        elif komento == "oikea":
            body.send_keys(Keys.ARROW_RIGHT)
        elif komento == "ylos":
            body.send_keys(Keys.ARROW_UP)
        elif komento == "alas":
            body.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.1)

    suurin_palikka = max(taulukko)
    suurin = max(ajat)
    pienin = min(ajat)
    keskiarvo = sum(ajat)/len(ajat)
    print("Suurin pala", suurin_palikka)
    print("Suurin:", suurin)
    print("Pienin:", pienin)
    print("Keskiarvo", keskiarvo)

    driver.exit()