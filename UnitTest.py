import unittest
import math
class Calculator: 
    def add(self, a, b):
        return a+b
class CalculatorTest(unittest.TestCase):
    def test_add(self):
      calc = Calculator()
      self.assertEqual(10, calc.add(7, 3))
    
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
