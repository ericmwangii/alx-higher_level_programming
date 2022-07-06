#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square_matrix = []
    for i in matrix:
        square_matrix.append([c**2 for c in i])
    return square_matrix
