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
     
    def test_x_getter(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)

    def test_width_setter(self):
        r = Rectangle(10, 2)
        r.width = 4
        self.assertEqual(r.width, 4)

    def test_init_height_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10, "2")
    
    def test_init_width_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle("10", 2)

    def test_init_x_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,2,"1")

    def test_init_y_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,2,2,"1")

    def test_init_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(-1,1)
   
    def test_init_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2,-1)

    def test_init_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2,2,-1)

    def test_init_y(self):
        with self.assertRaises(ValueError):
            r = Rectangle(2,2,2,-1)

    def test_setter_width_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,10)
            r.width = "3"

    def test_setter_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10,10)
            r.width = -1

    def test_setter_height_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,10)
            r.height = "3"

    def test_setter_height(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10,10)
            r.height = -1

    def test_setter_x_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,10)
            r.x = "3"

    def test_setter_x(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10,10)
            r.x = -1

    def test_setter_y_str(self):
        with self.assertRaises(TypeError):
            r = Rectangle(10,10)
            r.y = "3"

    def test_setter_width(self):
        with self.assertRaises(ValueError):
            r = Rectangle(10,10)
            r.y = -1
    
    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        p = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), p)

    def test_update(self):
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        p = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(str(r), p)
         
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

