from typing import List
from collections import defaultdict

# time: O(n**2) for the second step, the for-while nested loops
# space: O(n) for the output array we're building, we could store all values (mult times)
#
# this is like using the sum's complements in the two-sum algo question...
# ...although no sum's complement hash table
# inside of a for loop that adjusts the targetSum
def threeNumberSum(array, targetSum):
    """this seems to be missing some possibilities as shown in our test case 2.
    we should find the bug at some point, but not right now."""
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

def threeNumberSum2(array: List[int], targetSum: int) -> List[List[int]]:
    """keep a list of numbers we've seen so far. when looking at a new number,
    check if it is in the 2-nums complements. then add to the 2-nums complement."""
    
    two_nums_dict = defaultdict(list)  # e.g. target 10: key: 3, value: [2, 5]
    output = []

    for i in range(len(array)):
        if array[i] in two_nums_dict: 
            for two_list in two_nums_dict[array[i]]:
                output.append(two_list + [array[i]])
        
        for j in range(i):
            left_over = targetSum - (array[j] + array[i])
            two_nums_dict[left_over].append([array[j], array[i]])

    return output

if __name__ == "__main__":
    print(threeNumberSum([2, 3, 4, 3, 4, 5, 5], 10))
    print(threeNumberSum2([2, 3, 4, 3, 4, 5, 5], 10))



    
