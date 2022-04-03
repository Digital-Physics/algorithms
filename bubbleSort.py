# time: O(n**2) because we have to do multiple passes; best/sorted O(n)
# space: O(1) since the sort is done in place
def bubbleSort(array):
    updated = True  # last round had a swap update so keep going
    length = len(array)

    while updated:
        updated = False
        for i in range(length - 1):  # we don't want to look beyond the last el
            if array[i] > array[i + 1]:
                # swapHelp(i, i+1, array)
                array[i], array[i + 1] = array[i + 1], array[i]
                updated = True
        length -= 1

    return array
