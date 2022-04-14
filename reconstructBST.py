# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# should review later; Tim took a slightly different approach
# time: O(n**2)
# space: O(n)
def reconstructBst(preOrderTraversalValues):
    print("preOrdered Traversal List", preOrderTraversalValues)
    root = BST(preOrderTraversalValues[0])
    obj = SetChildrenHelper(preOrderTraversalValues)
    obj.setChildren(root, 0)
    return root


# in a pre-order, the right child of any BST node is simply...
# the first node in the pre-order which is greater than it
# our recursion sets a left subtree and right subtree node (not just one)
# note: if this a normal binary tree (not a BST), there could be many trees that the preorder came from
class SetChildrenHelper():
    def __init__(self, preordered_list):
        self.preordered_list = preordered_list
        self.seen = [False for _ in range(len(self.preordered_list))]

    def setChildren(self, curr_node, i):
        print()
        print("set children of node w/ value", curr_node.value, "at index", i)
        r_flag = False
        l_flag = False

        if i + 1 < len(self.preordered_list) and self.preordered_list[i + 1] < self.preordered_list[i] and not self.seen[i + 1]:
            print("left BST created. It's value:", self.preordered_list[i + 1])
            curr_node.left = BST(self.preordered_list[i + 1])
            self.seen[i + 1] = True
            l_flag = True

        for idx in range(i + 1, len(self.preordered_list)):
            if idx < len(self.preordered_list) and not self.seen[idx]:
                if self.preordered_list[idx] >= self.preordered_list[i]:
                    print("right BST created. It's value:", self.preordered_list[idx])
                    curr_node.right = BST(self.preordered_list[idx])
                    self.seen[idx] = True
                    r_flag = True
                    break

        if r_flag:
            print("calling node", curr_node.right.value)
            self.setChildren(curr_node.right, idx)
        if l_flag:
            print("calling node", curr_node.left.value)
            self.setChildren(curr_node.left, i + 1)


