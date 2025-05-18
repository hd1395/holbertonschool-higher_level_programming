#!/usr/bin/python3
"""
This module provides a function to print a text with 2 new lines after
each '.', '?', and ':' characters.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    start = 0

    for i, char in enumerate(text):
        if char in delimiters:
            segment = text[start:i+1].strip()
            print(segment, end="\n\n")
            start = i + 1

    if start < len(text):
        remaining = text[start:].strip()
        if remaining:
            print(remaining, end="")
