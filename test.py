import unittest
from calculator import divide, multiply, power


class CalculatorTests(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(6, 4), 24)

    def test_divide(self):
        self.assertEqual(divide(12, 3), 4)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(-2, 3), -8)


if __name__ == "__main__":
    unittest.main()