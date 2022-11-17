import unittest
from Calculadora import suma, resta, multiplicacion, division

class TestNnofraccionados(unittest.TestCase):

    def test_suma(self):
        self.assertAlmostEqual(suma(1,2), 3)

    def test_resta(self):
        self.assertAlmostEqual(resta(2,1), 1)
    
    def test_multiplicacion(self):
        self.assertAlmostEqual(multiplicacion(4,4), 16)

    def test_division(self):
        self.assertAlmostEqual(division(5,5), 1)
        
    

    