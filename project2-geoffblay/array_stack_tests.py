import unittest

from array_stack import *


class Tests(unittest.TestCase):
    def test_empty_stack_01(self):
        self.assertEqual(empty_stack(), ArrayStack())

    def test_push_01(self):
        s = ArrayStack(2)
        push(s, 1)
        push(s, 2)
        self.assertEqual(s.items, [1, 2])

    def test_push_02(self):
        s = ArrayStack(2)
        push(s, 1)
        push(s, 2)
        push(s, 3)
        self.assertEqual(s.items, [1, 2, 3, None])

    def test_pop_01(self):
        s = ArrayStack(2)
        push(s, 1)
        push(s, 2)
        self.assertEqual(pop(s), 2)
        self.assertEqual(s.items, [1, None])

    def test_pop_02(self):
        s = empty_stack()
        with self.assertRaises(IndexError):
            pop(s)

    def test_pop_03(self):
        s = ArrayStack(2)
        push(s, 1)
        push(s, 2)
        push(s, 3)
        push(s, 4)
        self.assertEqual(pop(s), 4)
        self.assertEqual(s.items, [1, 2, 3, None])

    def test_peek_01(self):
        s = empty_stack()
        push(s, 1)
        push(s, 2)
        push(s, 3)
        self.assertEqual(peek(s), 3)

    def test_peek_02(self):
        s = empty_stack()
        with self.assertRaises(IndexError):
            peek(s)

    def test_is_empty_01(self):
        s = empty_stack()
        self.assertTrue(is_empty(s))

    def test_is_empty_02(self):
        s = ArrayStack(2)
        push(s, 1)
        self.assertFalse(is_empty(s))

    def test_size_01(self):
        s = empty_stack()
        push(s, 1)
        push(s, 2)
        self.assertEqual(size(s), 2)

    def test_size_02(self):
        s = ArrayStack(5)
        push(s, 2)
        push(s, 3)
        push(s, 4)
        pop(s)
        self.assertEqual(size(s), 2)
