#!/usr/bin/python3
"""Island perimeter computing module.
"""


def island_perimeter(board):
    """
    Create a function def island_perimeter(board):
    that returns the perimeter of the island described in board
    """
    perimeter = 0
    if type(board) != list:
        return 0
    n = len(board)
    for i, r in enumerate(board):
        m = len(r)
        for j, k in enumerate(r):
            if k == 0:
                continue
            edges = (
                i == 0 or (len(board[i - 1]) > j and board[i - 1][j] == 0),
                j == m - 1 or (m > j + 1 and r[j + 1] == 0),
                i == n - 1 or (len(board[i + 1]) > j and board[i + 1][j] == 0),
                j == 0 or r[j - 1] == 0,
            )
            perimeter += sum(edges)
    return perimeter
