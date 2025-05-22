#!/usr/bin/python3
"""
This module defines a Square class with the following properties
1- size
2- position

And the following methods
1- area - calculates the area of the square
2- my_print - print square using the character '%'

"""


class Square:
    """
    Square class with size attribute,display method, and area calculation.

    Attributes:
        __size (int): The size of the square (private).
    """

    def __init__(self, size=0, position=(0,0)):
        """
        Initializes a new Square instance with a given size.

        Args:
            size (int): The size of the square (default is 0).
            position (tuple): The position(x, y)of the square(default is(0,0)

        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Gets the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets and validates the size of the square.

        Args:
            value (int): The new value of size.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.

        Returns:
            tuple: The position of the square (x, y).
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets and validates the position of the square.

        Args:
            value (tuple): The new position (x, y).

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
            ValueError: If any element of value is less than or equal to 0.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square using the '#' character, considering the position.
        If size is 0,prints an empty line.
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
