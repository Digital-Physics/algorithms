# time: O(N**2 N!) number of recursive calls: N! base cases, which took n calls to get to, with an extra n for concatenating & slicing
# space: O(N* N!) length of perm * num of permutations
def getPermutations(array):
    permutations_list = []  # our helper function will append to this
    next_perm_adder(array, [], permutations_list)
    print("all recursive calls kicked off have completed")
    return permutations_list


# handles one partial perm at a time
# but it recursively kicks off several more
# all the recursion does is eventually write to the list; there are no return elements to aggregate
def next_perm_adder(nums_left, partial_perm, permutations_list):
    print()
    print("remaining nums to use:", nums_left)
    print("perm constructed so far:", partial_perm)
    print("perm list for output so far:", permutations_list)

    if len(nums_left) == 0 and len(partial_perm):
        permutations_list.append(partial_perm)
        print("******append completed with permutation", partial_perm)
    else:
        for i, num in enumerate(nums_left):
            # copying; concatenating (w/ new name) instead of appending to avoid pointer headaches
            new_perm = partial_perm + [num]
            # copying; concatenating instead of popping to avoid pointer headaches
            print("kick off and put in call stack:")
            print("   remaining nums to use:", nums_left[:i] + nums_left[i + 1:])
            print("   perm constructed so far:", new_perm)
            print("   perm list for output so far:", permutations_list)
            next_perm_adder(nums_left[:i] + nums_left[i + 1:], new_perm, permutations_list)



