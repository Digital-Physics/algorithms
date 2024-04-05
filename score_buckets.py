from typing import List

def countSort(arr: List[List[str]]) -> str:
    """we'll take advantage of the fact that integer to key off of for sorting is between 0 and 100.
    sort should be stable, so order is preserved based on ingestion order when tied on score and in same bucket."""

    mid_idx = len(arr)//2  # n is even so we could have just /2

    # score buckets: take advantage of the fact that integer to key off of for sorting is between 1 and 10.
    # print([["_"]*11]) # ok; print([[]*11]) # wrong
    # buckets = [[] for _ in range(11)]  # 11 so we can use the s from 0 to 10; wrong it's -10 <= s <= 10
    # buckets = [[] for _ in range(21)]  # 21 so we can use the s from 0 to 20, where each x is shifted right +10
    buckets = [[] for _ in range(101)]  # scores are 0 to 100, strings are 1 to 10 in length

    for i, sample in enumerate(arr):
        score, string = sample[0], sample[1]
        buckets[int(score)].append(string if i >= mid_idx else "-")

    # don't forget to remove empty buckets with truthy check
    return " ".join([" ".join(bucket) for bucket in buckets if bucket])

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
    print(countSort(arr))