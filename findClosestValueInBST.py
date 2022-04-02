# O(logn) time complexity since at each node we explore we eliminate half of the tree on average
# O(n) worst case complexity if the tree is one sided
# O(logn) space complexity because our recursive call adds frames to the stack
# =O(h) space where h is the height of the tree (Clement said "depth" not "height")
# if we made this function iterative, we could have O(1) space because we don't have a recursive stack build-up; overwrite tree
def findClosestValueInBst(tree, target):
    if tree.value == target:
        return tree.value
    elif tree.value > target:
        # search left subtree, same target, best_dist, best_node
        return returnSubtreeEtc(tree.left, target, tree.value - target, tree.value)
    else:
        return returnSubtreeEtc(tree.right, target, target - tree.value, tree.value)


def returnSubtreeEtc(subtree, target, best_dist, best_node):
    if subtree is None:
        return best_node
    elif subtree.value == target:
        return subtree.value
    elif subtree.value > target:
        if subtree.value - target < best_dist:
            best_dist = subtree.value - target
            best_node = subtree.value
        return returnSubtreeEtc(subtree.left, target, best_dist, best_node)
    elif subtree.value < target:
        if target - subtree.value < best_dist:
            best_dist = target - subtree.value
            best_node = subtree.value
        return returnSubtreeEtc(subtree.right, target, best_dist, best_node)


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None