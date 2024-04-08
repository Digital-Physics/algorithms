from typing import List

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_min_value_node(node):
    current = node
    while current.left:
        current = current.left
    return current

def remove_node(root, value):
    if not root:
        return root

    if value < root.value:
        root.left = remove_node(root.left, value)
    elif value > root.value:
        root.right = remove_node(root.right, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = find_min_value_node(root.right)
        root.value = temp.value
        root.right = remove_node(root.right, temp.value)

    return root

# def remove_node2(root: TreeNode, value: int, parent: TreeNode | None = None) -> List[TreeNode]:
#     """we have the sub-root to remove and it's left subtree. 
#     find left-most/min val node in right tree in log(n) time. 
#     overwrite val of subroot with value of leftmost node.
#     remember parent. write parent.left = None. 
#     subroot.right = new right subtree
#     """
#     if value < root.value:
#         root.left = remove_node2(root.left, value, root)
#     elif value > root.value:
#         root.right = remove_node2(root.right, value, root)
#     else: # match
#         if not root.left:
#             return root.right
#         elif not root.right:
#             return root.left

#     right_subtree = subroot.right
#     min_node, parent_of_min_node = find_min_value_node2(right_subtree)
#     subroot.value = min_node.value
#     parent_of_min_node.left = None

#     return

# Example usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

# Remove node with value 3
root = remove_node(root, 3)