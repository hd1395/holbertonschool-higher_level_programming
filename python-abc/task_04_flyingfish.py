#!/usr/bin/python3
""" Module for FlyingFish class and subclasses """


class Fish:
    """Fish class

    Args:
        Nothing

    Returns:
        Nothing

    """

    def swim(self):
        """prints a string relevant to class"""
        print("The fish is swimming")

    def habitat(self):
        """prints a string relevant to class"""
        print("The fish lives in water")


class Bird:
    """Bird

    Args:
        Nothing

    Returns:
        Nothing

    """

    def fly(self):
        """prints a string relevant to class"""
        print("The bird is flying")

    def habitat(self):
        """prints a string relevant to class"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish

    Args:
        Nothing

    Returns:
        Nothing

    """

    def fly(self):
        """overrides method from Bird class"""
        print("The flying fish is soaring!")

    def swim(self):
        """overrides method from Fish class"""
        print("The flying fish is swimming!")

    def habitat(self):
        """overrides method from Bird and Fish class"""
        print("The flying fish lives both in water and the sky!")
