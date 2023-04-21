#/usr/bin/python3
"""
This tests the base class
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_none(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_not_none(self):
        b2 = Base(12)
        self.assertEqual(b2.id, 12)
