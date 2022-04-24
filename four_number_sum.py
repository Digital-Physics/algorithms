# we didn't use the smart way to avoid duplicates
# we just sorted our quadruples lists, turned them into hashable tuples, and put it through a set at the end
# Clement's way: wait to add complement value pair to the hash table until you hit the second number in your pair
# Clement's way: Avg: O(n**2) time | O(n**2) space; Worst:
def fourNumberSum(array, targetSum):
    two_sum_complement_dict = {}
    output_list = []

    print("target sum:", targetSum)

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            print(i, j, "values:", array[i], array[j])
            if array[i] + array[j] in two_sum_complement_dict:
                print("matched complement")
                for pair in two_sum_complement_dict[array[i] + array[j]]:
                    print("pair", pair)
                    # no indices used twice
                    if pair[0] != i and pair[1] != i and pair[0] != j and pair[1] != j:
                        output_list.append([array[i], array[j]] + [array[pair[0]], array[pair[1]]])

            print("add to table")
            if targetSum - (array[i] + array[j]) in two_sum_complement_dict:
                two_sum_complement_dict[targetSum - (array[i] + array[j])].append([i, j])
            else:
                two_sum_complement_dict[targetSum - (array[i] + array[j])] = [[i, j]]

    # a set of lists is not possible, because lists aren't hashable, because they are mutable
    # tuples are hashable because they are immutable. hash((1,2)) won't error. hash([1,2]) will error.
    # what would happen if you .append something to a list?... it would change your dict key! or item in your set!
    # if you changed a set element, do you want to add a new element or modify existing??
    return set(map(lambda x: tuple(sorted(x)), output_list))

