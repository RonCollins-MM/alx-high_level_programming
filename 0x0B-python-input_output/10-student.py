#!/usr/bin/python3
"""Student class that """


class Student:
    """Constructor"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the attributes specified from the __dict__ representation
        of an instance of the Student class. If no specific attributes are
        requested, all attributes are retrieved.

        Args:
            attrs - The attributes(keys) to be retrived

        Returns:
            A dictionary object containing the attributes retrieved

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
