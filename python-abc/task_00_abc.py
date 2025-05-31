#!/usr/bin/python3
""" Module for Abstract Animal Class and its Subclasses """

from abc import ABC, abstractmethod


class Animal(ABC):
    """Animal class
    Args:
        ABC
    Returns:
        Nothing
    """

    @abstractmethod
    def sound(self):
        """defines sound method.

            Returns:
                Nothing
        """

        return ""


class Dog(Animal):
    """Dog Class"""

    def sound(self):
        """overrides abstract method of Animal"""

        return "Bark"


class Cat(Animal):
    """Cat Class"""

    def sound(self):
        """overrides abstract method of Animal"""

        return "Meow"
