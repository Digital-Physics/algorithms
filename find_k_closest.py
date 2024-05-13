from typing import List

def findKclosest(arr: List[int], k: int, target: int) -> List[int]:
    """find the k closest elements in a sorted list and return them in a sorted list (ascending)"""

    # [1, 17, 20, 23, 31, 35], 3, 27
    # [1, 2, 3, 4, 5], 4, -1

    # 1) log time Binary search on sorted array
    h_idx = len(arr) - 1 # 4
    l_idx = 0

    while h_idx > l_idx:
        mid_idx = (h_idx + l_idx)//2

        if arr[mid_idx] < target:
            l_idx = mid_idx + 1
        elif arr[mid_idx] > target:
            h_idx = mid_idx # 0
        elif arr[mid_idx] == target:
            break    
 
    # start k elements below where we are (with range checks)
    window_start = max(l_idx - k, 0)
    window_end = window_start + k

    left_distance = abs(arr[window_start] - target)

    while window_end + 1 < len(arr) and abs(arr[window_end + 1] - target) < left_distance:
        window_start += 1
        window_end += 1
        left_distance = max(arr[window_start], arr[window_end])

    return arr[window_start: window_end]

def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k # binary search for the left starting point of range

    while left < right:
        mid = (left + right) // 2

        if x - arr[mid] > arr[mid + k] - x:  # if left side distance > right side distance
        # if abs(x - arr[mid]) > abs(arr[mid + k] - x):  # abs not needed, but easier to reason through in my head
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]

if __name__ == "__main__":
    print(findKclosest([1, 17, 20, 23, 31, 35], 3, 27))
    print(findClosestElements([1, 17, 20, 23, 31, 35], 3, 27))
    print(findKclosest([1, 2, 3, 4, 5], 4, -1))
    print(findClosestElements([1, 2, 3, 4, 5], 4, -1))

    




