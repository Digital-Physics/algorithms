# time: O((2**n)*n) 2**n subsets with each subset having n/2 elements on average
# space: O((2**n)*n)
def powerset(array):
    current_subsets = [[]]

    while len(array) > 0:
        # it's ok to mutate the original array in this example
        curr_el = array.pop(0)

        # don't mutate current_subsets while iterating through it
        added_subsets = []

        for subset in current_subsets:
            new_subset = subset + [curr_el]
            added_subsets.append(new_subset)

        current_subsets = current_subsets + added_subsets

    return current_subsets


# time: O((2**n)*n) 2**n subsets with each subset having n/2 elements on average
# space: O((2**n)*n)
def powerset2(array):
    current_subsets = [[]]

    while len(array) > 0:
        # it's ok to mutate the original array in this example
        curr_el = array.pop(0)

        for i in range(len(current_subsets)):
            new_subset = current_subsets[i] + [curr_el]
            # why? seems ok that we are mutating object we are using in our iteration reference?
            current_subsets.append(new_subset)

    return current_subsets
