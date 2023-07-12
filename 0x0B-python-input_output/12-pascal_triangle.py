#!/usr/bin/python3
"""
12-pascal_triangle module

Provides a function to generate Pascal's triangle up to a given number of rows.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows in the Pascal's triangle.

    Returns:
        list: List of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)

    return triangle
