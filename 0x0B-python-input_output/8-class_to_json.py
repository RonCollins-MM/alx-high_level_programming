#!/usr/bin/python3
"""A function that returns the dictionary description of an object for
serialization"""

def class_to_json(obj):
    """returns the dict of this obj instance for covnversion to JSON"""
    return obj.__dict__
