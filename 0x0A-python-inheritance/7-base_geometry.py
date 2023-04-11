#!/usr/bin/python3
'''
script contains a class
BaseGeometrt
'''


class BaseGeometry(object):
    '''
    this is an empty class
    '''
    def area(self):
        '''
        one has to implement this
        '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''validates the value'''

        if not isinstance(value, int):
            raise TypeError(f"{name} must be integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
