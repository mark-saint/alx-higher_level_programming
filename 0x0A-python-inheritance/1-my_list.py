#!/usr/bin/python3
"""
Script that inherits from
list
"""


class MyList(list):
    """
    This class inherits from
    list
    """

    def print_sorted(self):
        '''
        prints sorted
        list
        '''

        print(sorted(self))
