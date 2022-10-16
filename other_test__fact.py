import unittest
import math


class TestFact(unittest.TestCase):
    def test__min(self):
        self.assertEqual(720, math.factorial(6))
        self.assertEqual(120, math.factorial(5))
        self.assertEqual(24, math.factorial(4))


if __name__ == '__main__':
    unittest.main()
