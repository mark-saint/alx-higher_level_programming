#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id - 1)

    def test_id2(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_args(self):
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_x(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(10, 2)
            r.__x

    def test_y(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(10, 2)
            r.__y

    def test_width(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(10, 2)
           # r.width = 2
            r.__width

    def test_height(self):
        with self.assertRaises(AttributeError):
            r = Rectangle(10, 2)
            r.__height

    def test_x_setter(self):
        r = Rectangle(10, 2)
        r.x = 10
        self.assertEqual(10, r.x)
        
