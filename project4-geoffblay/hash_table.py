from __future__ import annotations

from collections.abc import Callable, Hashable
from typing import Any, List, Tuple

# An entry in the hash table is a key-value pair
HashEntry = Tuple[Hashable, Any]
# Each entry in the hash table array will be a list of HashEntry pairs
HashChain = List[HashEntry]


class HashTable:
    """A hash table with separate chaining."""

    def __init__(
            self,
            capacity: int = 10,
            hash_function: Callable[[Hashable], int] = hash):
        """Creates an empty hash table.

        Args:
            capacity:
                The initial capacity of the backing array.  The default
                capacity is 10.
            hash_function:
                The function to use to compute hash values for the given
                keys.  The default hash function is the Python builtin
                hash function.
        """
        self.table: list[HashChain] = [[] for _ in range(capacity)]

        self.size: int = 0
        self.capacity: int = capacity
        self.hash_function = hash_function


def _double_capacity(hash_table: HashTable) -> HashTable:
    lst_copy = hash_table.table
    hash_table.table = [[] for _ in range(hash_table.capacity)]
    hash_table.size = 0

    for k in range(0, len(lst_copy)):
        if lst_copy[k]:
            for m in range(0, len(lst_copy[k])):
                insert(hash_table, lst_copy[k][m][0], lst_copy[k][m][1])


# NOTE: Computing the hash value of the key could be slow, we should
# only do it once.
def insert(hash_table: HashTable, key: Hashable, value: Any) -> None:
    # hash_table.size += 1
    hash_value = hash_table.hash_function(key) % hash_table.capacity
    load = (hash_table.size + 1) / hash_table.capacity

    # for i in range(0, len(hash_table.table)):
    #     for j in range(0, len(hash_table.table[i])):
    #         if hash_table.table[i][j][0] == key:
    #             hash_table.table[i][j] = (key, value)
    #             return

    for i in range(0, len(hash_table.table[hash_value])):
        if hash_table.table[hash_value][i][0] == key:
            hash_table.table[hash_value][i] = (key, value)
            return

    if load > 1:
        hash_table.capacity *= 2
        _double_capacity(hash_table)

    hash_table.table[hash_value].append((key, value))
    hash_table.size += 1


def get_item(hash_table: HashTable, key: Hashable) -> Any:
    hash_value = hash_table.hash_function(key) % hash_table.capacity
    for i in range(0, len(hash_table.table[hash_value])):
        if hash_table.table[hash_value][i][0] == key:
            return hash_table.table[hash_value][i][1]

    raise KeyError


def contains(hash_table: HashTable, key: Hashable) -> bool:
    hash_value = hash_table.hash_function(key) % hash_table.capacity
    for i in range(0, len(hash_table.table[hash_value])):
        if hash_table.table[hash_value][i][0] == key:
            return True

    return False


def remove(hash_table: HashTable, key: Hashable) -> tuple[Hashable, Any]:
    # if contains(hash_table, key):
    hash_value = hash_table.hash_function(key) % hash_table.capacity
    for element in hash_table.table[hash_value]:
        if element[0] == key:
            hash_table.table[hash_value].remove(element)
            hash_table.size -= 1
            return element

    raise KeyError


def size(hash_table: HashTable) -> int:
    return hash_table.size


def keys(hash_table: HashTable) -> list:
    list_keys = []
    for i in range(0, len(hash_table.table)):
        if hash_table.table[i]:
            for element in hash_table.table[i]:
                list_keys.append(element[0])

    return list_keys


def load_factor(hash_table: HashTable) -> float:
    return hash_table.size / hash_table.capacity


def _contents(hash_table: HashTable) -> list[HashChain]:
    return hash_table.table
