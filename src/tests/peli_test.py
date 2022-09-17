import unittest
from peli.peli import *

class TestPeli(unittest.TestCase):
    def setUp(self):
        pass

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