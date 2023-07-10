#!/usr/bin/python3
"""
Module for Square class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class, inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes a Square instance

        Args:
            size (int): The size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square

        Returns:
            str: The square description
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
