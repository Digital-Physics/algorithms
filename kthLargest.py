from typing import List

# this is quicker than sorting in O(n*log(n)); this is O(n) because we expect to se 1n + ~1/2n, + ~1/4n, etc.
def findKthLargest(nums: List[int], k: int) -> int:
    """like quicksort with pivot, but we only call recursion on one side"""
    def quick_select(nums: List[int], l: int, r: int, target_idx: int) -> None:
        pivot_idx = partition_via_swaps2(nums, l, r)
        
        if pivot_idx < target_idx: 
            return quick_select(nums, pivot_idx + 1, r, target_idx)
        elif pivot_idx > target_idx: 
            return quick_select(nums, l, pivot_idx - 1, target_idx)
        else:
            return nums[pivot_idx]

    
    def partition_via_swaps(arr, left, right): # and return the sorted ending pivot index
        # note: you need to pass in the index, because low is not always 0 and high is not alway len(arr) - 1
        i = left
        j = right - 1
        pivot_val = arr[right]

        while i < j:
            # looking for first swap index, avoiding out of range issues
            while arr[i] < pivot_val and i < right:
                i += 1

            # note: j can go past i within each while loop step, but not pass the end. we'll check whether they crossed before we swa in the next step.
            while arr[j] > pivot_val and j > left: 
                j -= 1

            # swap if we didn't find pointers in the other side's territory (we don't want to swap good ones out of the left and right sides)
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # swap pivot val and arr[i]
        # i thought we didn't we didn't need extra line of code shown in https://www.youtube.com/watch?v=9KBwdDEwal8,  but we do
        # edge cases got us confused, and for that reason, we like swap2 better
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
        
    # e.g. 3rd largest in a set of 10 (0-9) will have an idx of 7, len(nums) - k
    return quick_select(nums, 0, len(nums) - 1, len(nums) - k)


if __name__ == "__main__":
    print(findKthLargest([1, 3, 4, 8, 5, 6], 1), "...1st largest should be 8")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 2), "...2nd largest should be 6")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 3), "...3rd largest should be 5")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 4), "...4th largest should be 4")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 5), "...5th largest should be 3")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 6), "...6th largest should be 1")
    print(findKthLargest([1, 3, 4, 8, 5, 6], 6 - 2 + 1), "...2nd smallest (5th largest) should be 3") # kth smallest