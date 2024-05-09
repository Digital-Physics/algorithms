from typing import List
    
def min_job_assignment(matrix):
    """
    Incomplete implementation of the Hungarian algorithm for a matrix.
    
    each worker (row) needs a (job) column in your matrix. 
    the matrix contains a cost or time for worker i to do job j. 
    The goal is to minimize it.
    in other words, minimize the trace of a matrix if you 
    are allowed to permute the rows and columns... not that
    this algorithm does that. This is a specific example of the
    Hungarian algorithm.
    https://en.wikipedia.org/wiki/Hungarian_algorithm
    """
    n = len(matrix)

    # Step 1: Subtract the smallest element from each row, leaving an extra, non-optimal cost for each job for worker i
    # note: this can also handle negative numbers turning every number into a non-negative
    for i in range(n):
        min_val = min(matrix[i])
        matrix[i] = [element - min_val for element in matrix[i]]

    # it's possible we have the right 0s lining up in different columns at this point

    # Step 2: Subtract the smallest element from each column, leaving an extra, non-optimal cost to assign each worker to job j
    for j in range(n):
        min_val = min(matrix[i][j] for i in range(n))
        for i in range(n):
            matrix[i][j] -= min_val

    # Step 3: 
    row_covered = [False] * n 
    col_covered = [False] * n
    num_covered = 0 

    ...

    return 0


cost_matrix = [
    [8, 4, 7],
    [5, 2, 3],
    [9, 4, 8]
]

print(min_job_assignment(cost_matrix))  