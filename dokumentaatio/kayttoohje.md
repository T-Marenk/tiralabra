# Käyttöohje

## Ohjelman asentaminen

### Riippuvaisuudet

Ohjelma on riippuvainen seuraavista paketeista

- Python >= 3.10

- Poetry

- Chrome

Poetryn asentaminen onnistuu _pipin_ avulla seuraavasti

```bash
pip install poetry
```

### Repositorion asentaminen

Kun olet saanut riippuvaisuudet koneellesi asennettua, kloonaa repositorio ja asenna loput ympäristö kohtaiset riippuvuudet poetrylla

1. 
```bash 
git clone https://github.com/T-Marenk/tiralabra
cd tiralabra
```

2. 
```bash
poetry install
```

## Ohjelman suorittaminen

Ohjelmassa on olemassa kaksi eri versiota. Yksi versio pyörittää alkuperäistä [2048 peliä](https://play2048.co/) netissä ja toinen pyörittää paikallista
kopiota pelistä komentorivillä

### Nettiversio

Ohjelman aloitukseksi syötä komentoriville komento

```bash
poetry run invoke start
```

Ohjelma kysyy aluksi, montako kertaa haluat suorittaa ratkojan. Anna vastauksena **positiivinen kokonaisluku**, jonka jälkeen ohjelma pyörittää ratkojan
halutun määrän kertoja

Ohjelman aikana tulostetaan komentoriville kunkin siirron kohdalla kyseiseen siirtoon kulunut aika.

Suoritusten jälkeen ohjelma palauttaa tiedot siitä, mikä oli jokaisen siirron päättämisessä suurin käytetty aika, pienin käytetty aika, keskiarvo päätöksiin
menneestä ajasta sekä mikä oli joka kerralla saavutettu suurin arvo

### Komentoriviversio

Ohjelman suoritukseksi komentoriviltä syötä komento

```bash
poetry run invoke ratkoja
```

Komentorivi versio suoritetaan yhden kerran. Joka siirron kohdalla näytetään siirron päättämiseen kulunut aika, samoin kuin nettiversiossa
