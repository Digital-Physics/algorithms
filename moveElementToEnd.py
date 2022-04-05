# time: O(n) linear time because we just go through the list once bringing two idx closer
# space: O(1) in space swapping
def moveElementToEnd(array, toMove):
    l_idx = 0
    r_idx = len(array) - 1

    while l_idx < r_idx:
        if array[l_idx] != toMove:
            l_idx += 1
        else:
            if array[r_idx] == toMove:
                r_idx -= 1
            else:
                array[l_idx], array[r_idx] = array[r_idx], array[l_idx]
                l_idx += 1
                r_idx -= 1

    return array
