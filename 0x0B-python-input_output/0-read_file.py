#!/usr/bin/python3
"""
kfadslkjdsfjkdfs
"""


def read_file(file_name=""):
    """
    reads a file
    """
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
