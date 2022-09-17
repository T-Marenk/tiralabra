import unittest
from peli.liiku import liiku_vasen, liiku_oikea, liiku_alas, liiku_ylos

class TestPeliLiikkuminen(unittest.TestCase):
    def setUp(self):
        self.taulukko1 = [[2,4,0,0],[2,0,2,0],[0,0,0,0],[2,0,0,0]]

    def test_liikkuu_oikein_vasen(self):
        taulukko = liiku_vasen(self.taulukko1)

        self.assertEqual(taulukko, [[2,4,0,0],[4,0,0,0],[0,0,0,0],[2,0,0,0]])

    def test_liikkuu_oikein_oikea(self):
        taulukko = liiku_oikea(self.taulukko1)

        self.assertEqual(taulukko, [[0,0,2,4],[0,0,0,4],[0,0,0,0],[0,0,0,2]])

    def test_liikkuu_oikein_ylos(self):
        taulukko = liiku_ylos(self.taulukko1)

        self.assertEqual(taulukko, [[4,4,2,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]])

    def test_liikkuu_oikein_alas(self):
        taulukko = liiku_alas(self.taulukko1)

        self.assertEqual(taulukko, [[0,0,0,0],[0,0,0,0],[2,0,0,0],[4,4,2,0]])