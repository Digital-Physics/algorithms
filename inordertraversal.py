class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

counter = 0
output = None

def inOrderTraversal(node: Node, k: int) -> int:
    """in-order traversal"""
    global counter, output

    if node.left is not None:
        inOrderTraversal(node.left, k)

    counter += 1
    # process
    if counter == k:
        output = node.val

    if node.right is not None and counter < k:
        inOrderTraversal(node.right, k)

root = Node(7)
root.left = Node(3)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.left = Node(11)
root.right.right = Node(17)
root.right.right.right = Node(17)

class Solution:
    def __init__(self):
        self.counter = 0
        self.output = None

    def kthSmallest(self, root: Node, k: int) -> int:
        def inOrder(node):
            if not node or self.output is not None:
                return

            inOrder(node.left)

            self.counter += 1
            if self.counter == k:
                self.output = node.val
                return

            inOrder(node.right)

        inOrder(root)
        return self.output

def kth_smallest(root: Node, k: int) -> int:
    counter = 0
    result = None

    def in_order(node):
        nonlocal counter, result
        if not node or result is not None:
            return

        in_order(node.left)
        counter += 1
        if counter == k:
            result = node.val
            return
        in_order(node.right)

    in_order(root)
    return result


if __name__ == "__main__":
    # inOrderTraversal(root, 6)
    inOrderTraversal(root, 6)
    print(output)

    sol = Solution()
    print(sol.kthSmallest(root, 6))

    print(kth_smallest(root, 6))

