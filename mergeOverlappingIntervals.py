# time: O(n*log(n)) for the sort
# space: O(n) for the output we build up
def merge_overlapping_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """think of the calendar matching problem with times converted to integers (minutes since midnight)
    remember: first we need to sort based on the starting time. then we initialize a sorted output list w/ first interval.
    then we compare the end time in the last added time interval added to the sorted output list with...
    the start time in the next interval to be processed in our for loop over the original input list.
    depending on the comparison/overlap, we either (potentially) update the end time in our output list...
    or finalize that output interval by adding the new interval (because the new interval started after last output interval ended)"""
    # n*log(n) sort
    intervals.sort(key=lambda x: x[0])
    output_array = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= output_array[-1][1]:
            output_array[-1][1] = max(output_array[-1][1], intervals[i][1])
        else:
            output_array.append(intervals[i])

    return output_array


test_intervals = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]

print(merge_overlapping_intervals(test_intervals))
