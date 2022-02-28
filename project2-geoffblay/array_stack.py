from typing import Any


class ArrayStack:
    def __init__(self, capacity: int = 5):
        self.items: list[Any] = [None] * capacity
        self.capacity: int = capacity
        self.size: int = 0

    def __eq__(self, other):
        return isinstance(other, ArrayStack) and self.items == other.items and\
               self.capacity == other.capacity and self.size == other.size


def double_capacity(stack: ArrayStack):
    new_items = [None] * (2 * stack.capacity)

    for i in range(0, stack.capacity):
        new_items[i] = stack.items[i]

    stack.items = new_items
    stack.capacity *= 2


def empty_stack() -> ArrayStack:
    return ArrayStack()


def push(stack: ArrayStack, value: Any) -> None:
    if stack.size == stack.capacity:
        double_capacity(stack)

    stack.items[stack.size] = value
    stack.size += 1


def pop(stack: ArrayStack) -> Any:
    if stack.items[0] is None:
        raise IndexError

    temp = stack.items[stack.size - 1]
    stack.items[stack.size - 1] = None
    stack.size -= 1
    return temp


def peek(stack: ArrayStack) -> Any:
    if stack.items[0] is None:
        raise IndexError

    return stack.items[stack.size - 1]


def is_empty(stack: ArrayStack) -> bool:
    return stack.items[0] is None


def size(stack: ArrayStack) -> int:
    return stack.size
