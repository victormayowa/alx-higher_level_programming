#!/usr/bin/python3
"""
Module for MyInt class
"""


class MyInt(int):
    """
    MyInt class, inherits from int
    """

    def __eq__(self, other):
        """
        Overrides the == operator
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator
        """
        return super().__eq__(other)
