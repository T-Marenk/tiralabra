# Testausdokumentti

Ohjelman testaus on toteutettu automatisoiduilla unittesteillä sekä ohjelman suorituskyky suoritetaan manuaalisesti laadituin testein

## Automatisoidut testit

### Pelin testaus

Pelin toimivuudesta vastaava `peli.py`-tiedosto testataan ![TestPeli](/src/tests/peli/peli_test.py)-luokalla. Pelin liikkumisesta vastaava `liiku.py`-tiedosto testataan ![TestPeliLiikkuminen](/src/tests/liikkuminen/liiku_test.py)-luokalla.

### Ratkojan testaaminen

Peli-ratkojasta vastaava `ratkoja.py`-tiedosto testataan ![TestRatkoja](/src/tests/ratkoja/ratkoja_test.py)-luokalla. 

### Testikattavuus

Tämän hetkinen testikattavuus on 71%

![](./kuvat/coverage-report_4.png)

## Suorituskyvyn testaaminen

### Toteutus

Suorituskyvyn testaamista varten ratkoja suoritetaan alusta loppuun ja joka testauskerralla otetaan ylös seuraavat asiat:

- Keskiarvo siirtojen päättämisessä kestäneestä ajasta

- Suurin siirron päättämiseen mennyt aika

- Pienin siirron päättämiseen mennyt aika

- Suurin arvo taulukossa pelin loputtua
