#!/usr/bin/python3
"""
Prints a square shape
"""


def print_square(size):
    """
    Prints a square of specified size using '#' character.

    Args:
        size - The size of the square

    Raises:
        TypeError: If size is not type int
        ValueError: If size is < 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
