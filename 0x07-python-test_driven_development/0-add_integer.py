#!/usr/bin/python3
"""
this creates a function of interest
that adds 2 integer numbers
it returns an integer
"""


def add_integer(a, b=98):
    """
    This functions adds 2 integer numbers 
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b

