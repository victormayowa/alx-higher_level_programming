#!/usr/bin/python3
'''
jsonn serialization
'''


def class_to_json(obj):
    """
    Returns the dictionary description with a simple data structure
    for JSON serialization of an object.

    Args:
        obj: Instance of a Class.

    Returns:
        dict: Dictionary description of the object
        with a simple data structure.
    """
    return obj.__dict__
    '''
    returns the description witha simple data structure in form of list,
    integer and boolean for json serialization of an obje
    '''
