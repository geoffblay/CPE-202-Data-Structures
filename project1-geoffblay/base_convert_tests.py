import unittest

from base_convert import convert


class Tests(unittest.TestCase):
    def test_convert_base02_1(self):
        self.assertEqual(convert(107, 2), '1101011')

    def test_convert_base10_1(self):
        self.assertEqual(convert(107, 10), '107')

    def test_convert_base16_1(self):
        self.assertEqual(convert(107, 16), '6B')

    def test_convert_base20_1(self):
        self.assertEqual(convert(110, 20), '5A')

    def test_convert_base49_1(self):
        self.assertEqual(convert(110, 49), '2C')

    def test_convert_base30_1(self):
        self.assertEqual(convert(103, 30), '3D')

    def test_convert_base30_2(self):
        self.assertEqual(convert(104, 30), '3E')

    def test_convert_base30_3(self):
        self.assertEqual(convert(105, 30), '3F')


if __name__ == '__main__':
    unittest.main()
