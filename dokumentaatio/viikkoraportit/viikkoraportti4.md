# Viikkoraportti 4

## Ohjelman edistyminen
Ratkoja on tämän viikon aikana saatu tehtyä loppuun. Se toimii hyvin ja katsoo mahdollisia siirtoja 3-6 kappaletta. Koska ohjelman toteutus olisi muuten
erittäin hidasta, käytin viikosta suurimman osan ajasta selvittäessä, miten _expectiminimaxiin_ saa yhdistettyä _Alpha-Beta-jaon_. Selvitettyäni tätä asiaa
sain lopulta lisättyä sen toimivana versiona ratkojaani. 

_Expectiminimaxin_ tehostamiseksi korjasin myös ratkojan heuristiikan, joka kertoo painotetusti peliruudukon ja antaa lisäpisteitä tyhjistä ruuduista

Tämän lisäksi koodista ollaan tehty luettavampaa jakamalla se erillisiin funktioihin, kuten _expectiminimaxilla_ on melkein pakkokin.

Muutokset ovat toimineet, sillä aivan muutamien ajamisten aikana ratkoja onnistui aina pääsemään 2048:iin sekä muutaman kerran jopa 4096:een.

Isojen koodimuutoksien takia tuli testejä korjailla hyvä määrä.

## Mitä opin

_Alpha-beta-jaon_ toiminta _expectiminimax_-algoritmissä. Erityisen hyödyllisenä lähteenä alkuperäisten lähteideni lisäksi toimi tämä [Nagyn ja Melkon paperi](https://www.researchgate.net/publication/220123091_Optimal_strategy_in_games_with_chance_nodes)
satunnaispelien optimoinnista.

Lisäksi opin tällä viikolla kunnolla, miten eri heuristiikat toimivat pelissä 2048 ja mitä niiden vahvuudet ovat. Näitä voisi yhdistää yhteen ratkojaan, jota en kuitenkaan itse tehnyt.

## Käytetty aika

Tällä viikolla käytin projektiin 16 tuntia.

## Ongelma tilanteet

_Alpha-beta-jaon_ toiminta tuli isona ongelmana, sillä pelin todennäköisyys teki perinteisen jaon implementoinnista hankalaa

## Ensi viikon suunnitelma

Kattavan ratkojan suorituskyvyn testauksen tekeminen sekä testien loppuun kirjoittaminen. Lisäksi mahdollisesti tehdä pelistä mielenkiintoisempaa seurata 
näyttämällä terminaalissa aina päivitetty ruudukko, eikä tulostamalla ruudukkoja peräkkäin. Tämä kuitenkin vain jos on aikaa.
