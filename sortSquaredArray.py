# note: the input array is sorted

# brute force
# O(n log n) time
# n objects in one 32bit int squared in one CPU step? each, and then nlogn is the quickest sort (merge sort, heap sort, quick sort)
# n + nlogn < 2nlogn => O(nlogn)
# O(n) space because we need to create an array
def sortedSquaredArray(array):
    # still need to sort even if you are told array is sorted... also what about negatives? so yeah, you need to sort it afterwards
    # and not with .sort()
    return sorted([el**2 for el in array])


# O(n)? time complexity since we only go through list once... but merging two lists takes O(n+m) so actually O(n**2) :(
# O(n) is space complexity since we create an array before we return it; we can't modify the input array...
# but can we not chunk it in and out?
def sortedSquaredArray(array):
    r_idx = len(array) - 1
    l_idx = 0
    sorted_squares = []

    while r_idx - l_idx >= 0:
        if r_idx - l_idx == 0:
            return [array[r_idx] ** 2] + sorted_squares
        else:
            if abs(array[l_idx]) >= abs(array[r_idx]):
                sorted_squares = [array[l_idx] ** 2] + sorted_squares
                l_idx += 1
            else:
                sorted_squares = [array[r_idx] ** 2] + sorted_squares
                r_idx -= 1


# O(n) is the time complexity since we only go through list once...
# two changes: multiply instead of square? is that helpful? and we don't concatenated two lists in O(n+m)
# O(n) is space complexity since we create an array before we return it; we can't modify the input array... but can we not chunk it in and out?
def sortedSquaredArray(array):
    r_idx = len(array) - 1
    l_idx = 0
    sorted_squares = [0 for _ in range(len(array))]

    for output_idx in reversed(range(len(array))):
        if abs(array[l_idx]) >= abs(array[r_idx]):
            sorted_squares[output_idx] = array[l_idx] * array[l_idx]
            l_idx += 1
            output_idx -= 1
        else:
            sorted_squares[output_idx] = array[r_idx] * array[r_idx]
            r_idx -= 1
            output_idx -= 1

    return sorted_squares

