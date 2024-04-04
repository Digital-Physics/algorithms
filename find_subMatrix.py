#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

def gridSearch(G: List[str], P: List[str]) -> str: # output is like a bool but a str "YES" or "NO"
    for i in range(len(G)):
        for j in range(len(G[0])):
            if isTotalMatch(i, j, G, P):
                return "YES"
    
    return "NO"

def isTotalMatch(i, j, G, P):
    for i_d in range(len(P)):
        for j_d in range(len(P[0])):
            if i + i_d >= len(G) or j + j_d >= len(G[0]):
                return False
            if G[i + i_d][j + j_d] != P[i_d][j_d]:
                return False
    
    return True

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip()) # test examples

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0]) # rows in big matrix

        C = int(first_multiple_input[1]) # cols in big matrix (not used)

        G = [] # grid for "grid search"

        for _ in range(R):
            G_item = input() # str length C
            G.append(G_item)

        second_multiple_input = input().rstrip().split() # pattern matrix

        r = int(second_multiple_input[0]) # small matrix row count

        c = int(second_multiple_input[1]) # col count

        P = [] # pattern

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()