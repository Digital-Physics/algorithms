# time complexity O(n)
# space complexity O(n)
def twoNumberSum(array, targetSum):
    dictionary = {}
    # store the targetSum's complement
    for num in array:
        if num in dictionary.keys():
            return [num, targetSum - num]
        else:
            dictionary[targetSum - num] = targetSum - num
    return []


