#!/bin/python3

import math
# import os
# import random
# import re
# import sys


def encryption(s: str) -> str:
    s = s.strip()
    length = len(s)
    lower_bound = math.floor(length**(1/2))
    upper_bound = math.ceil(length**(1/2)) # sometimes lower_bound + 1, sometimes they are equal
    
    if lower_bound*lower_bound == length:
        rows = lower_bound
        cols = lower_bound
    elif lower_bound*upper_bound >= length:
        rows = lower_bound
        cols = upper_bound
    elif upper_bound*upper_bound >= length:
        rows = upper_bound
        cols = upper_bound

    # print(rows, cols, length)
    # populate matrix
    matrix = [[s[i*cols + j] if i*cols + j < length else "" for j in range(cols)] for i in range(rows)] 
    # print(matrix)
    # encryption
    return " ".join(["".join(col) for col in zip(*matrix)])

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()