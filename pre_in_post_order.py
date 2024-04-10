class BinaryTree:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None

def preorder(root: BinaryTree):
    if root is None:
        return
    
    print(root.val)
    preorder(root.left)
    preorder(root.right)

def inorder(root: BinaryTree):
    if root is None:
        return
    
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def postorder(root: BinaryTree):
    if root is None:
        return
    
    postorder(root.left)
    postorder(root.right)
    print(root.val)


tree = BinaryTree(1)
tree.left = BinaryTree(2)
tree.left.left = BinaryTree(3)
tree.left.right = BinaryTree(4)
tree.right = BinaryTree(5)

preorder(tree)
inorder(tree)
postorder(tree)
