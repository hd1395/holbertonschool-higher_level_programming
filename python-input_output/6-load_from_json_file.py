#!/usr/bin/python3
"""Defines a JSON file-reading function."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename) as text_file:
        return json.load(text_file)
