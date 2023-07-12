#!/usr/bin/python3
''' load json file in read mode and stores it'''
import json
''' import json'''
def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): Name of the JSON file.

    Returns:
        object: Object created from the JSON file.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
    '''
    does not return anything but stores process in address
    can be accessed but variable storage
    '''
