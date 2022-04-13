# time: O(n) (It can be done in one pass using three indexes for where to insert numbers)
# space: O(1)
def threeNumberSort(array, order):
    counter = [0, 0, 0]

    for i in range(len(array)):
        if array[i] == order[0]:
            counter[0] += 1
        elif array[i] == order[1]:
            counter[1] += 1
        elif array[i] == order[2]:
            counter[2] += 1

        # for in-place
        for i in range(counter[0]):
            array[i] = order[0]

        for i in range(counter[1]):
            array[counter[0] + i] = order[1]

        for i in range(counter[2]):
            array[counter[0] + counter[1] + i] = order[2]

    return array

