# time: O(N) since we traverse the array once (and we do finite, constant calcs each step)
# space: O(1), no recursive stack, just keeping track of top 3 as we go through list
def findThreeLargestNumbers(array):
    # could initialize these to -inf using numpy or math libraries
    # read in first
    first = array[0]

    # second
    if array[1] > first:
        first, second = array[1], array[0]
    else:
        second = array[1]

    # third
    if array[2] > first:
        first, second, third = array[2], first, second
    elif array[2] > second:
        second, third = array[2], second
    else:
        third = array[2]

    def updateLeaders(contender, first, second, third):
        if contender > first:
            first, second, third = contender, first, second
        elif contender > second:
            second, third = contender, second
        elif contender > third:
            third = contender

        return first, second, third

    for idx in range(len(array) - 3):
        first, second, third = updateLeaders(array[idx + 3], first, second, third)

    return [third, second, first]