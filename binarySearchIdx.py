# Iterative
# O(log n) time | O(1) space
def binarySearch(array, target):
    l_idx = 0
    r_idx = len(array) - 1

    while r_idx >= l_idx:
        mid_idx = (l_idx + r_idx) // 2

        if array[mid_idx] == target:
            return mid_idx
        elif target < array[mid_idx]:
            r_idx = mid_idx - 1
        else:
            l_idx = mid_idx + 1

    return -1

# recursive
# Time: O(log n) time
# Space: O(log n) for the recursive calls put in the call stack
def binarySearch(array, target):
    def binSearchHelper(array, target, l_idx=0, r_idx=len(array) - 1):
        if r_idx < l_idx:
            return -1
        else:
            mid_idx = (l_idx + r_idx) // 2

            if array[mid_idx] == target:
                return mid_idx
            elif target < array[mid_idx]:
                return binSearchHelper(array, target, l_idx, mid_idx - 1)
            else:
                return binSearchHelper(array, target, mid_idx + 1, r_idx)

    return binSearchHelper(array, target)


