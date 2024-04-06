import os
import math

def andProduct_naive(a: int, b: int) -> int:
    total = a # easier init than making a seq of 1111 equal to the length of the first number
    
    for i in range(a + 1, b):
        total &= i  # bitwise and

    return total

def andProduct(a: int, b: int) -> int:
    # the difference bits will all turn over, so there will always be at least a 0
    diff_bits = math.floor(math.log(b-a, 2)) + 1
    
    a = a >> diff_bits
    b = b >> diff_bits

    c = a & b

    c = c << diff_bits

    return c

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    for n_itr in range(n):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = andProduct(a, b)
        print(result)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
