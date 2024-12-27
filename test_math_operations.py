import unittest
from math_operations import add_numbers, subtract_numbers

class TestMathOperations(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(10, 5), 5)
        self.assertEqual(subtract_numbers(0, 7), -7)
        self.assertEqual(subtract_numbers(5, 5), 0)

if __name__ == '__main__':
    unittest.main()
