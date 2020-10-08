#!/usr/bin/python3
"""
This module based in task 14
"""


def pascal_triangle(n):
    """This function returns a list of lists
    of integers representing the Pascal’s triangle of n:
    """

    if n <= 0:
        lista = []
        return lista
    else:
        lista = []
        for i in range(n):
            lista.append([1] * (i+1))
            for j in range(1, len(lista[i])-1):
                lista[i][j] = lista[i - 1][j] + lista[i - 1][j - 1]
        return lista
