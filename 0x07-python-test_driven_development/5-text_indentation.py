#!/usr/bin/python3
"""
This script contains a function
that prints a text with 2 new
lnes after each of the chars . ?
"""


def text_indentation(text):
    """
    :param text
    Returns modified text
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = ""
    for i in text:
        new_text += i
        if i == "." or i == "?":
            new_text += "\n\n"

    print(new_text)
