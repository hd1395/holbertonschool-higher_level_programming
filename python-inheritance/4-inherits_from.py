#!/usr/bin/python3
'''Module for inherits_from method.'''


def inherits_from(obj, a_class):
    '''object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    arguments:
        obj(object) whose class is to be inspected
        a_class(class) the class to be inspected
    Return: True if the class of the object is a subclass of the specified
            class, otherwise false
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
