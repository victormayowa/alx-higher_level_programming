#!/usr/bin/python3

def append_write(filename="", text=""):
    '''
    Appends a string to the end of a text file (UTF8) and returns
    Args:
        filename (str): Name of the file to append
        text (str): Text content to be appended to the file

    Returns:
        int: Number of characters added to the file
    '''
    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
