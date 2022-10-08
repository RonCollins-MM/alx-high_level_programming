#!/usr/bin/python3
"""this module serializes a string"""

import json

def to_json_string(my_obj):
    """This function returns the JSON representation of an object(string)

    Args:
        my_object: Object(string) to be serialized

    Returns:
        The JSON representation of the object(string)

    """
    return json.dumps(my_obj)
