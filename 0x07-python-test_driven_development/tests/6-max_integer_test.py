#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_number(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_non_int(self):
        self.assertRaises(TypeError, max_integer, [1, "mark", 3])


