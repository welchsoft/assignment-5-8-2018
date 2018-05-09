import unittest
from calculator import Calculator
class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(5,self.calc.add(2,3))

    def test_subtraction(self):
        self.assertEqual(5,self.calc.subtraction(7,2))

    def test_multiply(self):
        self.assertEqual(10,self.calc.multiply(5,2))

    def test_divide(self):
        self.assertEqual(10,self.calc.divide(20,2))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
