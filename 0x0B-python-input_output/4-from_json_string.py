#!/usr/bin/python3
"""
converts a JSON string to a python object)
"""
import json
"""
"""


def from_json_string(my_str):
    """"
    Returns an object (Python data structure) represented by a JSON string.

    Args:
        my_str: JSON string to be converted to an object.

    Returns:
        object: Python data structure represented by the JSON string.
    """
    return json.loads(my_str)
    """
    return the Python Object ofJSON string
    """
