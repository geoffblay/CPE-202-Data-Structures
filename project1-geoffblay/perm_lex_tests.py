import unittest

from perm_lex import perm_gen_lex


class Tests(unittest.TestCase):
    def test_perm_gen_lex_empty(self):
        self.assertEqual(perm_gen_lex(''), [''])

    def test_perm_gen_length_1(self):
        self.assertEqual(perm_gen_lex('a'), ['a'])

    def test_perm_gen_length_2(self):
        self.assertEqual(perm_gen_lex('ab'), ['ab', 'ba'])

    def test_perm_gen_length_3(self):
        self.assertEqual(perm_gen_lex('abc'), ['abc', 'acb', 'bac', 'bca',
                                               'cab', 'cba'])

    def test_perm_gen_length_4(self):
        self.assertEqual(perm_gen_lex('abcd'), ['abcd', 'abdc', 'acbd', 'acdb',
                                                'adbc', 'adcb', 'bacd', 'badc',
                                                'bcad', 'bcda', 'bdac', 'bdca',
                                                'cabd', 'cadb', 'cbad', 'cbda',
                                                'cdab', 'cdba', 'dabc', 'dacb',
                                                'dbac', 'dbca', 'dcab',
                                                'dcba'])


if __name__ == '__main__':
    unittest.main()
