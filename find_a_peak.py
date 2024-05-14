from typing import List

def findPeakElement(nums: List[int]) -> int:
    """
    we only have to find one peak element and we can assume
    that nums[-1] and nums[n] are both float("-inf"), so we
    can always squeeze a peak at the end points (of recursion too if we do it wisely)
    """
    mid = len(nums)//2

    if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
        return nums[mid]
    elif nums[mid - 1] > nums[mid]: # maybe that adjacent one will be a peak
        return findPeakElement(nums[:mid])
    elif nums[mid + 1] > nums[mid]: # maybe that adjacent one will be a peak
        return findPeakElement(nums[mid + 1:])

