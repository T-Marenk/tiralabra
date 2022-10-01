# Toteutusdokumentti

## Ohjelman yleisrakenne

![Ratkojan](src/ratkoja/ratkoja.py) toimintaan kuuluu kolme erillistä funktiota kutsumisfunktion lisäksi, jotka ovat maksimifunktio, mahdollisuusfunktio
sekä pisteytysfunktio.

Ratkojan kutsumisen jälkeen kutsutaan aluksi maksimi funktiota. Maksimifunktion tarkoituksena on valita nykyisen solmun mahdollisista siirroista
paras mahdollinen kutsumalla mahdollisuusfunktiota.

Mahdollisuusfunktio käy läpi kyseisellä ruudukolla mahdolliset vaihtoehdot siitä, millaiseksi peliruudukko voi muodostua, eli mihin uusi palikka voi syntyä.
Mahdollisille ruudukoille annetaan kullekin omat painotetut pisteensä laatan todennäköisyyden mukaan. Jokaisessa kohdassa katsotaan samalla sekä 2 laatan 
tilanne että 4-laatan tilanne. Mahdollisista pisteistä halutaan etsiä huonoin, sillä esittämällä maksimifunktiolle aina huonoin mahdollinen tilanne
saadaam valittua ideaalisin siirto.

Mahdollisuusfunktiossa näkyy myös alpha-beta karsinnan toiminta. Mikäli käydessä läpi mahdollisia pisteitä tuleville ruudukoille löydetään pisteet, jotka ovat
huonommat kuin jo löydetyt mahdolliset huonoimmat pisteet toisesta mahdollisesta siirrosta, lopetetaan funktion läpikäynti siihen, sillä tiedetään, että
se ei voi olla ideaalinen siirto verrattuna muuhun siirtoon.

Jos päästään halutulle syvyydelle algoritmin toimintaa varten, niin kutsutaan pisteytysfunktiota. Pisteytysfunktiossa on käytetty heuristiikkana painotettua
arvoa, jossa jokaisen laatan pisteet kerrotaan paikalle määritetyllä painoarvolla ja painotetut pisteeet laatoista lasketaan yhteen. Tämän lisäksi 
pisteytyksessä annetaan niin sanottuja bonuksia tyhjistä laatoista.

|||||
|:-:|:-:|:-:|:-:|
|7|6|5|4|
|6|5|4|3|
|5|4|3|2|
|4|3|2|1|


