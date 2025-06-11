import csv
import json
""" 
Module that provides a function that reads data from a CSV file
and converts it to JSON format into a file
"""


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and converts it to a JSON file (data.json).

    Args:
        csv_filename: The path to the csv file.

    Returns:
        True if conversion is successful, False otherwise.
    """
    try:
        with open(csv_filename, mode='r', newline='', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
