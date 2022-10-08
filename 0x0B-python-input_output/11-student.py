#!/usr/bin/python3
"""Module with Student class that can be converted to JSON or modified from a JSON"""

class Student:
    """Student class implementation"""

    def __init__(self, first_name, last_name, age):
        """Constructor

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves attributes from an instance of this class and returns a
        dictionary object of the attributed.

        See ``10-student.py`` for more details.
        """
        thisdict = dict()
        if type(attrs) is list:
            for i in list(self.__dict__):
                for j in attrs:
                    if i == j:
                        thisdict[j] = self.__dict__[i]
            return thisdict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Changes the attributes of an instance of this class from a JSON
        string.

        Args:
            json - The json file to read from.

        """
        for i in list(self.__dict__):
            if i in list(json):
                self.__dict__[i] = json[i]
