# time: O(n) we only see each node once
# space: O(log n) or O(h) for recursive call that returns TWO recusive calls
# the call stack will build up as it goes down the left side before returning values
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # initialize to infinity because root is not in right or left branch
    return valHelper(tree, float("-inf"), float("inf"))


# if left and right tree are valid, then we're good (recursively)
def valHelper(tree, min_val, max_val):
    # base case
    if tree is None:
        return True
    # each node has a min and max right value (which could be -inf or inf in some situations)
    # the further down you go, the more your min and max constrain valid values
    # the equality/inequality below reflect that you can be equal to the min (ties are added to the right)
    elif tree.value < min_val or tree.value >= max_val:
        return False
    else:
        # when you go left, your min is bounded
        leftside = valHelper(tree.left, min_val, tree.value)
        rightside = valHelper(tree.right, tree.value, max_val)
        return leftside and rightside