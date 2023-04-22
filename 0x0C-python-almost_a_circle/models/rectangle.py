#!/usr/bin/python3
"""
This is a script having the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    This is a rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        :param widht
        :param height
        :param x
        :param y
        """
        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
