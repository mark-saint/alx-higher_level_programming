#!/usr/bin/python3
'''Script for square class'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    this is a square
    class
    '''

    def __init__(self, size):
        ''' the init method'''

        super(Square, self).__init__(size, size)

        self.__size = self.integer_validator("size", size)

    def area(self):
        '''
        area method
        '''
        return self.__size ** 2
