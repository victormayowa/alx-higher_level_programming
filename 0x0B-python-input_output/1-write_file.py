#!/usr/bin/python3

def write_file(filename="", text=""):
    '''
    Writes a string to a text file (UTF8) and returns the number of characters written

    Args:
        filename (str): Name of the file to write
        text (str): Text content to be written to the file

    Returns:
        int: Number of characters written to the file
    '''

    with open(filename, mode = "w", encoding="utf-8") as file:
        char = file.write(text)
        return char
