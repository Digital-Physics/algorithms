def leftmost_binary_search(arr, target):
    low, high = 0, len(arr) - 1
    result = -1
    
    while low <= high:
        mid = low + (high - low) // 2
        
        if arr[mid] == target:
            result = mid 
            # don't return the result; keep going by updating the pointers
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return result

def binary_search(arr, target):
    """return the index of the target"""
    low, high = 0, len(arr) - 1
    result = -1 # if we can't find the index

    while low <= high:
        mid = (low + high)//2

        if arr[mid] == target:
            result = mid # return index
            return result
        elif arr[mid] > target:
            low = mid + 1
        else:
            high = mid -1
    
    return result


array = [2, 3, 3, 3, 4, 8, 10, 12]

print(leftmost_binary_search(array, 3))
print(binary_search(array, 3))

