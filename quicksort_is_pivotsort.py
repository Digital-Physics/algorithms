from typing import List

# usually log(n) unless you pick pivots at the extreme and don't really split things close to in-half
# if it is sorted, and you choose the last element to pivot on, it's going to be O(n**2)... it's more like insertion sort at this point.
def quicksort(arr: List[int]) -> List[int]:
    """in-place swapping.
    set pivot element to last element, by convention. (hopefully it isn't sorted or else your last element won't be close to the middle.)
    from the outside (-1 to avoid sort) in, increment and decrement pointers low/i and high/j.
    i is looking for a number > pivot to swap; j is looking for number < pivot to swap. (left side small nums; right side large nums)
    once pointers i and j cross or equal, swap in place the low one which is a number > pivot and pivot. pivot is in place. 
    the remaining array is partitioned into higher and lower than pivot.
    base case: when the len(arr) coming in is 1 (low == high), do nothing, the list is already sorted.

    This is a helpful way to think about the recursion, but there are no nested lists, only swapping:

    [[1], 2, 3, [5, 4]] => [1, 2, 3, [5, 4]]
    [1, 2, 3, [5, 4]] => [1, 2, 3, 4, [5]]
    => [1, 2, 3, 4, 5]

    recursively call quicksort_helper(arr, left idx, right idx)
    recursively call quicksort_helper(arr, left idx, right idx)
    """

    # assume they won't give you the indexes you'll work with; we can make that function. and call it for the first time
    def quicksort_helper(arr, low, high):
        # base case: no more swaps needed for this (sub)array
        if low >= high:
            return
        
        # else, recursive call
        partition_pos = partition_via_swaps2(arr, low, high)
        quicksort_helper(arr, low, partition_pos - 1) # this function only swaps or does nothing on the last step
        quicksort_helper(arr, partition_pos + 1, high)

    def partition_via_swaps(arr, left, right): # and return the sorted ending pivot index
        # note: you need to pass in the index, because low is not always 0 and high is not alway len(arr) - 1
        i = left
        j = right - 1
        pivot_val = arr[right]

        while i < j:
            # looking for first swap index, obeying bounds
            while arr[i] < pivot_val and i < right:
                i += 1

            # note: j can go past i within each while loop step, but not pass the end. we'll check whether they crossed before we swa in the next step.
            while arr[j] > pivot_val and j > left: 
                j -= 1

            # swap if we didn't find pointers in the other side's territory (we don't want to swap good ones out of the left and right sides)
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # swap pivot val and arr[i]
        # don't think we need extra line of code shown in https://www.youtube.com/watch?v=9KBwdDEwal8, but we actually might (kthLargest.py showed it was an issue)
        if arr[i] > pivot_val:
            arr[right], arr[i] = arr[i], pivot_val   
        
        # return the sorted pivot position for reference in the recursive calls
        return i
    
    def partition_via_swaps2(arr, left, right):
        i = left
        pivot_val = arr[right]
        pivot_idx = right

        while i < pivot_idx:
            if arr[i] > pivot_val: 
                arr[i], arr[pivot_idx - 1] = arr[pivot_idx - 1], arr[i]
                arr[pivot_idx], arr[pivot_idx - 1] = arr[pivot_idx - 1], arr[pivot_idx]
                i -= 1
                pivot_idx -= 1
                
            i += 1

        return pivot_idx
        
    
    quicksort_helper(arr, 0, len(arr) - 1)

arr = [1, 3, 8, 4, 2, 7, 7]
quicksort(arr)
print(arr)

