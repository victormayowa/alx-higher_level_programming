#!/usr/bin/python3
""" MOdule for base class unit testing """
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    def test_init(self):
        b = Base()
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 1)

        b = Base(10)
        self.assertIsInstance(b, Base)
        self.assertEqual(b.id, 10)

    def test_to_json_string(self):
        r = Rectangle(10, 5, 1, 2)
        json_str = r.to_json_string([r.to_dictionary()])
        self.assertEqual(json_str, '[{"id": 1, "width": 10, "height": 5, "x": 1, "y": 2}]')

    def test_from_json_string(self):
        json_str = '[{"id": 1, "width": 10, "height": 5, "x": 1, "y": 2}]'
        objs = Base.from_json_string(json_str)
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], dict)
        self.assertEqual(objs[0]['id'], 1)

    def test_save_to_file(self):
        r = Rectangle(10, 5, 1, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1, "width": 10, "height": 5, "x": 1, "y": 2}]')

    def test_load_from_file(self):
        objs = Rectangle.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 1)

    def test_save_to_file_csv(self):
        r = Rectangle(10, 5, 1, 2)
        Rectangle.save_to_file_csv([r])
        with open("Rectangle.csv", "r") as file:
            content = file.read()
            self.assertEqual(content, '1,10,5,1,2\n')

    def test_load_from_file_csv(self):
        objs = Rectangle.load_from_file_csv()
        self.assertEqual(len(objs), 1)
        self.assertIsInstance(objs[0], Rectangle)
        self.assertEqual(objs[0].id, 1)

    def test_draw(self):
        r = Rectangle(10, 5, 1, 2)
        s = Square(5, 3, 4)
        Base.draw([r], [s])  # Verify visually
