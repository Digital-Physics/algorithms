# https://www.codenewbie.org/basecs/62
# import random

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# def sorted_array_to_bst(nums):
#     """ This function goes from a sorted list to a BST. 
#     This function exists so we can go from an example list to a BST of nodes without manually creating the connections.

#     At a high level, this function puts the middle element in our sorted list into a new node object and returns it, 
#     but before it returns it, it recursively call this process on the remaining left and right elements in the partitioned list.
#     """
#     if not nums:
#         return None # at some point, after many recursive calls, our .left or .right will be None
#     mid = len(nums) // 2
#     root = TreeNode(nums[mid])
#     # since this function recursively calls itself and then return the root node, these assignments work
#     root.left = sorted_array_to_bst(nums[:mid]) 
#     root.right = sorted_array_to_bst(nums[mid+1:])
#     return root

# def random_insert_into_tree(root, val):
#     """We don't want to rebalance a normal tree because rebalancing a BST has value (quicker retrieval, adding, etc.)
#     while rebalancing a normal tree doesn't do much for us. We couldn't use it for quick retrieval in the first place."""
#     if root is None:
#         return TreeNode(val)
    
#     if random.randint(0, 1):
#         root.left = random_insert_into_tree(root.left, val)
#     else:
#         root.right = random_insert_into_tree(root.right, val)
#     return root

def insert_into_bst(root, val):
    """The order in which we insert values from a list will make the tree returned an unbalance BST"""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def inorder_traversal(root):
    """This function goes from tree of node objects and pointers back to a list.
    If the tree is a BST, the values will be sorted.

    Usually in-order is:

    recursive_call(curr_node.left)
    process node (e.g. append value to list)
    recursive_call(curr_node.right).

    This process is written in one line but it is evaluated in the same order."""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def balance_bst(root):
    """this function takes in a (BST) tree and returns a (sorted) list.
    The sorted list (if a BST was put in) length can then be used to determine root 
    of balanced BST. The helper function is then recursively called on the partitioned list
    so we can find the appropriate mid elements of those lists that will be the left and right nodes.
    Note: no left or right rotations used here."""
    def build_balanced_tree(nums):
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = build_balanced_tree(nums[:mid])
        node.right = build_balanced_tree(nums[mid + 1:])
        return node

    inorder = inorder_traversal(root)
    return build_balanced_tree(inorder)


# Example
if __name__ == "__main__":
    values = [2, 3, 4, 7, 6, 8]
    root = None
    for val in values:
        root = insert_into_bst(root, val)

    print("Unbalanced BST:")
    print(f"{root.val=}")
    print("But it is a BST, just unbalanced:")
    print(inorder_traversal(root))

    balanced_root = balance_bst(root)
    print(f"{balanced_root.val=}")
    print("\nBalanced BST:")
    print(inorder_traversal(balanced_root))


