from typing import List

def maxMin(k: int, arr: List[int]) -> int:
    arr.sort()

    mini = float("inf")

    for i in range(len(arr) - k + 1):
        mini =min(arr[i+k-1] - arr[i], mini)

    return mini


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()