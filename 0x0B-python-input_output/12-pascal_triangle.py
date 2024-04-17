#!/usr/bin/python3
"""
This module contains a function to generate Pascal's triangle.
"""


def pascal_triangle(n):
    """
    Generates Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: List of lists representing Pascal's triangle up to nth row.
              Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize with the first row
    for i in range(1, n):
        row = [1]  # Start each row with 1
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])  # Calculate the value based on the previous row
        row.append(1)  # End each row with 1
        triangle.append(row)  # Add the row to the triangle
    return triangle
