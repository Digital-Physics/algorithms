from typing import List

def counting_sort(array: List[int]) -> List[int]:
    """a stable sorting algorithm that works well for a small number keys that it will be sorted by.
    we work with a small range of integers here, but you could imagine tuples objects with one value being the key,
    and all the tuple values don't have too many possible keys."""

    # initialize our mutable counter array which starts with counts => PDF => CDF => insert index-updated CDF
    max_val = max(array)
    counter = [0] * (max_val + 1)

    # create PDF where x is the number (or letter) and y is the count or density
    for i in range(len(array)):
        counter[array[i]] += 1

    # create the cumulative count, the CDF
    for i in range(1, len(counter)):
        counter[i] = counter[i] + counter[i-1]

    output = [None for _ in range(len(array))]

    # start from end of original array (if you study the algo, you'll realize this is stable)
    for i in range(len(array) - 1, -1, -1):
        output[counter[array[i]] - 1] = array[i]
        counter[array[i]] -= 1

    return output

if __name__ == "__main__":
    print(counting_sort([2, 3, 0, 1, 1 , 2, 2, 4, 5, 2]))









