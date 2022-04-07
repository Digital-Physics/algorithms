# time: O(n) we go through each element in for loop doing a constant time max operations at each step
# space: O(1) we use the max_sum array to store our output
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        max_sum_through_second_to_last = array[0]
        max_sum_through_last = max(array[0], array[1])

        # in case there are two elements
        new_best = max_sum_through_last

        for i in range(2, len(array)):
            new_best = max(array[i] + max_sum_through_second_to_last, max_sum_through_last)

            # update for next round
            max_sum_through_second_to_last, max_sum_through_last = max_sum_through_last, new_best

        return new_best

# time: O(n) we go through each element in for loop doing a constant time max operations at each step
# space: O(n) we use the max_sum array to store two relevant numbers
def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    else:
        max_sum_through_idx = [0 for _ in range(len(array))]
        max_sum_through_idx[0] = array[0]
        max_sum_through_idx[1] = max(array[0], array[1])

        best = max_sum_through_idx[1]

        for i in range(2, len(array)):
            max_sum_through_idx[i] = max(array[i] + max_sum_through_idx[i-2], max_sum_through_idx[i-1])
            best = max(best, max_sum_through_idx[i])

        return best