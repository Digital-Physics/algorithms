# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# time: O(n) since we visit every node once and at only do constant time functions within those visits
# space: O(n). The DFS stack has at most log n nodes to visit at once...
# but the output is the number of leaves which is ~n/2 on perfectly balanced tree
def branchSums(root):
    # tree/node, total sum
    DFS_stack = [[root, root.value]]
    branch_sums = []

    while DFS_stack:
        print(DFS_stack)
        node = DFS_stack.pop()

        if node[0].left is None and node[0].right is None:
            branch_sums.append(node[1])

        # put children in stack in correct priority order
        if node[0].right is not None:
            DFS_stack.append([node[0].right, node[1] + node[0].right.value])
        if node[0].left is not None:
            DFS_stack.append([node[0].left, node[1] + node[0].left.value])

    return branch_sums
