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

        t = []
        for i in taulukko:
            t.append(i.copy())
        return t

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
