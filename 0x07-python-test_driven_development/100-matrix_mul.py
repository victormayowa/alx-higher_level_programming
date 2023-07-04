#!/usr/bin/python3
"""
Matrix multiplication - only Matrix product (two matrices)
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result

    Args:
        m_a (list): First matrix as a list of lists of integers or floats
        m_b (list): Second matrix as a list of lists of integers or floats

    Returns:
        list: Resulting matrix as a list of lists of integers or floats

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists,
                   or if an element in the matrices is not an integer or a float,
                   or if the rows in m_a or m_b are not of the same size
        ValueError: If m_a or m_b is empty or if the matrices cannot be multiplied
    """

    # Validate input matrices
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if any(not all(isinstance(num, (int, float)) for num in row) for row in m_a) or \
       any(not all(isinstance(num, (int, float)) for num in row) for row in m_b):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    # Check if matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            elem = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row.append(elem)
        result.append(row)

    return result
