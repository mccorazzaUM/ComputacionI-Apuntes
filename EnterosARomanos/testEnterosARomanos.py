import unittest

from enterosARomanos import entero_a_romano


class TestRomano(unittest.TestCase):

    def test_unidades_basicas(self):
        self.assertEqual(entero_a_romano(1), "I")
        self.assertEqual(entero_a_romano(5), "V")
        self.assertEqual(entero_a_romano(10), "X")

    def test_casos_con_resta(self):
        self.assertEqual(entero_a_romano(4), "IV")
        self.assertEqual(entero_a_romano(9), "IX")
        self.assertEqual(entero_a_romano(40), "XL")
        self.assertEqual(entero_a_romano(90), "XC")
        self.assertEqual(entero_a_romano(400), "CD")
        self.assertEqual(entero_a_romano(900), "CM")

    def test_numeros_compuestos(self):
        self.assertEqual(entero_a_romano(14), "XIV")
        self.assertEqual(entero_a_romano(37), "XXXVII")
        self.assertEqual(entero_a_romano(2024), "MMXXIV")
        self.assertEqual(entero_a_romano(3999), "MMMCMXCIX")