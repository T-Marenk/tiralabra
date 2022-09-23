class Taulukko:
    """Luokka, jonka tehtävä on taulukon läpikäyminen
    """

    def listat_kopioi(taulukko: list):
        """Kopioi nykyisen ruudukon

        Args:
            taulukko: Peli ruudukko

        Returns:
            Ruudukon kopiot
        """

        t1 = []
        t2 = []
        t3 = []
        t4 = []
        for i in taulukko:
            t1.append(i.copy())
            t2.append(i.copy())
            t3.append(i.copy())
            t4.append(i.copy())
        return t1,t2,t3,t4

    def tyhjat(self, taulukko: list):
        """Etsii nykyiseltä laudalta tyhjat paikat
        Args:
            taulukko: peliruudukko
            
        Returns:
            Listan, jossa on tyhjien paikkojen koordinaatit tupleina
        """

        tyhjat_paikat = []
        for i in range(4):
            for j in range(4):
                a = taulukko[i][j]
                if a == 0:
                    tyhjat_paikat.append((i,j))
        return tyhjat_paikat
