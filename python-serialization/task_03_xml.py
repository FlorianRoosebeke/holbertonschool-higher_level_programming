#!/usr/bin/python3
"""Module for basic serialization with JSON."""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a dictionary."""
    tree = ET.parse(filename)
    root_deserialize = tree.getroot()
    result = {}
    for child in root_deserialize:
        result[child.tag] = child.text
    return result
