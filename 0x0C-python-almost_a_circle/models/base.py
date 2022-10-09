#!/usr/bin/python3
"""Base Class Module"""

import models
import json
import os


class Base:
    """Base class Implementation"""

    __nb_objects = 0
    """int: Public attribute to keep track of number of instances from child
    Classes"""

    def __init__(self, id=None):
        """Constructor.

        Args:
            id (int) - Identification for each obejct. (Default = None)

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Generates a JSON string from a List of Dictionaries. If an  empty list
        is passed, an empty string is returned.

        Args:
            list_dictionaries - The List of Dictionaries to process from
        Returns:
            The JSON string generated if non-empty list passed, othwerwise,
            returns an empty string.
        """
        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves JSON representation of a list of objects to a file.

        The list of objects is first converted to a corresponding list of their
        dictionary equivalents.
        If empty list is passed, an empty string is saved to file.

        File will be created if it doesn't exist.
        The file name is auto-generated with the format: ``<class_name>.json``
        Contents of file will be overwritten if it exists.

        Args:
            list_objs - A list of objects that inherit from Base Class.
        """
        with open(f'{cls.__name__}.json', 'w', encoding='UTF-8') as f:
            dict_list = []
            if list_objs is not None:
                for i in list_objs:
                    dict_list.append(i.to_dictionary())
            f.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """Generates Python Dict object from JSON string. If JSON string is
        empty, an empty List is returned.

        Args:
            json_string - The JSON string to generate from

        Returns:
            Python Dict object from JSON string.
        """
        if json_string is None or "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates a new instance of the Rectangle or
        Square child class from a dictionary object.

        Uses the update method from the respective Class.
        A dummy instance is created first and then updated with the passed
        attributes.

        Args:
            **dictionary(:obj: dict) - dictionary containing attributes to
            create new instance with.

        Returns:
            The created instance
        """

        inst = ""
        if cls.__name__ == "Rectangle":
            inst = models.rectangle.Rectangle(1, 1)
        else:
            inst = models.square.Square(1)
        inst.update(**dictionary)
        return inst

    @classmethod
    def load_from_file(cls):
        """Creates instances of Rectangle or Square child classes from a JSON
        string and bundles them into a List object.

        The instances are created from a JSON file. Once the JSON file is read,
        a dictionary object containing dictionaries that contain attributes
        either Square or Rectangle objects is returned.
        Instances are then created from these nested dictionaries and appended
        to a List object.

        Returns:
            A list of instances from Square or Rectangle class.
        """

        # Make sure file exists
        j_file = f"{cls.__name__}.json"
        if not os.path.exists(j_file):
            return []

        # Open JSON file and read from it. Result is a Dict object
        with open(j_file, "r", encoding="UTF-8") as f:
            dict_ = Base.from_json_string(f.read())

        # Create a list of instances from the Dict object obtained
        inst_list = []
        for i in dict_:
            if cls.__name__ == "Rectangle":
                inst_list.append(models.rectangle.Rectangle.create(**i))
            else:
                inst_list.append(models.square.Square.create(**i))
        return int_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to a csv file"""
        with open("{}.csv".format(cls.__name__), "w", encoding="UTF-8") as f:
            if list_objs is not None:
                f.mode = "a"
                for i in list_objs:
                    if cls.__name__ == "Rectangle":
                        f.write("{},{},{},{},{}\n".format(i.id, i.width,
                                                          i.height, i.x, i.y))
                    else:
                        f.write("{},{},{},{}\n".format(i.id, i.size,
                                                       i.x, i.y))

    @classmethod
    def load_from_file_csv(cls):
        """load from csv file"""
        f = "{}.csv".format(cls.__name__)
        if not os.path.exists(f):
            return []
        thislist = []
        with open(f, "r", encoding="UTF-8") as f:
            for line in f:
                data = line.split(",")
                if cls.__name__ == "Rectangle":
                    thislist.append(models.rectangle.
                                    Rectangle.create(**{'id': int(data[0]),
                                                        'width': int(data[1]),
                                                        'height': int(data[2]),
                                                        'x': int(data[3]),
                                                        'y': int(data[4])}))
                else:
                    thislist.append(models.square.Square
                                    .create(**{'id': int(data[0]),
                                               'size': int(data[1]),
                                               'x': int(data[2]),
                                               'y': int(data[3])}))
        return thislist
