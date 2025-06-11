#!/usr/bin/python3
"""
Module that provides functions to serialize a Python dictionary to a JSON file
and deserialize the JSON file to recreate the Python Dictionary..
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize and saves data to the specified file.

    Args:
        data: The dictionary to serialize.
        filename: The name of the file to save the JSON data.
    """
    with open(filename, 'w') as text_file:
        json.dump(data, text_file)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from the specified file.

    Args:
        filename: The name of the JSON file to read from.

    Returns:
        The deserialized dictionary.
    """
    with open(filename, 'r') as text_file:
        return json.load(text_file)
