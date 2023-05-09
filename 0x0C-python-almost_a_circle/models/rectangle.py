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
        if not isinstance(width,int):
            raise TypeError("width must be an integer")
        if not isinstance(height,int):
            raise TypeError("height must be an integer")
        if not isinstance(x,int):
            raise TypeError("x must be an integer")
        if not isinstance(y,int):
            raise TypeError("y must be an integer")
        if id is not None:
            if not isinstance(id,int):
                raise TypeError("id must be an integer")

        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")

        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """This is a setter for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """This is a getter for y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    @property
    def width(self):
        """This is a getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This is a setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """This is a getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """This is a setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    def area(self):
        """Area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
