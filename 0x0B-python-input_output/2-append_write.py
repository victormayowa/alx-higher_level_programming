#!/usr/bin/python3
'''
append to the file
'''


def append_write(filename="", text=""):
    '''
    Appends a string to the end of a text file (UTF8) and returns
    Args:
        filename (str): Name of the file to append
        text (str): Text content to be appended to the file

    Returns:
        int: Number of characters added to the file
    '''

    with open(filename, "a", encoding="utf-8") as file:
        char = file.write(text)
        return char
