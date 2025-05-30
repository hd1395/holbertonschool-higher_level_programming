#!/usr/bin/python3

"""'MyInt' Module"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, v):
        return self.value != v

    def __ne__(self, v):
        return self.value == v
