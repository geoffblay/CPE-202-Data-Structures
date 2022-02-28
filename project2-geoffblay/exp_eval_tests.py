import unittest

from exp_eval import postfix_eval, infix_to_postfix


class Tests(unittest.TestCase):
    def test_postfix_eval_01(self):
        self.assertAlmostEqual(postfix_eval('1 2 +'), 3)

    def test_postfix_eval_02(self):
        self.assertAlmostEqual(postfix_eval('4 5 7 2 + - *'), -16)

    def test_postfix_eval_03(self):
        with self.assertRaises(ValueError):
            postfix_eval('')

    def test_postfix_eval_04(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 a +')

    def test_postfix_eval_05(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 +')

    def test_postfix_eval_06(self):
        with self.assertRaises(ValueError):
            postfix_eval('2 3 4 +')

    def test_postfix_eval_07(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval('2 0 /')

    def test_postfix_eval_08(self):
        with self.assertRaises(ZeroDivisionError):
            postfix_eval('2 0 //')

    def test_postfix_eval_09(self):
        self.assertAlmostEqual(postfix_eval('4 5 2 // /'), 2)

    def test_postfix_eval_10(self):
        self.assertAlmostEqual(postfix_eval('2 2 **'), 4)

    def test_infix_to_postfix_01(self):
        self.assertEqual(infix_to_postfix('1 + 2'), '1 2 +')

    def test_infix_to_postfix_02(self):
        self.assertEqual(infix_to_postfix('3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3'),
                         '3 4 2 * 1 5 - 2 3 ** ** / +')

    def test_infix_to_postfix_03(self):
        self.assertEqual(infix_to_postfix('2 ** 2 + 2 ** 2'),
                         '2 2 ** 2 2 ** +')

    def test_infix_to_postfix_04(self):
        self.assertEqual(infix_to_postfix('2 + 2 + 2 + 2'), '2 2 + 2 + 2 +')

    def test_infix_to_postfix_05(self):
        self.assertEqual(infix_to_postfix('( 5 + 7 ) * ( 6 - 2 )'),
                         '5 7 + 6 2 - *')

    def test_infix_to_postfix_06(self):
        self.assertEqual(infix_to_postfix('12'), '12')

    def test_infix_to_postfix_07(self):
        self.assertEqual(infix_to_postfix('12.0'), '12.0')


if __name__ == '__main__':
    unittest.main()
