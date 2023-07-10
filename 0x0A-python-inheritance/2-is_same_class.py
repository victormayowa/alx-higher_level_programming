#!/usr/bin/python3
"""
Module for is_same_class method
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a specified class.

    Args:
        obj (object): The object to be checked.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is exactly an instance of the specified class, False otherwise.
    """
    return type(obj) is a_class
