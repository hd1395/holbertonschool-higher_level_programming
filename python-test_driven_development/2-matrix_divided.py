#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix by a number.
"""


def matrix_divided(matrix, div):
    """
      Divides all elements of a matrix by a number.

    Args:
    matrix (list of lists): A matrix (list of lists) of integers/floats.
    div (int or float): The number to divide by.

    Returns:
    list:A new matrix with elments divided and rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers/floats.
    TypeError: If rows of matrix are not the same size.
    TypeError: If div is not a number.
    ZeroDivisionError: If div is zero.
    """
    row_len = 0
    size_error_msg = "Each row of the matrix must have the same size"
    type_err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(type_err_msg)

    for row in matrix:
        if not row or not isinstance(row, list):
            raise TypeError(type_err_msg)
        if row_len != 0 and len(row) != row_len:
            raise TypeError(size_error_msg)

        for num in row:
            if not isinstance(num, (float, int)):
                raise TypeError(type_err_msg)
        row_len = len(row)

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_list = list(map(lambda row: list(map(lambda n: round(n / div, 2), row))
                       , matrix))
    return (new_list)
