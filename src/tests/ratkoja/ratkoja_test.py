import unittest
from ratkoja.ratkoja import *

class TestRatkoja(unittest.TestCase):
    def setUp(self):
        self.mahdollisuudet1 = {"vasen": True, "oikea": False, "ylos": False, "alas": False}
        self.mahdollisuudet2 = {"vasen": False, "oikea": True, "ylos": False, "alas": False}
        self.mahdollisuudet3 = {"vasen": False, "oikea": False, "ylos": True, "alas": False}
        self.mahdollisuudet4 = {"vasen": False, "oikea": False, "ylos": False, "alas": True}
        
        self.taulukko1 = [[2,4,0,0],[2,0,2,0],[0,0,0,0],[2,0,0,0]]

    def test_tee_paatos_tekee_oikean_paatoksen(self):
        suunta1 = tee_paatos(self.taulukko1, self.mahdollisuudet1)
        suunta2 = tee_paatos(self.taulukko1, self.mahdollisuudet2)
        suunta3 = tee_paatos(self.taulukko1, self.mahdollisuudet3)
        suunta4 = tee_paatos(self.taulukko1, self.mahdollisuudet4)

        self.assertEqual(suunta1, "vasen")
        self.assertEqual(suunta2, "oikea")
        self.assertEqual(suunta3, "ylos")
        self.assertEqual(suunta4, "alas")