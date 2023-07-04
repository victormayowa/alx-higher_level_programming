#!/usr/bin/python3
"""Module to multiply 2 matrices using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function to multiply 2 matrices using NumPy

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        numpy.ndarray: The product of the two matrices.

    Raises:
        ValueError: If m_a or m_b is empty or not a rectangle.
        TypeError: If m_a or m_b is not a list of lists containing only integers or floats.
        ValueError: If m_a and m_b cannot be multiplied.

    """
    # Convert the input matrices to NumPy arrays
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    # Perform the matrix multiplication using the @ operator (Python 3.5+)
    result = arr_a @ arr_b

    return result.tolist()  # Convert the NumPy array back to a regular list of lists
