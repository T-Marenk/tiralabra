# Viikkoraportti 3

## Ohjelman edistyminen

Ratkojasta on tämän viikon aikana luotu ensimmäinen versio. Expectiminimax toimii kuten sen pitäisi ja katsoo tulevia mahdollisuuksia
tällä hetkellä 3 siirtoa eteenpäin. Toteutus ei kuitenkaan ole tällä hetkellä täydellinen, sillä parin suorituskerran aikana se ei onnistunut pääsemään
1024 laattaa pidemmälle. Tämän lisäksi ohjelman muissa osissa ollaan tehty pieniä korjauksia, kuten esimerkiksi muuttujien nimien parantamista.
Testausta ollaan laajennettu niin, että ratkoja on tällä hetkellä testattu kokonaan, vaikkakin testaukseen tulisi lisätä enemmän erilaisia mahdollisuuksia,
jotta voidaan olla varmoja, että se toimii hyvin.

Projektissa on tämän lisäksi otettu käyttöön pylint ja aloitettu koodin parantaminen sen ohjeiden mukaisesti. Myös dokumentaatiota ollaan laajennettu
huomattavasti.

## Opitut asiat

Expectiminimaxin toimivuus tarkemmin, eli miten chance-kohdat toimivat ja että mitä tarkalleen algoritmi haluaa tietää. Perehdyin myös tarkemmin
valitsemaani menetelmään pisteyttää eri pelitilanteet, vaikkakin tähän saatan hyvinkin tehdä jatkossa muutoksia. Lisäksi opin, kuinka nopeasti eri
vaihtoehdot lisääntyvät tällaisessa projektissa mahdollisia siirtoja katsoessa.

## Käytetty aika

Tällä viikolla aikaa projektiin käytin noin 12 tuntia.

## Ongelma tilanteet

Ensimmäisissä versioissa ongelmaksi osui algoritmin epätehokkuus. Tarkemmin ottaen, yritin katsoa 4 siirtoa eteenpäin, mutta mahdolliset ruudukot olivat 
monta miljoona, jonka takia algoritmin päätöksen teko kesti yli 20 sekuntia jokaista siirtoa kohden. Tämän takia algoritmi katsoo vain 3 siirtoa tulevaisuuten
tällä hetkellä.

## Seuraavan viikon tavoite

Algoritmin tehostaminen, esimerkiksi löytämällä tapa valita katsottavien siirtojen määrä pelitilanteesta riippuen.
