#!/usr/bin/python3
import xml.etree.ElementTree as ET

"""
Module that provides functions to serialize a Python dictionary into XML format
and save it to a file, and to deserialize XML back into a dictionary.
"""


def serialize_to_xml(dictionary, filename):
    """
    Serializes a dictionary into XML and saves it to a file.

    Args:
    dictionary: The dictionary to serialize.
    filename: The name of the file to save the XML.

    """
    xml_root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(xml_root, key)
        child.text = str(value)

    tree = ET.ElementTree(xml_root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Reads the XML data from a file and returns a deserialized dictionary.

    Parameters:
    filename: The name of the file to read the XML from.

    Returns:
    dictionary for the deserialized XML data.
    """
    tree = ET.parse(filename)
    xml_root = tree.getroot()
    result_dict = {}
    for child in xml_root:
        result_dict[child.tag] = child.text

    return result_dict

