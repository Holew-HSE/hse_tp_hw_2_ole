import unittest
from main import _sum, read


class TestSum(unittest.TestCase):
    def test__min(self):
        self.assertEqual(11968, _sum(read('test.txt')))


if __name__ == '__main__':
    unittest.main()
