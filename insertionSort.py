# time: O(n**2) because we have to do multiple passes; best when sorted O(n)
# space: O(1) since the sort is done in place
def insertionSort(array):
    insert_idx = 1  # first element is already sorted; first not sorted

    while insert_idx < len(array):
        check_idx = insert_idx
        while check_idx >= 1:
            if array[check_idx] < array[check_idx - 1]:
                array[check_idx], array[check_idx - 1] = array[check_idx - 1], array[check_idx]
            check_idx -= 1
        insert_idx += 1

    return array