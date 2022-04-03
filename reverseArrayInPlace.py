def reverseArrayInPlace(array):
    l_idx = 0
    r_idx = len(array)-1

    while l_idx < r_idx:
        array[l_idx], array[r_idx] = array[r_idx], array[l_idx]
        l_idx += 1
        r_idx -= 1

    return array


print(reverseArrayInPlace([2,4,5,6]))