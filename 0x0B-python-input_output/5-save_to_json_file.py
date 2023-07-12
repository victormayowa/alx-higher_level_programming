#!/usr/bin/python3
''' save the json object in a file withe name as filename '''
import json
'''
import json
create a function with styled name
'''
def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: Object to be serialized to JSON.
        filename (str): Name of the file to write.

    Returns:
        None
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
    '''
    opens the file and dumps it inn an obj
    '''
