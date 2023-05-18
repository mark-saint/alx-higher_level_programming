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
        if len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves to file
        """
        class_name_file = "{}.json".format(cls.__name__)
        if list_objs is None:
            with open(class_name_file, 'w') as f:
                json.dump("[]", f)

        else:
            list_objs = [f.to_dictionary() for f in list_objs]
            with open(class_name_file, 'w') as f:
                f.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """
        flslkfds
        """
        if json_string is None:
            return "[]"
        else:
            return json.loads(json_string)
