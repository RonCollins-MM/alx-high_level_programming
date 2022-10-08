#!/usr/bin/python3
"""This module contains a Student class with an attribute to return its
__dict__ format."""

class Student:
    """Implementation for Student class"""
    def __init__(self, first_name, last_name, age):
        """Constructor.

        Args:
            first_name (str) - First name of Student
            last_name (str) - Last name of Student
            age(int) - Age of Student

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """returns dictionary repr of Student object"""
        return self.__dict__
