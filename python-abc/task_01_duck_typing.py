#!/usr/bin/python3
""" Module for the Shape abstract class and subclasses """

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class

    Args:
        ABC

    Returns:
        Nothing

    """

    @abstractmethod
    def area(self):
        """calculates the area of the shape.

            Returns:
                Default 0
        """

        return 0

    @abstractmethod
    def perimeter(self):
        """calculates perimeter of the shape.

            Returns:
                Default 0
        """

        return 0


class Circle(Shape):
    """Circle Class"""

    __radius = 0

    def __init__(self, radius=0):
        self.radius = radius

    @property
    def radius(self):
        """Gets private value of radius

            Returns:
                value of __radius
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets and validates value of private radius

            Returns:
                Nothing
        """

        if value < 0:
            value = abs(value)

        self.__radius = value

    def area(self):
        """overrides abstract method of area"""

        area = math.pi * self.radius * self.radius
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self):
        """overrides abstract method of preimeter"""

        perimeter = 2 * math.pi * self.radius
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


class Rectangle(Shape):
    """Rectangle Class"""

    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Gets private value of width

            Returns:
                value of __width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets and validates value of private attribute width

            Returns:
                Nothing
        """

        self.__width = value

    @property
    def height(self):
        """Getter for private attribute height

            Returns:
                value of __height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets and validates value of private attribute height

            Returns:
                Nothing
        """

        self.__height = value

    def area(self):
        """overrides abstract method of area"""

        area = self.width * self.height
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self) -> float:
        """overrides abstract method of perimeter"""

        perimeter = 2 * (self.width + self.height)
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


def shape_info(shape :Shape):
    """shape information function"""

    area = shape.area()
    perimeter = shape.perimeter()

    return {'area': area, 'perimeter': perimeter }
