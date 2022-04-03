# "selection sort" because it selects the min remaining in the unsorted and swaps it into end of sorted section
# time: O(n**2) because we have to do multiple passes; best when sorted O(n)
# space: O(1) since the sort is done in place
def selectionSort(array):
    start_idx = 0  # first num in unsorted portion, which is on the right

    while start_idx < len(array) - 1:  # last element will be sorted at the end so -1
        # reset for sweep through next unsorted elements segment
        smallest_idx = start_idx
        for check_idx in range(start_idx + 1, len(array)):
            if array[check_idx] < array[smallest_idx]:
                smallest_idx = check_idx

        # there will be a new smallest you found in the unsorted section
        # swap it with the starting position of this round before increment start for next round
        array[smallest_idx], array[start_idx] = array[start_idx], array[smallest_idx]
        start_idx += 1

    return array