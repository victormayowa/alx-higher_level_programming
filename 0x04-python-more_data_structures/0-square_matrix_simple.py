#!/usr/bin/python3
def square_matrix_simple(matrix):
    # Create a new matrix with the same size as the input matrix
    new_matrix = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # Compute the square value of each element in the input matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[i][j] = matrix[i][j] ** 2

    # Return the new matrix
    return new_matrix
