#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Args:
        text (str): The text to be indented.

    Raises:
        TypeError: If text is not a string.

    Examples:
        >>> text_indentation("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \
        Quonam modo? Utrum igitur tibi litteram videor an totas paginas commovere? \
        Non autem hoc: igitur ne illud quidem. Fortasse id optimum, sed ubi illud: \
        Plus semper voluptatis?")
        Lorem ipsum dolor sit amet, consectetur adipiscing elit.

        Quonam modo?

        Utrum igitur tibi litteram videor an totas paginas commovere?

        Non autem hoc:
        igitur ne illud quidem.

        Fortasse id optimum, sed ubi illud:
        Plus semper voluptatis?
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuations = [".", "?", ":"]
    indented_text = ""
    for char in text:
        indented_text += char
        if char in punctuations:
            indented_text += "\n\n"

    print(indented_text.strip())
