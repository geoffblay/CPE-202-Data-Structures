import unittest

from bears import bears


class Tests(unittest.TestCase):
    def test_bears_40(self):
        self.assertFalse(bears(40))

    def test_bears_42(self):
        self.assertTrue(bears(42))

    def test_bears_250(self):
        self.assertTrue(bears(250))

    def test_bears_91(self):
        self.assertFalse(bears(91))

    def test_bears_90(self):
        self.assertFalse(bears(90))

    def test_bears_46(self):
        self.assertFalse(bears(46))

    def test_bears_51(self):
        self.assertFalse(bears(51))

    def test_bears_95(self):
        self.assertFalse(bears(95))

    def test_bears_45(self):
        self.assertFalse(bears(45))

    def test_bears_84(self):
        self.assertTrue(bears(84))


if __name__ == '__main__':
    unittest.main()
