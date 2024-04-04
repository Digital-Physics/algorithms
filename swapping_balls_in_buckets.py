#!/bin/python3
# import math
import os
from typing import List
# import random
# import re
# import sys

# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
def organizingContainers(container: List[List[int]]) -> str:
    """The transformations are matrix additions. 
    [[1, 0, 0, -1], [0, 0, 0, 0], [-1, 0, 0, 1], [0, 0, 0, 0]] is one allowable matrix addition 
    (assuming the first bucket 0 has type 2 >= 1 & bucket 2 has type 0 >= 1).
    The sum of the balls will need to match in the end, but the buckets don't have a designated type,
    so the solution will be not need to be a diagonal matrix, just a situation where every row and column 
    has only one value, almost like a permutation matrix, just with ball counts > 1 usually.
    One constraint, that turns out to be sufficient for determining if it is possible, is sum(balls in bucket i at init) will have to 
    equal a sum(sorted bucket j at end) because bucket ball count will remain constant with every swap. 
    So 10,7,8 bucket counts will have to end up as -10-,7--,--8 or --10,7--,-8- or any of the 3! sorts.
    So to sort before comparing them, we are increasing our chance of matching by 3! In other words,
    sorting before comparing is equivalent to not sorting and checking against all permutations/mappings."""
    bucket_ball_totals = sorted([sum(row) for row in container])
    ball_type_totals = sorted([sum(col) for col in zip(*container)])

    if all((bucket_ball_totals[i]==ball_type_totals[i] for i in range(len(bucket_ball_totals)))):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()