Tietojenkäsittelytieteen kandiohjelma (TKT)

Projekti tulee olemaan tehty pythonilla. En hallitse muita ohjelmointikieliä niin, että voisin tehdä niillä vertaisarviointeja. Dokumentaation sekä muun projektin kielenä tulee olemaan suomi.

Projektissa toteutan EXPECTIMINIMAX[1]ja[3] algoritmin, jonka avulla teen mahdollisimman tehokkaan 2048-pelin[2] ratkojan.

Valitsin EXPECTIMINIMAX algoritmin kyseiseen projektiin 2048-pelin satunnaisuuden takia. Koska joka vuorolla syntyy laudalle uusi numero satunnaiseen paikkaan, on hyödyllisempää käyttää EXPECTIMINIMAX algoritmia kuin perinteistä MINIMAX-algoritmia.[4]

Ohjelma tulee saamaan syötteenä aina nykyisen pelilaudan tilanteen, jota tarkastelemalla algoritmi tulee valitsemaan parhaan mahdollisen seuraavan siirron pelissä ja tekemään sen.

Tavoitteena on, että algoritmi tulee toimimaan ajassa O(n) ja tilavaativuus olisi myös O(n).

Lähteet:
[1] Wikipedia, Expectiminimax. 2020. URL:[https://en.wikipedia.org/wiki/Expectiminimax](https://en.wikipedia.org/wiki/Expectiminimax)

[2] Wikipedia, 2048 (video game). 2022. URL:[https://en.wikipedia.org/wiki/2048_(video_game)](https://en.wikipedia.org/wiki/2048_(video_game))

[3] M. Simic, Expectimax Search Algorithm. 2021. URL:[https://www.baeldung.com/cs/expectimax-search](https://www.baeldung.com/cs/expectimax-search)

[4] Y. Zhou, From AlhaGo Zero to 2048. 2019. URL:[https://www.cse.msu.edu/~zhaoxi35/DRL4KDD/2.pdf](https://www.cse.msu.edu/~zhaoxi35/DRL4KDD/2.pdf)
