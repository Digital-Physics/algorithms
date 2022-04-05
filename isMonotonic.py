# time: O(n)
# space: O(1)
def isMonotonic(array):
    increasing = None
    stop_idx = None

    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            continue  # or pass
        elif array[i] > array[i - 1]:
            increasing = True
            stop_idx = i
            break
        else:
            increasing = False
            stop_idx = i
            break

    if increasing:
        for i2 in range(stop_idx + 1, len(array)):
            if array[i2] < array[i2 - 1]:
                return False
    elif increasing == False: # we don't want it to pass on None so can't use "is not increasing"
        for i2 in range(stop_idx + 1, len(array)):
            if array[i2] > array[i2 - 1]:
                return False

    return True


# time: O(n) even though we have nested for loops since 2nd for picks up where first stops
# space: O(1)
def isMonotonic2(array):
    for i in range(1, len(array)):
        if array[i] == array[i - 1]:
            continue
        elif array[i] > array[i - 1]:
            for i2 in range(i + 1, len(array)):
                if array[i2] < array[i2 - 1]:
                    return False
            break
        else:
            for i2 in range(i + 1, len(array)):
                if array[i2] > array[i2 - 1]:
                    return False
            break

    return True
