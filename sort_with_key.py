# import math
# import os
# import random
# import re
# import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0]) # athletes

    m = int(nm[1]) # stats

    arr = []

    for _ in range(n):
        # arr.append(list(map(int, input().rstrip().split())))
        arr.append([int(val) for val in input().split(" ")]) 

    k = int(input())

    print(*[" ".join([str(val) for val in list_of_stats]) for list_of_stats in sorted(arr, key=lambda x: x[k])], sep="\n")