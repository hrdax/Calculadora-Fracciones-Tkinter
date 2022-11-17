import unittest
from ClassFraccion import *
from Calculadora import restaFraccion, sumaFraccion, multiplicacionFraccion, divisionFraccion

class TestFraccion(unittest.TestCase):
    
    def test_suma(self):
        self.assertAlmostEqual(sumaFraccion(3,5,4,4), 3)

    def test_resta(self):
        self.assertAlmostEqual(restaFraccion(5,5,5,5), [25,25])
    
    def test_multiplicacionFraccion(self):
        self.assertAlmostEqual(multiplicacionFraccion(5,5,5,5), [25,25])
    
    def test_divisionFraccion(self):
        self.assertAlmostEqual(divisionFraccion(5,5,5,5), (25,25))