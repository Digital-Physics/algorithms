from typing import List

def gamingArray_naive(arr: List[int]) -> str:
    turn = "BOB"

    while True:
        arr = arr[:arr.index(max(arr))]
        if len(arr) == 0:
            return turn
        else:
            turn = "ANDY" if turn == "BOB" else "BOB"

def gamingArray(arr: List[int]) -> str:
    """traverse from left to right and count new maximums.
    the reason through odd/even for the two playing the game."""
    max = float("-inf")
    count = 0

    for i in range(len(arr)):
        if arr[i] > max:
            count += 1
            max = arr[i]

    return "ANDY" if count % 2 == 0 else "BOB"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()