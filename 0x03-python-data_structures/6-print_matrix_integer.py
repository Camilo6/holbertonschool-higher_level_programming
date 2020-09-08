#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return None
    if len(matrix[0]) == 0:
        print()
        return

    for row in range(0, len(matrix[:])):
        for idx in matrix[row]:
            print("{:d}".format(idx), end="")
            row_size = len(matrix[row]) - 1
            row_index = matrix[row].index(idx)
            if row_index != row_size:
                print(' ', end="")
            else:
                print()
