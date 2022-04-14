# flip binary tree left to right
# time: O(n) since we although we do two child swaps in one step, we still need to process each node
# space: O(h) for the recursive call stack that can reach a max size of the height of the tree
def invertBinaryTree(tree):
    tree.left, tree.right = tree.right, tree.left
    if tree.left is not None:
        invertBinaryTree(tree.left)
    if tree.right is not None:
        invertBinaryTree(tree.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
