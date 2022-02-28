from __future__ import annotations

from typing import Optional


# class Node:
#     """Represents a node to be used in a doubly linked list."""
#
#     def __init__(
#             self,
#             value: Any,
#             prev: Optional[Node] = None,
#             nxt: Optional[Node] = None):
#         self.value = value
#
#         # NOTE: This means that if prev and nxt are None, self.prev and
#         # self.next will be self.  You may find this useful.  This means
#         # that self.prev and self.next aren't Optional Nodes, they are
#         # always Nodes.
#         self.prev: Node = prev or self
#         self.next: Node = nxt or self
#
#     # def __repr__(self) -> str:
#     #     return 'Pair(%r, %r, %r)' % (self.value, self.prev, self.next)


class OrderedList:

    def __init__(self):
        self.head = HuffmanNode(None)
        self.size: int = 0


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

    # def __lt__(self, other) -> bool:
    #     """Returns True if and only if self < other."""
    #     if self.frequency != other.frequency:
    #         return self.frequency < other.frequency
    #
    #     return self.char < other.char
    #
    # def __le__(self, other) -> bool:
    #     return self.frequency <= other.frequency
    #
    # def __gt__(self, other):
    #     if self.frequency != other.frequency:
    #         return self.frequency > other.frequency
    #
    #     return self.char > other.char

    def __eq__(self, other):
        return isinstance(other, HuffmanNode) and self.char == other.char and \
               self.frequency == other.frequency and self.left == other.left \
               and self.right == other.right


def insert(lst: OrderedList, node: HuffmanNode):
    # if lst.head.next.char is None:
    #     new = HuffmanNode(node.char, node.frequency, node.left, node.right,
    #                       lst.head, lst.head)
    #     lst.head.next = new
    #     lst.head.prev = new
    #     lst.size += 1
    #     return
    #
    # elif lst.head.next.char is not None:
    #     curr = lst.head.next
    #     prev = lst.head
    #     while curr != lst.head:
    #         if node < curr and prev == lst.head:
    #             new = HuffmanNode(node.char, node.frequency, node.left,
    #                               node.right, lst.head, curr)
    #             lst.head.next = new
    #             curr.prev = new
    #             lst.size += 1
    #             return
    #
    #         elif curr < node and prev == lst.head:
    #             prev = curr
    #             curr = prev.next
    #             continue
    #
    #         elif prev < node < curr:
    #             new = HuffmanNode(node.char, node.frequency, node.left,
    #                               node.right, prev, curr)
    #             prev.next = new
    #             curr.prev = new
    #             lst.size += 1
    #             return
    #
    #         prev = curr
    #         curr = curr.next
    #
    #     new = HuffmanNode(node.char, node.frequency, node.left, node.right,
    #                       prev, curr)
    #     prev.next = new
    #     curr.prev = new
    #     lst.size += 1

    if lst.head.next.char is None:
        node.prev = lst.head
        node.next = lst.head
        lst.head.next = node
        lst.head.prev = node
        lst.size += 1
        return

    elif lst.head.next.char is not None:
        curr = lst.head.next
        prev = lst.head
        while curr != lst.head:
            if node < curr and prev == lst.head:
                node.prev = lst.head
                node.next = curr
                lst.head.next = node
                curr.prev = node
                lst.size += 1
                return

            elif curr < node and prev == lst.head:
                prev = curr
                curr = prev.next
                continue

            elif prev < node < curr:
                node.prev = prev
                node.next = curr
                prev.next = node
                curr.prev = node
                lst.size += 1
                return

            prev = curr
            curr = curr.next

        node.prev = prev
        node.next = curr
        prev.next = node
        curr.prev = node
        lst.size += 1


# def remove(lst: OrderedList, value: Any) -> None:
#     # removes a given value from a given OrderedList
#     curr = lst.head
#     stop = False
#
#     if curr.next.value is not None:
#         curr = curr.next
#         while curr != lst.head and not stop:
#             if curr.value == value:
#                 curr.prev.next = curr.next
#                 curr.next.prev = curr.prev
#                 lst.size -= 1
#                 return
#             elif curr.value > value:
#                 stop = True
#             else:
#                 curr = curr.next
#
#     raise ValueError


# def contains(lst: OrderedList, value: Any) -> bool:
#     # returns true if the given OrderedList contains the given value, False
#     # if not
#     curr = lst.head
#     stop = False
#
#     if curr.next.value is not None:
#         curr = curr.next
#         while curr != lst.head and not stop:
#             if curr.value == value:
#                 return True
#             elif curr.value > value:
#                 stop = True
#             else:
#                 curr = curr.next
#
#     return False


# def index(lst: OrderedList, value: Any) -> int:
#     # returns the index of the given value in the given OrderedList
#     count = 0
#     curr = lst.head
#
#     if curr.next.value is not None:
#         curr = curr.next
#         while curr != lst.head:
#             if curr.value == value:
#                 return count
#             count += 1
#             curr = curr.next
#
#     raise ValueError


def get(lst: OrderedList, index: int) -> HuffmanNode:
    curr = lst.head.next
    count = 0

    while curr != lst.head:
        if count == index:
            return curr
        count += 1
        curr = curr.next

    raise IndexError


def pop(lst: OrderedList, index: int) -> HuffmanNode:
    curr = lst.head
    count = 0

    if curr.next.char is not None:
        curr = curr.next
        while curr != lst.head:
            if count == index:
                ret = curr
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                lst.size -= 1
                return ret
            count += 1
            curr = curr.next

    raise IndexError


# def is_empty(lst: OrderedList) -> bool:
#     # returns true if the given OrderedList is empty, false if not
#     return lst.size == 0
#
#
# def size(lst: OrderedList) -> int:
#     # returns the number of elements in the given OrderedList
#     return lst.size
