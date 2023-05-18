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
            for dict_ in list_dictionaries:
                json_dict.append(json.dumps(dict_))
            return json_dict
        else:
            return list_dictionaries
