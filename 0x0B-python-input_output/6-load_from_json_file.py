#!/usr/bin/python3
"""Deserializes a JSON file"""

import json

def load_from_json_file(filename):
    """Creates an object from a JSON file

    Args:
        filename - The file containing the JSON string

    """
    with open(filename, "r", encoding="UTF-8") as fi:
        text = fi.read()
    return json.loads(text)
