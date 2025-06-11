#!/usr/bin/python3
"""
Module that provides function to serialize
and deserialize a custom Python objects using pickle.
"""


import pickle


class CustomObject:
    
    def __init__(self, name, age, is_student):
        """
        Initializes the object
        """

        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Prints out the object’s attributes
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object to the filename using pickle.

        Args:

        filename: The name of the file to save the JSON data.
        """

        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize and return an instance of CustomObject from the filename.

        filename: The name of the JSON file to read from.

        Returns: An instance of CustomObject if success, othwerwise None

        Throws: Exception if file does not exist or malformed
        """
        try:
            with open(filename, 'rb') as text_file:
                obj = pickle.load(text_file)
                if isinstance(obj, cls):
                    return obj
        except Exception:
            return None
