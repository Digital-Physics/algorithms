# https://www.codenewbie.org/basecs/62
# also see rebalance_binary_search_tree2.py

class TreeNode:
    def __init__(self, key):
        self.key = key  # The key is used to determine the position of the node in the tree, while the value (could be different) is the data stored at that node.
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """AVL trees are self-balancing Binary Search Trees"""
    def insert(self, root, key):
        if not root:
            return TreeNode(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, node):
        """we left rotate when the tree is right-heavy
        
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
        new_node = node.right
        node.right = new_node.left
        new_node.left = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left), self.get_height(new_node.right))

        return new_node

    def right_rotate(self, node):
        """we right rotate when the tree is left-heavy"""
        new_node = node.left
        node.left = new_node.right
        new_node.right = node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_node.height = 1 + max(self.get_height(new_node.left), self.get_height(new_node.right))

        return new_node

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root):
        """for printing purposes, although this doesn't tell you how your BST is balanced"""
        if not root:
            return []
        return self.inorder_traversal(root.left) + [root.key] + self.inorder_traversal(root.right)


if __name__ == "__main__":
    avl_tree = AVLTree()
    root = None
    keys = [10, 20, 30, 40, 50, 25]
    for key in keys:
        root = avl_tree.insert(root, key)
        print(f"{root.key=}")

    print("AVL tree inorder traversal:")
    print(avl_tree.inorder_traversal(root))

