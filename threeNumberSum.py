# time: O(n**2) for the second step, the for-while nested loops
# space: O(n) for the output array we're building, we could store all values (mult times)
#
# this is like using the sum's complements in the two-sum algo question...
# ...although no sum's complement hash table
# inside of a for loop that adjusts the targetSum
def threeNumberSum(array, targetSum):
    # sort in O(n log(n)) to start using quick sort, for instance
    # will help narrow search from brute force O(n**3) approach to O(n**2)
    array.sort()
    output_arrays = []

    # should we enumerate or just handle 3 idx?
    for i, num in enumerate(array[:-2]):
        # initialize
        l_idx = i + 1
        r_idx = len(array) - 1

        while l_idx < r_idx:
            if num + array[l_idx] + array[r_idx] == targetSum:
                output_arrays.append([num, array[l_idx], array[r_idx]])
                # could move just one index too but this is riskless and quicker
                l_idx += 1
                r_idx -= 1
            elif num + array[l_idx] + array[r_idx] > targetSum:
                r_idx -= 1
            else:
                l_idx += 1

    return output_arrays