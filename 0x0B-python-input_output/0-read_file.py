#!/usr/bin/python3

def read_file(filename=""):
    '''
    Reads a text file and prints its contents to stdout

    Args:
        filename (str): Name of the file to read

    Returns:
        None
    '''
    with open(filename, "r") as file:
        r = file.read()
        print(r, end='')
