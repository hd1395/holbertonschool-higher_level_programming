#!/usr/bin/python3

"""'add_attribute' module"""


def add_attribute(obj, attribute, value):
    """
    adds a new attribute to an object if it is possible
    Raise a TypeError exception, if the object can’t have new attribute
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
