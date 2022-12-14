import unittest
from ratkoja.ratkoja import *
from peli.liiku import liiku_alas, liiku_ylos, liiku_vasen, liiku_oikea

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
        
        self.taulukko6 = [[0, 0, 0, 0],
                            [0, 0, 2, 0],
                            [0, 2, 0, 0],
                            [2, 0, 0, 0]]

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

        self.assertEqual(pisteet, 268551.0)

    def test_mahdollisuus_palauttaa_oikean_pistemaaran(self):
        pisteet = mahdollisuus(self.taulukko1, 1, 1.0, -
                               float('inf'), float('inf'))

        self.assertEqual(round(pisteet, 2), 578120.3)
    
    def test_testi(self):
        suunta, _ = tee_paatos(self.taulukko6)

        suunta_funktiot = {"vasen":liiku_vasen, "oikea":liiku_oikea, "ylos":liiku_ylos, "alas":liiku_alas}
        for i in suunta_funktiot:
            if suunta == i:
                uusi_taulukko = suunta_funktiot[i](self.taulukko6)

        uusi_taulukko2 = []
        for rivi in uusi_taulukko:
            uusi_taulukko2.append(rivi.copy())
        uusi_taulukko[3][3] = 2
        uusi_taulukko2[0][3] = 4

        suunta1, _ = tee_paatos(uusi_taulukko)

        suunta2, _ = tee_paatos(uusi_taulukko2)

        self.assertEqual(suunta1, "ylos")
        self.assertEqual(suunta2, "oikea")