#!/usr/bin/python3
"""A module with a function that writes to a file"""


def write_file(filename="", text=""):
    """Function that writes text to a file
    
    Args:
        filename: Name of file to write to
        text: text to write

    Returns:
        The number of characters entered into the file

    """
    with open(filename, "w", encoding="UTF-8") as fi:
        count = fi.write(text)
    return count
