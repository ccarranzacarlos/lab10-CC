# https://github.com/ccarranzacarlos/lab10-CC.git
# Partner 1: Carlos Carranza Santos (both roles)

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 5), 5)
    
    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-2, 3), -5)
    ##########################
    
    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-2, 3), -6)
        self.assertEqual(mul(0, 5), 0)
    
    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 10), 5.0)
        self.assertEqual(div(4, 8), 2.0)
        self.assertAlmostEqual(div(3, 1), 0.3333333333333333)
    ##########################
    
    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    
    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(3, 9), 2.0)
    
    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 5)  # base cannot be 1
    ##########################
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -5)
    
    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5.0)
        self.assertEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(1, 1), 1.4142135623730951)
    
    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)
        self.assertEqual(square_root(9), 3.0)
        self.assertEqual(square_root(16), 4.0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
