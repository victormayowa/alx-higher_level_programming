#!/usr/bin/python3
"""Function that returns JSON representation of an object (string)..
"""
import json

'''

'''


def to_json_string(my_obj):
    """
    # Write a function that returns the JSON representation...
    # ...of an object (string):
    # VARIABLE(" "):
    # JSON String(my_obj): To JSON string
    # Return: Always 0. (Success)
    """
    """'to_json_string' function is defined with an optional parameter..
    which represents the object to be converted to a JSON string...
    ..The 'json.dumps()' function is used to convert the object to a...
    JSON string...The 'dumps()' function takes an object as input and...
    returns its JASON representation..."""
    return json.dumps(my_obj)
    """Finally, we return the JSON string representation of the object."""
