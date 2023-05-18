#!/usr/bin/python3
"""
This is a base script
"""


import json
import os
import csv


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

    @classmethod
    def create(cls, **dictionary):
        """
        creates an instance
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
                new.update(**dictionary)
            elif cls.__name__ == "Square":
                new = cls(1)
                new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """
        sdfasdf
        """
        list_ = []
        file_name = "{}.json".format(cls.__name__)
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                instances = Base.from_json_string(f.read())
            for instance_ in instances:
                instance_ = cls.create(**instance_)
                list_.append(instance_)
            return list_
        else:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        save to csv
        """
        class_name_file = "{}.csv".format(cls.__name__)
        if list_objs is None:
            with open(class_name_file, 'w') as f:
                f.write("[]")

        else:
            list_objs = [f.to_dictionary() for f in list_objs]
            if cls.__name__ == "Rectangle":
                field_names = ['id', 'width', 'height', 'x', 'y']
            elif cls.__name__ == "Square":
                field_names = ['id', 'size', 'x', 'y']

            with open(class_name_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=field_names)
                writer.writeheader()
                for obj in list_objs:
                    writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """
        sadfasdf
        """
        list_ = []
        class_name_file = "{}.csv".format(cls.__name__)
        if os.path.exists(class_name_file):
            with open(class_name_file, newline='') as csvfile:
                reader = csv.DictReader(csvfile)

                for row in reader:
                    row = dict([key, int(value)] for key, value in row.items())
                    instance_ = cls.create(**row)
                    list_.append(instance_)
            return list_
        else:
            return []
