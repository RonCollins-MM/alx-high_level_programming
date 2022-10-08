#!/usr/bin/python3
"""
Module that adds two integers together.

"""

def add_integer(a, b=98):
    """Adds two integers. If the parameters passed are not of type ``int`` or
    ``float``, an TypeError is thrown. Floats passed are rounded to the neares int.

    Args:
        a - First integer
        b - Second integer

    Returns:
        Sum of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
