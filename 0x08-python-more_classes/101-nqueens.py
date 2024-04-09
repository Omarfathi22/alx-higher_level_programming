#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    i = 0
    while i < n:
        board.append([' '] * n)
        i += 1
    return board


def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    r = 0
    while r < len(board):
        c = 0
        while c < len(board):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
            c += 1
        r += 1
    return solution


def xout(board, row, col):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        board (list): The current working chessboard.
        row (int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    c = col + 1
    while c < len(board):
        board[row][c] = "x"
        c += 1
    # X out all backwards spots
    c = col - 1
    while c >= 0:
        board[row][c] = "x"
        c -= 1
    # X out all spots below
    r = row + 1
    while r < len(board):
        board[r][col] = "x"
        r += 1
    # X out all spots above
    r = row - 1
    while r >= 0:
        board[r][col] = "x"
        r -= 1
    # X out all spots diagonally down to the right
    r = row + 1
    c = col + 1
    while r < len(board) and c < len(board):
        board[r][c] = "x"
        r += 1
        c += 1
    # X out all spots diagonally up to the left
    r = row - 1
    c = col - 1
    while r >= 0 and c >= 0:
        board[r][c] = "x"
        r -= 1
        c -= 1
    # X out all spots diagonally up to the right
    r = row - 1
    c = col + 1
    while r >= 0 and c < len(board):
        board[r][c] = "x"
        r -= 1
        c += 1
    # X out all spots diagonally down to the left
    r = row + 1
    c = col - 1
    while r < len(board) and c >= 0:
        board[r][c] = "x"
        r += 1
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return solutions

    c = 0
    while c < len(board):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)
        c += 1

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
