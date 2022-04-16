# time: worst = O(N**2); best = O(nlogn) when pivot divides array in half; avg: O(nlogn)
# space: O(logn) for the recusive call stack (if we always choose smaller subarray first to keep call stack low)
# space note: nothing added for sorting in space
#
def quickSort(array):
    # helper function sorts array in place but doesn't return anything
    quick_sort_helper(array, 0, len(array) - 1)
    return array


# helper is helpful since it allows us to pass in boundaries of subarray
def quick_sort_helper(array, start_idx, end_idx):
    # quick sort uses the pivot number as a dividing line
    # swap l and r numbers if needed. then swap in pivot. then one pivot point is sorted
    # recursively repeat on two new subarrays, going with smaller one first

    # if lenght is 1 on subarray, then it is sorted
    # base case
    if start_idx >= end_idx:
        return  # to exit

    pivot_idx = start_idx  # there are other variations for choosing pivot, but this allows us to mindlessly swap after while loop
    l_idx = start_idx + 1
    r_idx = end_idx

    # pivot stays to the side while you swap
    while r_idx >= l_idx:
        if array[l_idx] > array[pivot_idx] and array[r_idx] < array[pivot_idx]:
            array[l_idx], array[r_idx] = array[r_idx], array[l_idx]
        if array[l_idx] <= array[pivot_idx]:
            l_idx += 1
        if array[r_idx] >= array[pivot_idx]:
            r_idx -= 1

    # then pivot is swapped into place
    # note: the r_idx will always be less than the pivot num at the end of while; that's why we swap
    array[pivot_idx], array[r_idx] = array[r_idx], array[pivot_idx]
    pivot_idx = r_idx

    # recursive call on two subarrays, w/ preference on the shorter array (for space complexity)
    l_array_length = (pivot_idx - 1) - start_idx
    r_array_length = end_idx - (pivot_idx + 1)

    if l_array_length < r_array_length:
        quick_sort_helper(array, start_idx, (pivot_idx - 1))
        quick_sort_helper(array, (pivot_idx + 1), end_idx)
    else:
        quick_sort_helper(array, (pivot_idx + 1), end_idx)
        quick_sort_helper(array, start_idx, (pivot_idx - 1))

