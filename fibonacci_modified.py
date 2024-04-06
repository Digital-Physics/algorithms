from typing import Dict
import sys
sys.set_int_max_str_digits(0)  # don't use scientific notation for large int

def fibonacciModified_v1(t1: int, t2: int, n: int):
    for _ in range(n - 2):
        t1, t2 = t2, t1 + t2**2
    
    return t2

def fibonacciModified(t1: int, t2: int, n: int, memo: Dict[int, int] = {}):
    """the default argument, memo, is a mutable dictionary, so once populated, 
    any other function call can use it, even if it was on a far away branch.
    those calls won't get fresh, empty dictionaries, they all get the same mutating object. 
    this is easier than sharing a common state through a class object or having
    a dictionary sit outside the function"""
    if n == 1:
        return t1
    if n == 2:
        return t2

    if n not in memo:
        memo[n] = fibonacciModified(t1, t2, n - 2) + (fibonacciModified(t1, t2, n - 1) ** 2)

    return memo[n]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()