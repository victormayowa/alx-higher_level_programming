#!/usr/bin/python3
"""
Module: 101-locked_class
Contains a class that prevents dynamically creating new instance attributes, except for "first_name".
"""


class LockedClass:
    """
    A class that prevents dynamically creating new instance attributes, except for "first_name".
    """

    __slots__ = ['first_name']
