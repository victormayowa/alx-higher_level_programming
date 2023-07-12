#!/usr/bin/python3
'''  search and append after '''


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in each line of the file.
        new_string (str): Line of text to be inserted after each line
        containing the search string.

    Returns:
        None

    """
    lines = []
    with open(filename, 'r') as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, 'w') as file:
        file.writelines(lines)
