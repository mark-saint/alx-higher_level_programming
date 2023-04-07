#!/usr/bin/python3
"""
this file does bla bla
bla bla
bla bla
"""


def say_my_name(first_name, last_name=""):
    """
    :param first_name
    :param last_name
    Returns
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
