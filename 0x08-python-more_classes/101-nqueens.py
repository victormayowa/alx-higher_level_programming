#!/usr/bin/python3
"""
This module solves the N-Queens problem.
"""

import sys


def is_safe(board, row, col):
    """
    Checks if it is safe to place a queen at the given position on the board.
    Args:
        board (list): The current state of the board.
        row (int): The row index to check.
        col (int): The column index to check.
    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    """
    Recursive function to solve the N-Queens problem.
    Args:
        board (list): The current state of the board.
        row (int): The current row to consider.
        solutions (list): List to store the solutions.
    """
    if row == len(board):
        # Base case: All queens have been placed
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place a queen at the current position
            board[row][col] = 1

            # Recur for the next row
            solve_nqueens(board, row + 1, solutions)

            # Backtrack: Remove the queen from the current position
            board[row][col] = 0


def print_solutions(solutions):
    """
    Prints the solutions to the N-Queens problem.
    Args:
        solutions (list): List of solutions.
    """
    for solution in solutions:
        print(solution)


def nqueens(n):
    """
    Solves the N-Queens problem and prints the solutions.
    Args:
        n (int): The size of the chessboard and the number of queens.
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    print_solutions(solutions)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
