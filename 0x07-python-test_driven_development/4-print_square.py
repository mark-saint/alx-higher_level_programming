#!/usr/bin/python3
"""
this script contains a function
that prints a square with the
character #
"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        if isinstance(size, float):
            raise TypeError("size must be an integer")
        raise ValueError("size must be >= 0")

    list_ = []
    for i in range(size):
        list_.append("#" * size)
    print("\n".join(length for length in list_))
