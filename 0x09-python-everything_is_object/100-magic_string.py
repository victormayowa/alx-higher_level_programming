#!/usr/bin/python3
"""
Module: 100-magic_string
Contains a function that returns a string "BestSchool" n times based on the number of iterations.
"""


def magic_string():
    """
    Generates a string "BestSchool" n times based on the number of iterations.

    Returns:
        str: A string with "BestSchool" repeated n times.

    """
    magic_string.count = getattr(magic_string, 'count', -1) + 1
    return "BestSchool, " * magic_string.count + "BestSchool"
