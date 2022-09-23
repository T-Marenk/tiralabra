import unittest
from ratkoja.ratkoja import *


class TestRatkoja(unittest.TestCase):
    def setUp(self):
        self.mahdollisuudet1 = {"vasen": True,
                                "oikea": False, "ylos": False, "alas": False}
        self.mahdollisuudet2 = {"vasen": False,
                                "oikea": True, "ylos": False, "alas": False}
        self.mahdollisuudet3 = {"vasen": False,
                                "oikea": False, "ylos": True, "alas": False}
        self.mahdollisuudet4 = {"vasen": False,
                                "oikea": False, "ylos": False, "alas": True}
        self.mahdollisuudet5 = {"vasen": False,
                                "oikea": False, "ylos": False, "alas": False}

        self.taulukko1 = [[2, 4, 0, 0], [
            2, 0, 2, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
        self.taulukko2 = [[0, 0, 0, 0], [
            0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

    def test_tee_paatos_tekee_oikean_paatoksen(self):
        suunta1 = tee_paatos(self.taulukko1, self.mahdollisuudet1)
        suunta2 = tee_paatos(self.taulukko1, self.mahdollisuudet2)
        suunta3 = tee_paatos(self.taulukko1, self.mahdollisuudet3)
        suunta4 = tee_paatos(self.taulukko1, self.mahdollisuudet4)
        suunta5 = tee_paatos(self.taulukko2, self.mahdollisuudet5)

        self.assertEqual(suunta1, "vasen")
        self.assertEqual(suunta2, "oikea")
        self.assertEqual(suunta3, "ylos")
        self.assertEqual(suunta4, "alas")
        self.assertEqual(suunta5, "lopeta")

    def test_kay_lapi_palauttaa_oikean_arvon(self):
        pisteet = kay_lapi(self.taulukko1)

        self.assertEqual(pisteet, 16)

    def test_arvo_palauttaa_oikean_pistemaaran(self):
        pisteet = arvo(self.taulukko1, 1)

        self.assertEqual(round(pisteet, 2), 9.25)
