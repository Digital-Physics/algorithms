# time: O(n) worst case
# space: O(1) # take advantage that numbers are only from 1 to n
# we will never be out of range; we hop around. numbers treating like hash. negative marks seen. if you find a negative after hashing, you've seen that input before.
def firstDuplicateValue(array):
    for i in range(len(array)):
        if array[i] < 0:
            if array[abs(array[i]) - 1] < 0:
                return abs(array[i])
            else:
                array[abs(array[i]) - 1] *= -1
        else:
            if array[array[i] - 1] < 0:
                return array[i]
            else:
                array[array[i] - 1] *= -1

    return -1


# time: O(n)
# space: O(n)
def firstDuplicateValue2(array):
    dict_of_seen = {}
    for i in range(len(array)):
        if array[i] in dict_of_seen:
            return array[i]
        else:
            dict_of_seen[array[i]] = True

    return -1