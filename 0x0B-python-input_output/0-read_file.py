#!/usr/bin/python3
"""Module with a function that reads from a file"""


def read_file(filename=""):
    """this functions reads from a file"""

    with open(filename, "r", encoding="UTF-8") as thisfile:
        print(thisfile.read(), end="")
