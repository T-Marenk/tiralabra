"""Välikäännös, joka antaa ratkojan pelata 2048-peliä internetissä"""

import time
from collections import deque
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from ratkoja.ratkoja import tee_paatos

def yhdista():
    """Funktio, joka yhdistaa netti peliin
    Returns:
        selaimen ajurin
    """

    url = 'https://play2048.co/'
    driver = webdriver.Chrome('assets/chromedriver')
    driver.get(url)
    return driver

def hae_taulukko(driver):
    """Funktio, joka hakee nettipelistä nykyisen taulukon
    Args:
        driver: internet selain
    Returns:
        peliruudukon listana
    """

    matriisi = [[0 for i in range(4)] for j in range(4)]
    ruudut = driver.find_elements(By.CLASS_NAME, 'tile')

    for ruutu in ruudut:
        luokka = ruutu.get_attribute('class')
        sarake, rivi = luokka.split(
            'tile-position-')[1].split(' ')[0].split('-')
        sarake, rivi = int(sarake)-1, int(rivi)-1
        numero = int(luokka.split('tile tile-')[1].split(' ')[0])
        if numero > matriisi[rivi][sarake]:
            matriisi[rivi][sarake] = numero

    return matriisi


def main():
    """Pääfunktio, joka pyörittää nettiselainta
    Returns:
        Isoimmat ajat siirroissa, pienimmät ajat siirroissa, isoimman palikan,
        keskiarvon kuluneesta ajasta yhteen siirtoon
    """

    driver = yhdista()
    try:
        cookie_prompt = driver.find_element(By.ID, "ez-accept-all")
        cookie_prompt.click()
    except NoSuchElementException:
        pass

    body = driver.find_element(By.TAG_NAME, 'body')

    ajat = deque()
    komento = None

    while komento != "lopeta":
        taulukko = hae_taulukko(driver)
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

        try:
            jatka = driver.find_element(By.CLASS_NAME, "keep-playing-button")
            jatka.click()
        except NoSuchElementException:
            pass

        time.sleep(0.05)

    suurin_arvo = None
    for rivi in taulukko:
        suurin_rivi = max(rivi)
        if suurin_rivi > suurin_arvo:
            suurin_arvo = suurin_rivi
    suurin_palikka = max(taulukko)
    suurin = max(ajat)
    pienin = min(ajat)
    keskiarvo = sum(ajat)/len(ajat)

    driver.close()

    return suurin_palikka, suurin, pienin, keskiarvo
