#!/usr/bin/python3
"""
Square Module
"""


class Square:
    """
    Defines a square by its size.
    """
    def __init__(self, size):
        """
        Initializes a square instance.

        Args:
            size (int): The size of the square.

        Attributes:
            __size (int): The private instance attribute representing the size of the square.
        """
        self.__size = size
