from typing import List

def counting_sort(array: List[int]) -> List[int]:
    """a stable sorting algorithm that works well for a small amount of keys it will be sorted by.
    we work with a small range of integers here where the item to be sorted is the key, 
    but you could imagine tuples objects with one value being the key. This would be a good sorting algorithm
    for long lists without too many possible keys. If the number of keys equals the number of 
    items to sort, the time complexity jumps from O(n + max_val), something linear when the size of the max_val
    is held constant, to quadratic."""

    # initialize our mutable counter array which which evolves: counts => PDF => CDF => decremented CDF
    max_val = max(array)
    counter = [0] * (max_val + 1)

    # create a discrete PDF of integers (or letters or enumerable keys)
    for i in range(len(array)):
        counter[array[i]] += 1  # radix_sort_place will be 1, 10, 100, 1000, etc.

    # create the cumulative count, the discrete CDF
    for i in range(1, len(counter)):
        counter[i] = counter[i] + counter[i-1]

    # initialize output that we'll populate
    output = [None for _ in range(len(array))]

    # start from end of original array and work backwards to populate output array 
    # if you think about this algorithm, you'll realize this makes the sorting stable) 
    for i in range(len(array) - 1, -1, -1):
        output[counter[array[i]] - 1] = array[i]
        counter[array[i]] -= 1

    return output


def counting_sort_for_radix_sort(array: List[int], radix_sort_place: int = 1) -> List[int]:
    """a stable sorting algorithm that works well for a small amount of keys it will be sorted by.
    we work with a small range of integers here where the item to be sorted is the key, 
    but you could imagine tuples objects with one value being the key. This would be a good sorting algorithm
    for long lists without too many possible keys. If the number of keys equals the number of 
    items to sort, the time complexity jumps from O(n + max_val), something linear when the size of the max_val
    is held constant, to quadratic. To understand why we have the radix sort variable, read radix_sort.py"""

    # initialize our mutable counter array which which evolves: counts => PDF => CDF => decremented CDF
    max_val = max(array) if radix_sort_place == 1 else 9  # we assume radix sort is done on base 10 numbers
    counter = [0] * (max_val + 1)

    # create a discrete PDF of integers (or letters or enumerable keys)
    for i in range(len(array)):
        counter[(array[i]//radix_sort_place) % 10] += 1  # radix_sort_place will be 1, 10, 100, 1000, etc.

    # create the cumulative count, the discrete CDF
    for i in range(1, len(counter)):
        counter[i] = counter[i] + counter[i-1]

    # initialize output that we'll populate
    output = [None for _ in range(len(array))]

    # start from end of original array and work backwards to populate output array 
    # if you think about this algorithm, you'll realize this makes the sorting stable) 
    for i in range(len(array) - 1, -1, -1):
        output[counter[(array[i]//radix_sort_place) % 10] - 1] = array[i]
        counter[(array[i]//radix_sort_place) % 10] -= 1

    return output

if __name__ == "__main__":
    print(counting_sort([2, 3, 0, 1, 1 , 2, 2, 4, 5, 2]))









