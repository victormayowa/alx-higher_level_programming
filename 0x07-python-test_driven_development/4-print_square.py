#!/usr/bin/python3

def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): The size length of the square.

    Raises:
        TypeError: If size is not an integer.
                   If size is a float and is less than 0.
        ValueError: If size is less than 0.

    Examples:
        >>> print_square(4)
        ####
        ####
        ####
        ####

        >>> print_square(10)
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########
        ##########

        >>> print_square(0)

        >>> print_square(1)
        #

        >>> try:
        ...     print_square(-1)
        ... except Exception as e:
        ...     print(e)
        size must be >= 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
