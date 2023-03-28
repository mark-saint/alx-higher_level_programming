#!/usr/bin/python3
"""
Cool stuff
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise ValueError
