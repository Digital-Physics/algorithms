# flip binary tree left to right
# time: O(n) we process each node, and there is a constant number of swaps (2) done in constant time each
# space: O(h) for the recursive call stack that can reach a max size of the height of the tree
class BinaryTree:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def invertBinaryTree(tree: BinaryTree) -> None:
    """'invert' or rather do an in-place left-right mirror flip of a binary tree..."""
    tree.left, tree.right = tree.right, tree.left
    if tree.left is not None:
        invertBinaryTree(tree.left)
    if tree.right is not None:
        invertBinaryTree(tree.right)


