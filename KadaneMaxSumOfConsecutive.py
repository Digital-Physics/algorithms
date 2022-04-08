# time: O(n) since we go through each number in the array once doing constant time algos at each step
# space: O(1) since we don't add more than a constant auxiliary memory
def kadanesAlgorithm(array, best=float("-inf")):
    # drop subarray as soon as running total becomes negative
    # always want to prepend sequence if it's positive
    # note: we are forced to return at least one number if they are all negative
    running_total = 0
    print()
    print("best", best)
    print("running total", running_total)

    for i in range(len(array)):
        running_total += array[i]
        if running_total > best:
            best = running_total

        if running_total < 0:
            return kadanesAlgorithm(array[i + 1:], best)

    return best
