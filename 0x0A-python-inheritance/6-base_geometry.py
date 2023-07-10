#!/usr/bin/python3
"""
Module for BaseGeometry class
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Calculates the area of the geometry

        Raises:
            Exception: Always raises an exception with the message "area() is not implemented"
        """
        raise Exception("area() is not implemented")
