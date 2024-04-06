from typing import List

def pylons(k: int, arr: List[int]) -> int:
    last_pylon = -1 # if you reach this, you didn't find a pylon and return -1
    pylon_idx = k - 1 # best search location to start with
    counter = 0
    covered = -1 # covered through this index

    while covered < len(arr) - 1:  
        if pylon_idx == last_pylon:
            return -1
        elif arr[pylon_idx] == 1:
            counter += 1
            last_pylon = pylon_idx
            covered = pylon_idx + (k - 1)
            pylon_idx = min(covered + k, len(arr) - 1)
        else:
            pylon_idx -= 1
    
    return counter

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pylons(k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()