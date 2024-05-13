from typing import Optional

class TreeNode:
    def __init__(self, value: int, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def isBST(root: Optional[TreeNode], lower_bound: int | float = float("-inf"), upper_bound: int | float = float("inf")) -> bool:
    """validates whether the tree is a BST"""
    if root is None: 
        # not an issue returning True on just one leaf without getting to all of them; 
        # it works because our recursive call below returns left AND right (meaning all leaves will be checked and will need to be True to evaluate to True)
        return True 
        
    if lower_bound < root.value < upper_bound:
        return isBST(root.left, lower_bound, root.value) and isBST(root.right, root.value, upper_bound)
    else:
        return False
    
if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print(isBST(root))  # Output: True

    # Construct a non-BST
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)

    print(isBST(root))  # Output: False