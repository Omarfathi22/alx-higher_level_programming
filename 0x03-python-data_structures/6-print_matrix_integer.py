#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    row_index = 0
    while row_index < len(matrix):
        col_index = 0
        while col_index < len(matrix[row_index]):
            print("{:d}".format(matrix[row_index][col_index]), end="")
            if col_index != len(matrix[row_index]) - 1:
                print(" ", end="")
            col_index += 1
        print()
        row_index += 1
