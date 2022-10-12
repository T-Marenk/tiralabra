# Testausdokumentti

Ohjelman testaus on toteutettu automatisoiduilla unittesteillä sekä ohjelman suorituskyky suoritetaan manuaalisesti laadituin testein

## Automatisoidut testit

### Pelin testaus

Pelin toimivuudesta vastaava `peli.py`-tiedosto testataan ![TestPeli](/src/tests/peli/peli_test.py)-luokalla. Pelin liikkumisesta vastaava `liiku.py`-tiedosto testataan ![TestPeliLiikkuminen](/src/tests/liikkuminen/liiku_test.py)-luokalla.

### Ratkojan testaaminen

Peli-ratkojasta vastaava `ratkoja.py`-tiedosto testataan ![TestRatkoja](/src/tests/ratkoja/ratkoja_test.py)-luokalla. 


### Testien ajaminen

Juurihakemistosta kutsumalla seuraavaa komentoa on mahdollista ajaa yksikkö testit

```bash
poetry run invoke test
```

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

Tämä saadaan tehtyä niin, että kun peliä ratkojaa kutsutaan kohteesta ![Netti-peli](/src/peli/netti_peli.py), otetaan ylös kulunut aika ja pelin päätyttyä tulokset tulostetaan komentoriville


### Suorituskyky testausten ajaminen

Kutsumalla projektin juurihakemistosta seuraavan komennon pystyy pyörittämään pelin internet versiota

```bash
poetry run invoke start
```

Jos haluat testata suorituskykyä komentorivi versiolla, on se mahdollista seuraavalla komennolla

```bash
poetry run invoke ratkoja
```

### Suurin saavutettu arvo

Alla on taulukoitu, että kun pelejä on suoritettu 2 kappaletta, niin kuinka suuren osan ajasta se on päässyt kyseiseen arvoon ja maksimisyvyys on 5

|Saavutettu arvo|512|1024|2048|4096|
|:-:|:-:|:-:|:-:|:-:|
|Kerrat|2|2|1|0|
|Prosenttina|100%|100%|50%|0%|

### Kulunut aika

Kun testejä on suoritettu 2 kappaletta, niin algoritmilla on mennyt maksimisyvyydellä 5

Vähiten aikaa vienyt siirto:

- $1.811*10^-5$ s

Eniten aikaa vienyt siirto:

- 0.5468 s

Keskiarvo joka siirtoon:

- 0.08301 s


