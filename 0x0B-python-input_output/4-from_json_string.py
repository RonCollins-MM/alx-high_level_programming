#!/usr/bin/python3
"""Module that deserialises a string"""

import json

def from_json_string(my_str):
    """Converts a JSON string to an object(Python Data Structure)

    Args:
        my_str - The JSON string to convert

    Returns:
        An object(Python data structure)

    """
    return(json.loads(my_str))
