# time: O(n) for <~3 passes
# space: O(1)
def subarraySort(array):
    print("array", array)
    print("a number is sorted if it is >= its left neighbor and <= its right neighbor")
    temp_sorted = [False for _ in range(len(array))]
    smallest_temp_unsorted = [float("inf"), None]
    largest_temp_unsorted = [float("-inf"), None]

    for i in range(len(array)):
        if i == 0:
            if array[i] <= array[i + 1]:
                temp_sorted[i] = True
            else:
                if array[i] < smallest_temp_unsorted[0]:
                    smallest_temp_unsorted = [array[i], i]
                if array[i] >= largest_temp_unsorted[0]:
                    largest_temp_unsorted = [array[i], i]
        elif i == len(array) - 1:
            if array[i] >= array[i - 1]:
                temp_sorted[i] = True
            else:
                if array[i] < smallest_temp_unsorted[0]:
                    smallest_temp_unsorted = [array[i], i]
                if array[i] >= largest_temp_unsorted[0]:
                    largest_temp_unsorted = [array[i], i]
        else:
            if array[i - 1] <= array[i] <= array[i + 1]:
                temp_sorted[i] = True
            else:
                if array[i] < smallest_temp_unsorted[0]:
                    smallest_temp_unsorted = [array[i], i]
                if array[i] >= largest_temp_unsorted[0]:
                    largest_temp_unsorted = [array[i], i]

    print("temp_sorted", temp_sorted)
    if all(temp_sorted):
        return [-1, -1]

    print("after one traversal, the smallest and largest of the unsorted numbers (and their indices) are:")
    print(smallest_temp_unsorted, largest_temp_unsorted)
    print("but is the smallest unsorted actually greater than the monotonically-increasing left side's right end point?")
    print("similarly, is the largest unsorted less than the monotonically-decreasing right side's left end point?")
    print("if not, we need to expand the end points of the unsorted array, with another pass or two.")

    for i in range(len(array)):
        if temp_sorted[i]:
            if smallest_temp_unsorted[0] < array[i]:
                print("we actually need to expand the left side of our unsorted subarray to", i)
                left_start = i
                break
        else:
            left_start = i
            break

    for i in reversed(range(len(array))):
        print(i)
        if temp_sorted[i]:
            if largest_temp_unsorted[0] > array[i]:
                print("we actually need to expand the right side of our unsorted subarray to", i)
                right_end = i
                break
        else:
            right_end = i
            break

    return [left_start, right_end]