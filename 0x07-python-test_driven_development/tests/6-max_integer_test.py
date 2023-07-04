#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Class containing unit tests for the max_integer function
    """

    def test_empty_list(self):
        """
        Test for an empty list
        """
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """
        Test for a list with a single element
        """
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        """
        Test for a list of positive numbers
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_negative_numbers(self):
        """
        Test for a list of negative numbers
        """
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)
        self.assertEqual(max_integer([-2, -2, -2, -2]), -2)

    def test_mixed_numbers(self):
        """
        Test for a list of mixed positive and negative numbers
        """
        self
