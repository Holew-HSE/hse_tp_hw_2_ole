import unittest
from main import _max, read


class TestMax(unittest.TestCase):
    def test__min(self):
        self.assertEqual(5222, _max(read('test.txt')))


if __name__ == '__main__':
    unittest.main()
