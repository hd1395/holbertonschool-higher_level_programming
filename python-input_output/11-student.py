#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represents a student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Gets a dictionary representation of the Student.
        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved.
        Otherwise, all attributes must be retrieved.

        Returns:
            dict: dictionary representation.
        """
        if attrs is None:
            return self.__dict__

        result_dict = {}
        for attr in attrs:
            try:
                result_dict[attr] = self.__dict__[attr]
            except Exception:
                pass
        return result_dict

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
        json (dict): The key/value pairs to replace attributes with.
        """
        for key, value in json.items():
            setattr(self, key, value)
