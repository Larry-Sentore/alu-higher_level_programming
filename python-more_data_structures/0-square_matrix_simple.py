#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num * num)
        result.append(new_row)
    return result
