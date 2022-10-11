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

    def test_tee_paatos_tekee_oikean_paatoksen(self):
        suunta1 = tee_paatos(self.taulukko1)
        suunta2 = tee_paatos(self.taulukko2)
        suunta3 = tee_paatos(self.taulukko3)

        self.assertEqual(suunta1, "ylos")
        self.assertEqual(suunta2, "alas")
        self.assertEqual(suunta3, "vasen")

    def test_kay_lapi_palauttaa_oikean_arvon(self):
        pisteet = kay_lapi(self.taulukko1)

        self.assertEqual(pisteet, 242)

    def test_mahdollisuus_palauttaa_oikean_pistemaaran(self):
        pisteet = mahdollisuus(self.taulukko1, 1, 1.0, -
                               float('inf'), float('inf'))

        self.assertEqual(round(pisteet, 2), 291.72)
