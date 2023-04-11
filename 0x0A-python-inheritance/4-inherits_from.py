#!/usr/bin/python3
'''
Contains a script that inherits from
sht
'''


def inherits_from(obj, a_class):
    '''
    :param obj
    :param a_class
    Returns  bool
    '''

    mro_ = a_class.__mro__
    if type(obj) in mro_:
        return False
    else:
        return True
