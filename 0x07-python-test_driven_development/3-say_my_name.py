#!/usr/bin/python3
"""
Introduces a person object.
"""


def say_my_name(first_name, last_name=""):
    """Prints two names in the format:
        ``My name is <first name> <last name>``

    Args:
        first_name(str)
        last_name(str)
    Raises:
        TypeError: If anything other than String is passed into function
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
