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

    @property
    def x(self):
        """This is a setter for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """This is a getter for x"""
        self.__x = value

    @property
    def y(self):
        """This is a setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is a getter for y"""
        self.__y = value

    @property
    def width(self):
        """This is a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is a setter for width"""
        self.__width = value

    @property
    def height(self):
        """This is a getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is a setter for height"""
        self.__height = height
