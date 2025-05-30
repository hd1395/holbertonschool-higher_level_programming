#!/usr/bin/python3
"""
Defines a Rectangle class.
"""


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0  # Class attribute to track number of instances
    print_symbol = "#"       # Class attribute, default is '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with optional width and height
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the count of instances

    @property
    def width(self):
        """
        Gets the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets and validates the width of the Rectangle
        Throws:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets and validates the height of the Rectangle
        Throws:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle
        If width or height is 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the Rectangle using
        the print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        result_str = []
        for i in range(self.__height):
            line = "".join(str(self.print_symbol) for _ in range(self.__width))
            result_str.append(line)
        return "\n".join(result_str)

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Prints a message when a Rectangle instance is deleted
        and decrements the instance counter.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the count of instances

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.
        Returns rect_1 if both have the same area value.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
