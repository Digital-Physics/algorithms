# break down the array and then merge-sort it back together, like a messy riffle shuffle
# time: O(n*log(n))
# space: O(n*log(n)) not sorting in place, not mutating; could do in O(n) time if we worked w/ indices instead of actual lists
def mergeSort(array):
    # the top level just splits; the helper function merges
    if len(array) == 1:
        return array

    mid_idx = len(array) // 2
    l_array = array[:mid_idx]
    r_array = array[mid_idx:]

    # this is the key line to remember structure
    return merge_sorted(mergeSort(l_array), mergeSort(r_array))


def merge_sorted(l_arr, r_arr):
    sorted = [None for _ in range(len(l_arr) + len(r_arr))]

    curr_idx_l = 0
    curr_idx_r = 0
    sorted_idx = 0

    while curr_idx_l < len(l_arr) and curr_idx_r < len(r_arr):
        if l_arr[curr_idx_l] <= r_arr[curr_idx_r]:
            sorted[sorted_idx] = l_arr[curr_idx_l]
            curr_idx_l += 1
            sorted_idx += 1
        else:
            sorted[sorted_idx] = r_arr[curr_idx_r]
            curr_idx_r += 1
            sorted_idx += 1

    while curr_idx_l < len(l_arr):
        sorted[sorted_idx] = l_arr[curr_idx_l]
        curr_idx_l += 1
        sorted_idx += 1

    while curr_idx_r < len(r_arr):
        sorted[sorted_idx] = r_arr[curr_idx_r]
        curr_idx_r += 1
        sorted_idx += 1

    return sorted

# Clement goes through more complicated example that uses an auxiliary copy of the array to keep track of indices as opposed to new lists
# time: O(n*log(n))
# space: O(n)




