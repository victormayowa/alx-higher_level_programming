#!/usr/bin/python3
"""
Square Module
"""


class Square:
    """
    Defines a square by its size.
    """
    def __init__(self, size=0):
        """
        Initializes a square instance.

        Args:
            size (float or int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.

        Attributes:
            __size (float or int): The private instance attribute representing the size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (float or int): The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Checks if two square instances have the same area.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Checks if two square instances have different areas.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the areas are different, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Checks if the area of the square is less than the area of another square.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the area is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Checks if the area of the square is less than or equal to the area of another square.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the area is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Checks if the area of the square is greater than the area of another square.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the area is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Checks if the area of the square is greater than or equal to the area of another square.

        Args:
            other (Square): The other square instance to compare.

        Returns:
            bool: True if the area is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()
