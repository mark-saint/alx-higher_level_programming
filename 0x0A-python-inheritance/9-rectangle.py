#!/usr/bin/python3
'''script contains Rectangle class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This is a rectangle class'''

    def __init__(self, width, height):
        '''this is the init class'''

        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def area(self):
        '''returns the area of a rectangle'''

        return self.__width * self.__height

    def __str__(self):
        '''does representation stuff'''

        return f"[Rectangle] {self.__width}/{self.__height}"

    def __repr__(self):
        '''prints the representation'''

        return (f"[Rectangle] {self.__width}/{self.__height}")
