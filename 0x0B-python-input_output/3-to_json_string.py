#!/usr/bin/python3
"""
Function that returns JSON representation of an object (string)..
"""


import json
'''
import json module
'''


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: Object to be serialized to JSON.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
