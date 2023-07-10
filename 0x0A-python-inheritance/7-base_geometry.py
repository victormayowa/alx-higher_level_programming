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

    def integer_validator(self, name, value):
        """
        Validates the value as an integer

        Args:
            name (str): The name of the value
            value (int): The value to be validated

        Raises:
            TypeError: If the value is not an integer
            ValueError: If the value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
