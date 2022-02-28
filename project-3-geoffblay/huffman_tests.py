import unittest
import subprocess

# NOTE: Do not import anything else from huffman.  If you do, your tests
# will crash when I test them.  You shouldn't need to test your helper
# functions directly, just via testing the required functions.
from huffman import (
    HuffmanNode, count_frequencies, build_huffman_tree, create_codes,
    create_header, huffman_encode, parse_header, huffman_decode)


class TestList(unittest.TestCase):
    def test_count_frequencies_01(self):
        frequencies = count_frequencies("text_files/file2.txt")
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_node_lt_01(self):
        node1 = HuffmanNode(97, 10)
        node2 = HuffmanNode(65, 20)

        self.assertLess(node1, node2)
        self.assertGreater(node2, node1)

    def test_build_huffman_tree_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        huffman_tree = build_huffman_tree(frequencies)

        # NOTE: This also requires a working __eq__ for your HuffmanNode
        self.assertEqual(
            huffman_tree,
            HuffmanNode(97, 15, HuffmanNode(97, 5), HuffmanNode(98, 10))
        )

    def test_build_huffman_tree_02(self):
        frequencies = [0] * 256
        frequencies[97] = 4
        frequencies[98] = 3
        frequencies[99] = 2
        frequencies[100] = 1
        frequencies[32] = 3

        huffman_tree = build_huffman_tree(frequencies)

        # print(huffman_tree.char)
        # print(huffman_tree.frequency)
        # print(huffman_tree.left.char)
        # print(huffman_tree.left.frequency)
        # # print(huffman_tree.left.left.char)
        #
        # print(huffman_tree.right.char)
        # print(huffman_tree.right.frequency)
        # print(huffman_tree.right.right.char)

        self.assertEqual(
            huffman_tree,
            HuffmanNode(32, 13,
                        HuffmanNode(32, 6,
                                    HuffmanNode(32, 3),
                                    HuffmanNode(98, 3)),
                        HuffmanNode(97, 7,
                                    HuffmanNode(99, 3,
                                                HuffmanNode(100, 1),
                                                HuffmanNode(99, 2)),
                                    HuffmanNode(97, 4)))
        )

    def test_create_codes_01(self):
        huffman_tree = HuffmanNode(
            97, 15,
            HuffmanNode(97, 5),
            HuffmanNode(98, 10)
        )

        codes = create_codes(huffman_tree)
        self.assertEqual(codes[ord('a')], '0')
        self.assertEqual(codes[ord('b')], '1')

    def test_create_codes_02(self):
        huffman_tree = HuffmanNode(32, 13,
                                   HuffmanNode(32, 6,
                                               HuffmanNode(32, 3),
                                               HuffmanNode(98, 3)),
                                   HuffmanNode(97, 7,
                                               HuffmanNode(99, 3,
                                                           HuffmanNode(100, 1),
                                                           HuffmanNode(99, 2)),
                                               HuffmanNode(97, 4)))

        codes = create_codes(huffman_tree)
        self.assertEqual(codes[ord(' ')], '00')
        self.assertEqual(codes[ord('d')], '100')
        self.assertEqual(codes[ord('a')], '11')

    def test_create_header_01(self):
        frequencies = [0] * 256
        frequencies[97] = 5
        frequencies[98] = 10

        self.assertEqual(create_header(frequencies), "97 5 98 10")

    def test_create_header_02(self):
        header = create_header(
            count_frequencies('text_files/war_and_peace.txt'))
        self.assertEqual(header, '10 98306 32 590193 33 3409 34 17945 36 5 '
                                 '37 4 38 100 39 7848 40 643 41 633 42 369 '
                                 '44 39896 45 14602 46 31102 47 150 48 292 '
                                 '49 1368 50 457 51 388 52 377 53 348 54 '
                                 '2711 55 250 56 419 57 233 58 989 59 1263 '
                                 '61 2 63 3136 65 7720 66 4062 67 2300 68 '
                                 '2533 69 3576 70 2125 71 1375 72 4451 73 '
                                 '7856 74 347 75 1582 76 923 77 3477 78 4720 '
                                 '79 2632 80 6686 81 38 82 3535 83 3314 84 '
                                 '7179 85 404 86 1127 87 3380 88 386 89 1361 '
                                 '90 115 91 7 92 15 93 9 94 178 95 1 97 '
                                 '198387 98 31049 99 59832 100 118577 101 '
                                 '313235 102 53959 103 50080 104 163581 105 '
                                 '167366 106 2230 107 19347 108 96372 109 '
                                 '58463 110 181252 111 189601 112 39159 113 '
                                 '2306 114 146036 115 161095 116 220129 117 '
                                 '64879 118 26199 119 56403 120 3734 121 '
                                 '45040 122 2332 123 3 124 6 125 2 126 4')

    def test_huffman_encode_01(self):
        huffman_encode("text_files/file1.txt", "text_files/file1_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/file1_out.txt',
             'text_files/file1_soln.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_encode_02(self):
        huffman_encode("text_files/test1.txt", "text_files/test1_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/test1_out.txt',
             'text_files/test1_solu.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_huffman_encode_03(self):
        huffman_encode("text_files/test_empty.txt",
                       "text_files/test_empty_out.txt")

        result = subprocess.run(
            ['diff',
             '--strip-trailing-cr',
             'text_files/test_empty_out.txt',
             'text_files/test_empty_solu.txt'],
            check=False,
            text=True,
            capture_output=True,
        )

        self.assertEqual(result.returncode, 0, result.stdout)

    def test_parse_header_01(self):
        header = "97 2 98 4 99 8 100 16 102 2\n"

        frequencies = parse_header(header)
        expected = [0, 2, 4, 8, 16, 0, 2, 0]

        self.assertEqual(frequencies[96:104], expected)

    def test_huffman_decode_01(self):
        huffman_decode(
            "text_files/file1_soln.txt", "text_files/file1_decoded.txt")

        with open("text_files/file1_decoded.txt") as student_out, \
                open("text_files/file1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_02(self):
        huffman_decode(
            "text_files/part_b/b_test1_out.txt",
            "text_files/part_b/b_test1_decoded.txt")

        with open("text_files/part_b/b_test1_decoded.txt") as student_out, \
                open("text_files/part_b/b_test1.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    def test_huffman_decode_03(self):
        huffman_decode(
            "text_files/part_b/b_test2_out.txt",
            "text_files/part_b/b_test2_decoded.txt")

        with open("text_files/part_b/b_test2_decoded.txt") as student_out, \
                open("text_files/part_b/b_test2.txt") as correct_out:
            self.assertEqual(student_out.read(), correct_out.read())

    # def test_huffman_decode_04(self):
    #     huffman_decode(
    #         "text_files/war_and_peace_out.txt",
    #         "text_files/war_and_peace_decoded.txt")
    #
    #     with open("text_files/war_and_peace_decoded.txt") as student_out, \
    #             open("text_files/war_and_peace.txt") as correct_out:
    #         self.assertEqual(student_out.read(), correct_out.read())


if __name__ == '__main__':
    unittest.main()
