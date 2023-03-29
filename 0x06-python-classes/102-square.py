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

    def __eq__(self, other):
        """equal to """
        return self.area() == other.area()

    def __ne__i(self, other):
        """ not equal to"""
        return self.area() != other.area()

    def __gt__(self, other):
        """greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """greater equal"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """less than"""
        return self.area() <= other.area()
