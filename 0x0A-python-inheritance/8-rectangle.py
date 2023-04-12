#!/usr/bin/python3
'''script contains Rectangle class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''This is a rectangle class'''

    def __init__(self, width, height):
        '''this is the init class'''

        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)
