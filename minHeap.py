# A heap is a tree but it's organized in a list, not using tree/node class objects with children
# siftDown, siftUp, peek, remove, and insert methods.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # time: O(n) constructing a min heap and removing the min is quicker than sorting and having BST retrieval
    # space: O(1) swaps of elements in array/heap done in place
    def buildHeap(self, array):
        # use siftDown over siftUp since it is faster for majority of nodes (towards bottom)
        # last parent in tree is needed
        # you don't need to siftDown any leaf nodes so just start with the last parent in heap/tree
        # heap index property: min is 0 index, then l_idx = curr_idx * 2 + 1 and r_idx = curr_idx * 2 + 2
        last_parent_idx = ((len(array)-1)-1)//2
        for curr_idx in reversed(range(last_parent_idx + 1)):  # +1 to include it in range
            self.siftDown(curr_idx, array)
        return array  # for init method

    # time: O(logn)
    # space: O(1)
    def siftDown(self, curr_idx, heap):  # (in a min heap, not a max heap)
        l_idx = curr_idx * 2 + 1

        while l_idx <= len(heap) - 1:
            r_idx = curr_idx * 2 + 2
            if r_idx > len(heap) - 1:
                r_idx = None

            if r_idx is not None and heap[r_idx] < heap[l_idx]:
                potential_swap = r_idx
            else:
                potential_swap = l_idx

            if heap[potential_swap] < heap[curr_idx]:
                heap[potential_swap], heap[curr_idx] = heap[curr_idx], heap[potential_swap]
                potential_swap, curr_idx = curr_idx, potential_swap
                l_idx = curr_idx * 2 + 1
            else:
                break

    # time: O(logn)
    # space: O(1)
    def siftUp(self, curr_idx, heap):  # (in a min heap)
        parent_idx = (curr_idx - 1) // 2
        # do iterative instead of recursion
        while curr_idx > 0 and heap[parent_idx] > heap[curr_idx]:
            heap[parent_idx], heap[curr_idx] = heap[curr_idx], heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

    # time: O(1)
    # space: O(1)
    def peek(self):
        return self.heap[0]

    # time: O(logn)
    # space: O(1)
    def remove(self):  # (the top of the heap) (and return it)
        # (since heap not sorted, it is not meant for quick removal of other values)
        # swap first/top and last and then remove last(which was top) before siftDown on temp top
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        removed_value = self.heap.pop()
        self.siftDown(0, self.heap)
        return removed_value

    # time: O(logn)
    # space: O(1)
    def insert(self, value):
        # add val to the end of the heap tree, and then sift it up into place
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)
        