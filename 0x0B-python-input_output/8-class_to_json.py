#!/usr/bin/python3
"""A function that returns the dictionary description of an object for
serialization"""

def class_to_json(obj):
    """Returns the dict of an obj instance for covnversion to JSON

    Args:
        obj - The object to be converted to __dict__

    Returns:
        The object dictionary format

    """
    return obj.__dict__
