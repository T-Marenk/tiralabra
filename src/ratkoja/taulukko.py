"""Ratkojaa varten luotu luokka, joka auttaa taulukoiden kanssa
"""


class Taulukko:
    """Luokka, jonka tehtävä on taulukon läpikäyminen
    """

    def kopioi(taulukko: list):
        """Kopioi nykyisen ruudukon kerran

        Args:
            taulukko: Peli ruudukko

        Returns:
            Kopion ruudukosta
        """

        taulukko_kopio = []
        for indeksi in range(4):
            rivi = taulukko[indeksi]
            taulukko_kopio.append(rivi.copy())
        return taulukko_kopio

    def tyhjat(taulukko: list):
        """Etsii nykyiseltä laudalta tyhjat paikat
        Args:
            taulukko: peliruudukko

        Returns:
            Listan, jossa on tyhjien paikkojen koordinaatit tupleina
        """

        tyhjat_paikat = []
        maara = 0
        for i in range(4):
            for j in range(4):
                arvo = taulukko[i][j]
                if arvo == 0:
                    tyhjat_paikat.append((i, j))
                    maara += 1
        return tyhjat_paikat, maara
