# time: O(nlog(n)) for the sort
# space: O(n) for the output we build up
def mergeOverlappingIntervals(intervals):
    # nlogn sort
    intervals.sort(key=lambda x: x[0])
    output_array = [intervals[0]]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= output_array[-1][1]:
            output_array[-1][1] = max(output_array[-1][1], intervals[i][1])
        else:
            output_array.append(intervals[i])

    return output_array
