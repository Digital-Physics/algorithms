from collections import deque
from typing import Optional

class BinaryTree:
    def __init__(self, value: int, left: Optional["BinaryTree"] = None, right: Optional["BinaryTree"] = None) -> None:
        self.value = value
        self.left = left
        self.right = right

def get_level_order(root: Optional[BinaryTree]) -> None:
    output = []

    def level_order(root: Optional[BinaryTree]) -> None:
        """return list of nodes from the top level to the bottom level and from left to right in the levels"""
        nonlocal output
        if root is None:
            return output
        
        q = deque([root])

        while q:
            # pop and
            curr_node = q.popleft()

            # process
            output.append(curr_node.value)
            
            # add neighbors
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)

    level_order(root)

    return output

def get_level_order2(root: Optional[BinaryTree]) -> None:
    if root is None:
        return []
    
    output = []

    q = deque([root])

    while q:
        # pop and
        curr_node = q.popleft()

        # process
        output.append(curr_node.value)
        
        # add neighbors
        if curr_node.left:
            q.append(curr_node.left)
        if curr_node.right:
            q.append(curr_node.right)

    return output

if __name__ == "__main__":
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    root.left.left.left = BinaryTree(8)

    print(get_level_order(root))
    print(get_level_order2(None))
    print(get_level_order(root))
    print(get_level_order2(None))
