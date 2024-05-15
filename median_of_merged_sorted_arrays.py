from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """find the median of two sorted arrays after they are (partially merged).
    this is in linear time but we want this done in O(log(m+n))."""

    length = len(nums1) + len(nums2)
    idx = length//2
    
    if length % 2 == 1:
        one_num = True
    else:
        one_num = False
    
    merged_i = 0
    second_to_last_number = 0
    last_number = 0

    i_1 = 0
    i_2 = 0

    while merged_i <= idx:
        if i_1 < len(nums1) and i_2 < len(nums2):
            if nums1[i_1] < nums2[i_2]:
                second_to_last_number = last_number
                last_number = nums1[i_1]
                i_1 += 1
            elif nums2[i_2] <= nums1[i_1]: # it doesn't matter which we pick if they're tied so just pick
                second_to_last_number = last_number
                last_number = nums2[i_2]
                i_2 += 1
        elif i_1 < len(nums1):
            second_to_last_number = last_number
            last_number = nums1[i_1]
            i_1 += 1
        else:  # i_2 < len(nums2)
            second_to_last_number = last_number
            last_number = nums2[i_2]
            i_2 += 1

        merged_i += 1

    return float(last_number) if one_num else (last_number + second_to_last_number)/2   

def findMedianSortedArrays2(nums1: List[int], nums2: List[int]) -> float:
    """find the median of two sorted arrays after they are (partially merged).
    done in O(log(m+n))."""
    n1 = len(nums1)
    n2 = len(nums2)
    
    # make first list the smaller one
    if n1 > n2:
        return findMedianSortedArrays2(nums2, nums1)
    
    n = n1 + n2
    left = (n1 + n2 + 1) // 2 # (17 + 1)//2 = 9 or (18 + 1)//2 = 9
    low = 0
    high = n1  # we'll work off the left partition
    
    while low <= high:
        # the items on the left of both arrays will be half
        mid1 = (low + high) // 2 
        mid2 = left - mid1 
        
        l1 = float('-inf')
        l2 = float('-inf')
        r1 = float('inf')
        r2 = float('inf')
        
        # Determine values of l1, l2, r1, and r2
        if mid1 < n1:
            r1 = nums1[mid1]
        if mid2 < n2:
            r2 = nums2[mid2]
        if mid1 - 1 >= 0:
            l1 = nums1[mid1 - 1]
        if mid2 - 1 >= 0:
            l2 = nums2[mid2 - 1]
        
        if l1 <= r2 and l2 <= r1:
            # The partition is correct, we found the median
            if n % 2 == 1:
                return float(max(l1, l2))
            else:
                return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            # Move towards the left side of nums1
            high = mid1 - 1
        else:
            # Move towards the right side of nums1
            low = mid1 + 1

if __name__ == "__main__":
    print(findMedianSortedArrays([1, 5, 9], [2, 5, 9, 10]))
    print(findMedianSortedArrays([1, 5, 9], [2, 5, 6, 9, 10]))
    print(findMedianSortedArrays2([1, 5, 9], [2, 5, 9, 10]))
    print(findMedianSortedArrays2([1, 5, 9], [2, 5, 6, 9, 10]))
    

