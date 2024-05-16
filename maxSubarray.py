from typing import List

def maxSubArray(nums: List[int]) -> int:
    """return the largest subarray sum. what makes this interesting is
    there are positive and negative ints.
    We'll use Kadane's algorithm. 
    time: O(n); space: O(1)"""

    # Always prepend sequence if it's positive =>
    # drop subarray as soon as prefix cumulative total becomes negative;
    # note: are we forced to return at least one number if they are all negative?
    
    def kadane_helper(nums2: List[int], best: int) -> int:
        prefix_sum = 0 # reset on each recursive call (while previous best is passed as argument)

        for i in range(len(nums2)):
            prefix_sum += nums2[i]

            if prefix_sum > best:
                best = prefix_sum

            if prefix_sum < 0:
                return kadane_helper(nums2[i + 1:], best)
        
        return best

    return kadane_helper(nums, 0)


def maxSubArray2(nums: List[int]) -> int:
    """iterative Kadane"""
    prefix_sum = 0
    best = 0
    i = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum > best:
            best = prefix_sum

        if prefix_sum < 0:
            prefix_sum = 0

    return best

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(maxSubArray2([-2,1,-3,4,-1,2,1,-5,4]))