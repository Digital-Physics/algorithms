from counting_sort import counting_sort_for_radix_sort

# Radix, in the context of technology and computing, refers to the base of a number system. 
# It's the number of unique digits (including zero) used to represent numbers in a positional numeral system.
# In base 10, there are only 10 possible keys, and that's why Radix sort leverages counting sort (see notes in counting_sort.py).

def LSD_radix_sort(arr):
    """We will sort the list based on the least significant digit first, then sort on the next LSD, and so on.
    This works because counting sort is a stable sorting algorithm. Even though items based on the ones place
    will all get reshuffled in the next round, they will still keep their relative order if they have the same 10s digit.
    This analogy holds for subsequent sorting rounds as well."""
    max_num = max(arr) # this is for our while loop, not for our range of keys which we assume is 10, digits 0-9
    radix_sort_place = 1

    while max_num // radix_sort_place > 0: # this will loop for as many digits as we have in the longest number
        arr = counting_sort_for_radix_sort(arr, radix_sort_place)
        radix_sort_place *= 10

    return arr


def MSD_radix_sort(arr):
    """although it is more intuitive that this approach would work, and it represents how a human might do radix sort,
    the code is a little more convoluted because of recursion. we'd need to split the sorted ties into buckets and further
    sort them by the next MSD."""
    max_num = max(arr) 
    radix_sort_place = len(str(max_num)) - 1

    ...


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = LSD_radix_sort(arr)
    sorted_arr2 = MSD_radix_sort(arr)
    
    print("Sorted array is:", sorted_arr)
    print("Sorted array is:", sorted_arr2)