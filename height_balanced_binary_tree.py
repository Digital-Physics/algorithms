# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# time: O(n) because we go through all nodes
# space: O(h) for recursive stack max height
def heightBalancedBinaryTree(tree):
    obj = BalanceCheck()
    obj.get_val(tree)
    return obj.answer


class BalanceCheck():
    def __init__(self):
        self.answer = True

    def get_val(self, tree):
        print()
        # base case
        if tree is None:  # leaf
            print("hit leaf. It has a height of 0. We can now build up other heights with this and other leaves.")
            return 0

        # this is a post-order traversal
        # ...we do both left and right recursive calls first, before processing results
        # ... because we need the height of the left and right subtrees to calc height of current node/tree
        print("Get height val of left subtree of:", tree.value)
        l_node = self.get_val(tree.left)
        print("Get height val of right subtree of:", tree.value)
        r_node = self.get_val(tree.right)

        # ......process step.....
        print("height of left and right subtrees of node w/ value", tree.value, "is", l_node, r_node)
        if abs(l_node - r_node) > 1:
            self.answer = False

        height = max(l_node, r_node) + 1
        print("height of node w/ value", tree.value, "is", height)
        return height
