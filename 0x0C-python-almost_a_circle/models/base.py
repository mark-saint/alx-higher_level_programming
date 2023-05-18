#!/usr/bin/python3
"""
This is a base script
"""


import json


class Base:
    """
    This is a base script
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        :param id
        """

        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        does stuff
        """
        json_dict = []
        if len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
