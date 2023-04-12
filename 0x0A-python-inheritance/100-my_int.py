#!/usr/bin/python3
'''
script contains a myint class
'''


class MyInt(int):
    '''this is the myint class'''

    def __ne__(self, value):
        '''inverts == '''
        return self is not value

    def __eq__(self, value):
        '''inverts != '''

        return self is value
