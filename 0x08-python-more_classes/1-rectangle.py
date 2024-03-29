#!/usr/bin/python3
"""
This is a real Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        Instantiate a rectangle class
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrive width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
