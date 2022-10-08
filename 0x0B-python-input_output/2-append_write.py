#!/usr/bin/python3
"""Module with a function that appends text to a file"""


def append_write(filename="", text=""):
    """This function appends text to a file

    Args:
        filename: File to append text to
        text: Text to be appended

    Returns:
        The number of characters appended

    """
    with open(filename, "a", encoding="UTF-8") as fi:
        count = fi.write(text)
    return count
