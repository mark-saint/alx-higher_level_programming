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
        else:
            self.__size = size

    def area(self):
        """
        Area here we go
        """
        return self.__size ** 2

    @getter
    def size(self):
        """
        Returns size
        """
        return self.__size

    @setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be as integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
