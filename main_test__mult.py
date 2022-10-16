import unittest
from main import _mult, read


class TestMult(unittest.TestCase):
    def test__min(self):
        self.assertEqual(26409634830953215495851768991580160, _mult(read('test.txt')))


if __name__ == '__main__':
    unittest.main()
