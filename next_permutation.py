from typing import List


def nextPermutation(nums: List[int]) -> None:
    i = j = len(nums)-1 # least significant digit idx

    while i > 0 and nums[i-1] >= nums[i]: # stop right before first decreasing (actually, non-increasing (could have duplicates)) number (and don't go past 0)
        i -= 1

    if i == 0: # it was a total increasing run (going backwards); reset to the the smallest permutation order (an increasing run going forward)
        nums.reverse()
        print(nums)
        return 
    
    # get smallest number greater than the one we stopped at to swap in; that'll be that next digit
    # Note: we won't touch the left part of the string, the Most Significant Digits
    # Note: nums[i-1] is where we stopped; the while loop exited before i got to decrement, hence the -1
    while nums[j] <= nums[i - 1]:
        j -= 1
    
    nums[i-1], nums[j] = nums[j], nums[i-1]
    
    # now we have something smaller 
    # reverse end (but not including the number that got swapped into the correct space where we'd stopped)
    # the significant digits leading up to the swapped digit (going backwards) used to be ascending, now they'll be ascending going forward (like odometer turned over)
    nums[i:]= nums[len(nums)-1:i-1:-1]
    print(nums)

if __name__ == "__main__":
    nextPermutation([1,2,4,3])
    nextPermutation([1,2,4,3,5])
    nextPermutation([3,2,1])