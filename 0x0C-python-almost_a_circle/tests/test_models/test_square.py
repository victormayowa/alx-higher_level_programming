#!/usr/bin/pytho3
""" Module for square class and methods """
import unittest
import pep8
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_init(self):
        s = Square(5, 1, 2)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

    def test_area(self):
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        s = Square(3)
        self.assertEqual(s.display(), None)

    def test_update(self):
        s = Square(5, 1, 2)
        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        s.update(20, 8, 3, 4)
        self.assertEqual(s.id, 20)
        self.assertEqual(s.size, 8)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary(self):
        s = Square(5, 1, 2)
        expected_dict = {'id': 1, 'size': 5, 'x': 1, 'y': 2}
        self.assertEqual(s.to_dictionary(), expected_dict)
