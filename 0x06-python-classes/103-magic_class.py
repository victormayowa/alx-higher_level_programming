#!/usr/bin/env python3

"""
This module defines the MagicClass, which represents a circle with a given radius.
"""

import math

class MagicClass:
    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with the specified radius.

        Args:
            radius (float or int): The radius of the circle. Default is 0.

        Raises:
            TypeError: If the radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates and returns the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
