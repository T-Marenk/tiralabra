import unittest
from peli.peli import *
from peli.liiku import mahdolliset_liikkeet


class TestPeli(unittest.TestCase):
    def setUp(self):
        self.taulukko1 = [[2, 4, 0, 0], [
            2, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
        self.taulukko2 = [[2, 4, 0, 0], [
            8, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0]]
        self.taulukko3 = [[2, 0, 0, 0], [
            8, 0, 0, 0], [4, 0, 0, 0], [2, 0, 4, 0]]
        self.taulukko4 = [[0, 0, 0, 2], [
            0, 0, 0, 0], [0, 0, 0, 4], [2, 4, 8, 4]]

    def test_uusi_peli_taulukko_luotu_oikein(self):
        taulukko = uusi_peli()

        self.assertEqual(len(taulukko), 4)
        self.assertEqual(len(taulukko[0]), 4)

        a = 0
        for i in taulukko:
            for j in i:
                if j != 0:
                    a += 1

        self.assertEqual(a, 2)

    def test_katsoo_oikein_voiko_liikkua_ylos(self):
        arvo1 = mahdolliset_liikkeet(self.taulukko1)
        arvo2 = mahdolliset_liikkeet(self.taulukko2)

        self.assertEqual(arvo1["ylos"], True)
        self.assertEqual(arvo2["ylos"], False)

    def test_katsoo_oikein_voiko_liikkua_alas(self):
        arvo1 = mahdolliset_liikkeet(self.taulukko1)
        arvo2 = mahdolliset_liikkeet(self.taulukko3)

        self.assertEqual(arvo1["alas"], True)
        self.assertEqual(arvo2["alas"], False)

    def test_katsoo_oikein_voiko_liikkua_vasen(self):
        arvo1 = mahdolliset_liikkeet(self.taulukko1)
        arvo2 = mahdolliset_liikkeet(self.taulukko2)

        self.assertEqual(arvo1["vasen"], True)
        self.assertEqual(arvo2["vasen"], False)

    def test_katsoo_oikein_voiko_liikkua_oikea(self):
        arvo1 = mahdolliset_liikkeet(self.taulukko1)
        arvo2 = mahdolliset_liikkeet(self.taulukko4)

        self.assertEqual(arvo1["oikea"], True)
        self.assertEqual(arvo2["oikea"], False)
