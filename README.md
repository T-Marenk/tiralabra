# 2048-ratkoja

Tämä projekti on luotu Helsingin yliopiston kurssia *Aineopintojen harjoitustyö: Tietorakenteet ja algoritmit* varten. 

Projektin tarkoituksena on luoda mahdollisimman tehokas 2048-pelin ratkoja hyödyntämällä _Expectiminimax_-algoritmia.

## Dokumentaatio

![Määrittelydokumentti](./dokumentaatio/maarittelydokumentti.md)

![Testausdokumentti](./dokumentaatio/Testaus.md)

![Toteutusdokumentti](./dokumentaatio/toteutusdokumentti.md)

![Käyttöohje](./dokumentaatio/kayttoohje.md)

[Pydoc3 dokumentaatio](https://htmlpreview.github.io/?https://github.com/T-Marenk/tiralabra/blob/main/dokumentaatio/html/src/index.html)

### Viikkoraportit

![Viikkoraportti 1](./dokumentaatio/viikkoraportit/viikkoraportti1.md)

![Viikkoraportti 2](./dokumentaatio/viikkoraportit/viikkoraportti2.md)

![Viikkoraportti 3](./dokumentaatio/viikkoraportit/viikkoraportti3.md)

![Viikkoraportti 4](./dokumentaatio/viikkoraportit/viikkoraportti4.md)

![Viikkoraportti 5](./dokumentaatio/viikkoraportit/viikkoraportti5.md)

![Viikkoraportti 6](./dokumentaatio/viikkoraportit/viikkoraportti6.md)

## Ohjelman vaatimukset

Projekti käyttää python-versiota 3.10. Tämän lisäksi projektissa on hyödynnetty poetrya, joka tulee olla asennettuna tietokoneella

Ratkojaa pyörittäessä avataan peli Chrome selaimessa, joten tietokoneella tarvitsee olla Chrome asennettuna.

## Asennus

1. Kopioi projekti tietokoneellesi
```bash
git clone https://github.com/T-Marenk/tiralabra.git
```

2. Mene ladattuun kansioon
```bash
cd tiralabra
```

3. Asenna riippuvuudet poetrylla
```bash
poetry install
```

4. Käynnistä ohjelma tai ratkoja

Ratkojan käynnistys:
```bash
poetry run invoke ratkoja
```

Pelkän pelin käynnistys:
```bash
poetry run invoke start
```

Tarkemmat tiedot ohjelman suorittamiesta saat [käyttöohjeista](./dokumentaatio/kayttoohje.md)

## Testaaminen

### Testien suorittaminen

Suorita testit komennolla
```bash
poetry run invoke test
```

### Kattavuusraportti

1. Kerää tiedot kattavuus raporttia varten suorittamalla
```bash
poetry run invoke coverage
```

2. Luo raportti suorittamalla komento
```bash
poetry run invoke coverage-report
```
Raportti luodaan tiedostoon index.html kansioon htmlcov. Näet raportin avaamalla index.html-tiedoston.

### Pylint

Koodin laatua tarkastelua varten on käytössä pylint. Suorita pylint komennolla

```bash
poetry run invoke lint
```
