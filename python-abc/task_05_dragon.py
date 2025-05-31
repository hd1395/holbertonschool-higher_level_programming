#!/usr/bin/python3
""" Module for mixin and Dragon classes """

class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        """prints a string"""
        print("The creature swims!")

class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        """prints a string"""
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        """prints a string"""
        print("The dragon roars!")
