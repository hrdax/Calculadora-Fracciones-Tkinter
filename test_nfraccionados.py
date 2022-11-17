import unittest
from ClassFraccion import *
from Calculadora import restaFraccion, sumaFraccion, multiplicacionFraccion, divisionFraccion

class TestFraccion(unittest.TestCase):
    
    def test_suma(self):
        self.assertAlmostEqual(sumaFraccion(1,2), 3)

    def test_resta(self):
        self.assertAlmostEqual(restaFraccion(5,5,5,5), 1/)
    
    def test_multiplicacionFraccion(self):
        self.assertAlmostEqual(multiplicacionFraccion(1,2,3,4), 3/8)
    
    def test_divisionFraccion(self):
        self.assertAlmostEqual(divisionFraccion(1,2,3,4), 2/3)