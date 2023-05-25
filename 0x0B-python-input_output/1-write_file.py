#!/usr/bin/python3
"""
sdfjndflk
"""


def write_file(filename="", text=""):
    """
    writes a file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
