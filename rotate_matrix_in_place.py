from typing import List

def rotate(matrix: List[List[int]]) -> None:
    """
    Rotate n x n image clockwise 90 degrees. 
    Do not return anything; modify matrix in-place instead.
    We will transpose it and then reverse the rows.
    """
    # transpose 
    # iterate over upper triangular matrix and swap w/ lower triangular matrix
    for i in range(1, len(matrix)): # the diagonal won't change
        for j in range(i, len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # reverse rows
    for i in range(len(matrix)):
        matrix[i] = matrix[i][::-1]  # or matrix[i].reverse(); but not reversed(matrix[i]) which gives us an iterator

    # or 
    # for row in matrix:
    #     row[:] = row[::-1] # but not row = row[::-1]

