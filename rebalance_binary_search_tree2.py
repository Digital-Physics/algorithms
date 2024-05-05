# https://www.codenewbie.org/basecs/62

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_into_bst(root, val):
    """The order in which we insert values from a list can make the tree returned an unbalance BST"""
    if root is None:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def inorder_traversal(root):
    """This function goes from tree of node objects with pointers back to a list.
    If the tree is a BST, the values will be sorted.

    Usually in-order is:

    recursive_call(curr_node.left)
    process node (e.g. append value to list)
    recursive_call(curr_node.right).

    This process is written in one line but it is evaluated in the same order."""
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

def rotate_left(node):
    """this was one of the rebalancing operations discussed in the podcast.

      10
        \
        20
        / \
       15  30
            \
            40

    left rotation on 10

          20
        /   \
       10   30
        \     \
        15     40

    """
    new_root = node.right  # new_root now points to node 20 object
    node.right = new_root.left  # reassign 10's right to be 20's left (15 node)
    new_root.left = node  # now connect the original node on the left
    return new_root

def rotate_right(node):
    """this was one of the rebalancing operations discussed in the podcast"""
    new_root = node.left
    node.left = new_root.right
    new_root.right = node
    return new_root

def rebalance_bst(root):
    def get_height(node):
        """clever way to get height through the max of two recursive calls on the left and right nodes"""
        if not node: # base case
            return 0
        return 1 + max(get_height(node.left), get_height(node.right))

    def get_balance_factor(node):
        if not node: # if it is a leaf, it's balanced after that point so return 0
            return 0
        return get_height(node.left) - get_height(node.right)

    def balance(node):
        balance_factor = get_balance_factor(node)
        if balance_factor > 1: # one off is ok, but if more the tree is left-heavy
            # Now if the left child is right heavy, we'll do an additional rotation
            if get_balance_factor(node.left) < 0: 
                node.left = rotate_left(node.left)
            return rotate_right(node)
        elif balance_factor < -1:
            if get_balance_factor(node.right) > 0:
                node.right = rotate_right(node.right)
            return rotate_left(node)
        return node
    
    while True:
        new_root = balance(root)
        if new_root == root:
            break
        root = new_root

    return root


# Example
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5]
    root = None
    for val in values:
        root = insert_into_bst(root, val)

    print("Unbalanced BST:")
    print(f"{root.val=}")
    print("But it is a BST, just unbalanced:")
    print(inorder_traversal(root), "\n")

    balanced_root = rebalance_bst(root)
    print("\nBalanced BST:")
    print(f"{balanced_root.val=}")
    print(inorder_traversal(balanced_root))


