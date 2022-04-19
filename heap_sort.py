# time: O(n*log(n))
# space: O(1)
# one left part of array is a shrinking heap; the right side is growing sorted list; swap first and last, then sift down
def heapSort(array):
    # construct a max heap in O(n) in place
    build_max_heap(array)

    # swap first (greatest/root) and last node in range of heap
    # last node/item in array is now sorted
    # Sift Down new root node through heap (which is one item less) O(log(n))
    for end_idx in reversed(range(1, len(array))):
        array[0], array[end_idx] = array[end_idx], array[0]
        siftDown(0, end_idx - 1, array)

    return array


# A heap is a tree but it's organized in a list, instead of using tree/node class objects with .left and .right attributes
def build_max_heap(array):
    # time: O(n) constructing a min heap and removing the min is quicker than sorting and having BST retrieval
    # space: O(1) swaps of elements in array/heap done in place
    # use siftDown over siftUp since it is faster for majority of nodes (towards bottom)
    # you don't need to siftDown any leaf nodes so just start with the last parent in heap/tree
    # heap index property: min is 0 index, then l_idx = curr_idx * 2 + 1 and r_idx = curr_idx * 2 + 2
    last_parent_idx = ((len(array) - 1) - 1) // 2
    for curr_idx in reversed(range(last_parent_idx + 1)):  # +1 to include it in range
        siftDown(curr_idx, len(array) - 1, array)


# time: O(log(n))
# space: O(1)
# modified to take into account moving end_idx in Heap Sort
def siftDown(curr_idx, end_idx, heap_array):
    l_idx = curr_idx * 2 + 1

    while l_idx <= end_idx:
        r_idx = curr_idx * 2 + 2 if (curr_idx * 2 + 2 <= end_idx) else None

        if r_idx is not None and heap_array[r_idx] > heap_array[l_idx]:
            potential_swap = r_idx
        else:
            potential_swap = l_idx

        if heap_array[potential_swap] > heap_array[curr_idx]:
            heap_array[potential_swap], heap_array[curr_idx] = heap_array[curr_idx], heap_array[potential_swap]
            potential_swap, curr_idx = curr_idx, potential_swap
            l_idx = curr_idx * 2 + 1
        else:
            return

# .sift_up() not neede because we aren't inserting
# .peek() not needed either
# .insert() not needed either
# .remove() not needed either
