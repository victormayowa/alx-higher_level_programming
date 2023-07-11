#!/usr/bin/python3

def read_file(filename=""):
    '''
    Reads a text file and prints its contents to stdout

    Args:
        filename (str): Name of the file to read

    Returns:
        None
    '''

    if not isinstance(filename, str):
        raise TypeError("filename must be a string")

    with open(filename, "r") as file:
        print(file.read(), end='')
