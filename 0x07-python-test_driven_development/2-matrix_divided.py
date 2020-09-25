#!/usr/bin/python3
"""This module is from task 2"""
error_v = "matrix must be a matrix (list of lists) of integers/floats"


def matrix_divided(matrix, div):
    """"This function that divides all elements of a matrix"""
    if matrix == [] or not isinstance(matrix, list):
        raise TypeError(error_v)
    if not all(isinstance(item, list) for item in matrix):
        raise TypeEror("Each row of the matrix must have the same size")
    if len(matrix[0]) == 0:
        raise TypeError(error_type)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    matrix_quotient = []
    for row in matrix:
        item = 0
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if isinstance(item, (int, float)):
                item = int(item)
            else:
                raise TypeError(error_type)
    matrix_quotient = [[round(item / div, 2)
                        for item in row] for row in matrix]
    return(matrix_quotient)
