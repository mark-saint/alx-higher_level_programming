#!/usr/bin/python3
"""
This is a real Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Instantiate a rectangle class
        """
        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """Returns the area"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """returns a str representation of the class"""
        str_ = []
        for height_ in range(self.__height):
            str_.append(str(self.print_symbol) * self.__width)
        return "\n".join(m for m in str_)

    def __repr__(self):
        """representation of a class"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete the instance of this class"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
