#!/usr/bin/python3
"""writes serialized text to a file"""

import json

def save_to_json_file(my_obj, filename):
    """Converts and object to JSON and writes to a file

    Args:
        my_obj - The object to be converted
        filename - The file to be written to

    """
    with open(filename, "w", encoding="UTF-8") as fi:
        fi.write(json.dumps(my_obj))
