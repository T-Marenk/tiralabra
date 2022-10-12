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

## Saavutettu aikavaativuus

Loppulliseksi aikavaativuudeksi algortimille tuli

$O(b^n)$

Missä _b_ on kaikki mahdolliset haarat, jotka algortimi voi katsoa ja _n_ on syyvyys, jolle algortimi meni

Alpha-beta jaon takia algortimi harvoin käy läpi kaikkia mahdollisia haaroja, mutta se on edelleen mahdollista

Syvyys algoritmille on 3-5, riippuen tyhjien paikkojen määrästä

## Saavutettu tilavaativuus

Lopullinen tilavaativuus algoritmilla on

$O(b*n)$

Missä _b_ on kaikki mahdolliset haarat, jotka algortimi voi katsoa ja _n_ on syyvyys, jolle algortimi meni

## Puutteet 

Algortimin isoimpia ongelmia tällä hetkellä on nopeus, jolla se toimii. Jos olisi mahdollista lisätä katsottavan syvyyden määrä ilman, että kulunut aika
yhden siirron katsomiselle nousisi älyttömästi, niin se olisi huomattavasti tehokkaampi

Yksi helppo tapa lisätä algoritmia olisi luoda taulukko, jossa pidetään kirjaa siitä, mitkä nykyisen taulukon pisteet ovat, jos se on jo nähty. Toinen tapa
olisi myös luoda taulukko siiroille, eli jokaista riviä ei tarvitsisi manuaalisesti siirtä vaan se voitaisiin ajassa $O(1)$ katsoa taulukosta ja korvata vanha taulukko uudella.

## Lähteet

Projektin tekemistä varten olleen hyödynnetty seuraavia lähteitä

Erityisesti lähteistä [4], [5] ja [7] on ollut hyötyä. Näiden avulla olen soveltanut nykyinen Expectiminimax algoritmin, joka on oikeastaan MiniGminimax algoritmi, johon sain yhdistettyä alpha-beta-karsinnan. 

[1] Wikipedia, Expectiminimax. 2020. URL:https://en.wikipedia.org/wiki/Expectiminimax

[2] Wikipedia, 2048 (video game). 2022. URL:https://en.wikipedia.org/wiki/2048_(video_game)

[3] M. Simic, Expectimax Search Algorithm. 2021. URL:https://www.baeldung.com/cs/expectimax-search

[4] Y. Zhou, From AlhaGo Zero to 2048. 2019. URL:https://www.cse.msu.edu/~zhaoxi35/DRL4KDD/2.pdf

[5] E. Melkó, B. Nagy. Optimal strategy in games with chance nodes. 2007. URL:https://www.researchgate.net/publication/220123091_Optimal_strategy_in_games_with_chance_nodes

[6] StackOverflow, What is the optimal algorithm for the game 2048?. 2014. URL:https://stackoverflow.com/questions/22342854/what-is-the-optimal-algorithm-for-the-game-2048 (Ensimmäinen vastaus)

[7] Wikipedia, Alpha-beta pruning. 2022. URL:https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

