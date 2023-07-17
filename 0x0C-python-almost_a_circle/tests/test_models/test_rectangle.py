#!/usr/bin/python3
"""  Module for unit test of rectangle class """
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 5, 1, 2)
        self.assertIsInstance(r, Rectangle)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)

    def test_area(self):
        r = Rectangle(10, 5)
        self.assertEqual(r.area(), 50)

    def test_display(self):
        r = Rectangle(3, 2)
        self.assertEqual(r.display(), None)

    def test_update(self):
        r = Rectangle(5, 10, 1, 2)
        r.update(10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        r.update(20, 8, 3, 4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 3)

    def test_to_dictionary(self):
        r = Rectangle(5, 10, 1, 2)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected_dict)
