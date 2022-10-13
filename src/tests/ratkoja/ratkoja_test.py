import unittest
from ratkoja.ratkoja import *


class TestRatkoja(unittest.TestCase):
    def setUp(self):

        self.taulukko1 = [[2, 4, 0, 0], [
            2, 0, 2, 0],
            [0, 0, 0, 0],
            [2, 0, 0, 0]]
        self.taulukko2 = [[2048, 128, 64, 2],
                          [1024, 256, 4, 16],
                          [16, 128, 16, 4],
                          [0, 2, 4, 2]]
        self.taulukko3 = [[0, 2048, 128, 4],
                          [1024, 256, 8, 4],
                          [128, 64, 32, 2],
                          [16, 2, 4, 2]]

        self.taulukko4 = [[8, 2, 4, 0],
                        [4, 4, 2, 0],
                        [2, 0, 0, 0],
                        [0, 0, 0, 0]]

        self.taulukko5 = [[2048, 128, 64, 2],
                [1024, 256, 4, 16],
                [16, 128, 16, 4],
                [2, 4, 2, 8]]

    def test_tee_paatos_tekee_oikean_paatoksen(self):
        suunta1, _ = tee_paatos(self.taulukko1)
        suunta2, _ = tee_paatos(self.taulukko2)
        suunta3, _ = tee_paatos(self.taulukko3)
        suunta4, _ = tee_paatos(self.taulukko4)
        suunta5, _ = tee_paatos(self.taulukko5)

        self.assertEqual(suunta1, "ylos")
        self.assertEqual(suunta2, "vasen")
        self.assertEqual(suunta3, "vasen")
        self.assertEqual(suunta4, "vasen")
        self.assertEqual(suunta5, "lopeta")

    def test_kay_lapi_palauttaa_oikean_arvon(self):
        pisteet = kay_lapi(self.taulukko1)

        self.assertEqual(pisteet, 483844)

    def test_mahdollisuus_palauttaa_oikean_pistemaaran(self):
        pisteet = mahdollisuus(self.taulukko1, 1, 1.0, -
                               float('inf'), float('inf'))

        self.assertEqual(round(pisteet, 2), 805686.8)
