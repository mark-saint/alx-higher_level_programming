#!/usr/bin/python3
"""
asdfsdf
"""


class Student:
    """
    dsfs
    """
    def __init__(self, first_name, last_name, age):
        """
        sadf
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        asfasdf
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for k in attrs:
                if k in self.__dict__:
                    new_dict[k] = self.__dict__[k]
            return new_dict

    def reload_from_json(self, json):
        """
        sdfdas
        """
        self.__dict__ = json
