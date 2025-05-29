#!/usr/bin/python3
"""BaseGeometry module.

Defines a class BaseGeometry, and some methods.
"""


class BaseGeometry():
  """BaseGeometry class."""
  
  def area(self):
    """Raises an Exception."""
    raise Exception("area() is not implemented")
  
  def integer_validator(self, name, value):
     """Validates an integer."""
    if type(value) is not int:
      raise TypeError(f"{name} must be an integer")
    if value <= 0:
      raise ValueError(f"{name} must be greater than 0")
