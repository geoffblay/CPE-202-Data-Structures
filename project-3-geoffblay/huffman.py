from __future__ import annotations

from typing import Optional
from ordered_list import OrderedList, insert, pop, get


# from ordered_list_huffman import insert, OrderedList, pop, get


class HuffmanNode:
    """Represents a node in a Huffman tree.

    Attributes:
        char: The character as an integer ASCII value
        frequency: The frequency of the character in the file
        left: The left Huffman sub-tree
        right: The right Huffman sub-tree
    """

    def __init__(
            self,
            char: Optional[int] = None,
            frequency: Optional[int] = None,
            left: Optional[HuffmanNode] = None,
            right: Optional[HuffmanNode] = None,
            prev: Optional[HuffmanNode] = None,
            nxt: Optional[HuffmanNode] = None):
        self.char = char
        self.frequency = frequency
        self.left = left
        self.right = right
        self.prev: HuffmanNode = prev or self
        self.next: HuffmanNode = nxt or self

    def __lt__(self, other) -> bool:
        """Returns True if and only if self < other."""
        if self.frequency != other.frequency:
            return self.frequency < other.frequency

        return self.char < other.char

    # def __gt__(self, other):
    #     if self.frequency != other.frequency:
    #         return self.frequency > other.frequency
    #
    #     return self.char > other.char

    def __eq__(self, other):
        return isinstance(other, HuffmanNode) and self.char == other.char and \
               self.frequency == other.frequency and self.left == other.left \
               and self.right == other.right


HT = Optional[HuffmanNode]


def is_leaf(node: HuffmanNode) -> bool:
    return node.left is None and node.right is None


def search_tree(tree: HT, char: int) -> bool:
    if tree is None:
        return False

    if tree.char == char:
        return True

    return search_tree(tree.left, char) or search_tree(tree.right, char)


def build_codes(tree: HT, char: int, code: str = '') -> str:
    # while tree is not None:
    if tree.char == char and is_leaf(tree):
        return code

    elif search_tree(tree.right, char):
        code += '1'
        return build_codes(tree.right, char, code)

    elif search_tree(tree.left, char):
        code += '0'
        return build_codes(tree.left, char, code)


def count_frequencies(filename: str) -> list[int]:
    """Reads the given file and counts the frequency of each character.

    The resulting Python list will be of length 256, where the indices
    are the ASCII values of the characters, and the value at a given
    index is the frequency with which that character occured.
    """
    lst_freq = [0] * 256
    str_file = open(filename, 'r')
    for line in str_file:
        for char in line:
            lst_freq[ord(char)] += 1

    return lst_freq


def build_huffman_tree(frequencies: list[int]) -> Optional[HuffmanNode]:
    """Creates a Huffman tree of the characters with non-zero frequency.

    Returns the root of the tree.
    """
    ordered = OrderedList()
    count = 0
    for i in range(0, len(frequencies)):
        if frequencies[i] != 0:
            count += 1
            insert(ordered, HuffmanNode(i, frequencies[i]))

    if count == 0:
        return HuffmanNode()

    if count == 1:
        return get(ordered, 0)

    while ordered.size > 1:
        first = pop(ordered, 0)
        second = pop(ordered, 0)
        freq = first.frequency + second.frequency

        if first.char < second.char:
            new = HuffmanNode(first.char, freq, first, second)
        else:
            new = HuffmanNode(second.char, freq, first, second)

        insert(ordered, new)

    return get(ordered, 0)


def create_codes(tree: Optional[HuffmanNode]) -> list[str]:
    lst_codes = [''] * 256

    for i in range(0, len(lst_codes)):
        lst_codes[i] = build_codes(tree, i)

    return lst_codes


def create_header(frequencies: list[int]) -> str:
    """Returns the header for the compressed Huffman data.

    For example, given the file "aaaccbbbb", this would return:
    "97 3 98 4 99 2"
    """
    header = ''
    for i in range(0, len(frequencies)):
        if frequencies[i] != 0:
            header += str(i) + ' ' + str(frequencies[i]) + ' '

    return header.strip()


def huffman_encode(in_filename: str, out_filename: str) -> None:
    """Encodes the data in the input file, writing the result to the
    output file."""
    codes = create_codes(build_huffman_tree(count_frequencies(in_filename)))
    header = create_header(count_frequencies(in_filename))
    with open(in_filename, 'r') as input_file:
        with open(out_filename, 'w') as output_file:
            output_file.write(header + '\n')

            for line in input_file:
                for char in line:
                    output_file.write(codes[ord(char)])

    output_file.close()
    input_file.close()


# --------------------------------------------------------------
def parse_header(string: str) -> list[int]:
    lst = [0] * 256
    lst_string = string.split()
    for i in range(0, len(lst_string), 2):
        lst[int(lst_string[i])] = int(lst_string[i + 1])

    return lst


def parse_tree(tree, string):
    # return False if it was not able to reach a leaf, and the correct
    # character if it is
    if is_leaf(tree):
        return chr(tree.char)

    elif string == '':
        raise ValueError

    elif string[0] == '0':
        return parse_tree(tree.left, string[1:])

    elif string[0] == '1':
        return parse_tree(tree.right, string[1:])


def huffman_decode(in_filename, out_filename):
    # frequencies = parse_header line 1 of file in
    with open(in_filename, 'r') as input_file:
        with open(out_filename, 'w') as output_file:
            lines = input_file.readlines()

            if len(lines[0].split()) == 2:
                lst_line = lines[0].split()
                ret_str = chr(int(lst_line[0])) * int(lst_line[1])
                output_file.write(ret_str)
                return

            if len(lines[0].split()) == 0:
                output_file.write('')
                return

            lst_frequencies = parse_header(lines[0])
            tree = build_huffman_tree(lst_frequencies)
            code = ''
            for char in lines[1]:
                code += char
                try:
                    output_file.write(parse_tree(tree, code))
                    code = ''
                except ValueError:
                    continue

    output_file.close()
    input_file.close()
