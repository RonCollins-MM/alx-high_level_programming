#!/usr/bin/python3
"""
Finds the largest integer in a list
"""


def max_integer(list=[]):
    """Function that finds the largest integer from a list.

    Args:
        The list to be searched
    Returns:
        The largest int
    """
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
