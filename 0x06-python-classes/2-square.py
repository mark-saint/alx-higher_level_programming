#!/usr/bin/python3
"""
Cool stuff
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        """
        Args:
            size: sth
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
