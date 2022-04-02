# O(n) time complexity because we have to visit every node, and we only do basic, constant-time functions at each node
# O(h) space complexity because the DFS stack will have at most the tree height h, because we have at most one branch in the DFS stack
def nodeDepths(root):
    DFS_stack = []
    node_info = (root, 0)  # depth
    DFS_stack.append(node_info)
    sum_of_depths = 0

    while DFS_stack:
        # pop and process the DFS stack
        node_info = DFS_stack.pop()
        sum_of_depths += node_info[1]

        # put children in stack in correct priority order
        if node_info[0].right is not None:
            DFS_stack.append((node_info[0].right, node_info[1] + 1))
        if node_info[0].left is not None:
            DFS_stack.append((node_info[0].left, node_info[1] + 1))

    return sum_of_depths


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# recursive approach is more elegant and has same time and space complexity
# instead of growing this array stack, we have a function stack
# i guess we can modify the input too (by adding another argument) if we want to use it recursively
def nodeDepths2(root, depth=0):
    # base case for subtrees that are None (leaves)
    if root is None:
        return 0
    else:
        return depth + nodeDepths(root.left, depth+1) + nodeDepths(root.right, depth+1)
