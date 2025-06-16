from typing import List
import math

def zeroOut(matrix: List[List[int]]):
    # could just go through matrix once, but we go through twice
    # could use less memory by making the first element in rows or cols 0 instead of using additional memory
    row_prods = [math.prod(row) for row in matrix]
    col_prods = [math.prod(col) for col in zip(*matrix)]

    for i, val in enumerate(row_prods):
        if val == 0:
            matrix[i] = [0] * len(matrix[0])
    
    for j, val in enumerate(col_prods):
        if val == 0:
            for i in range(len(matrix)):
                matrix[i][j] = 0
    
    return matrix


if __name__ == "__main__":

    my_matrix = [
        [1, 2, 3],
        [4, 5, 0],
        [7, 8, 9]
        ]

    print(zeroOut(my_matrix))

