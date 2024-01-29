#     1
#    / \
#   2   3
#  / \
# 4   5

# Pre-order traversal: Visit the root node, then recursively do a pre-order traversal of the left subtree, followed by a pre-order traversal of the right subtree.

# Pre-order traversal of the above tree: 1, 2, 4, 5, 3

# In-order traversal: Recursively do an in-order traversal of the left subtree, visit the root node, and then do an in-order traversal of the right subtree.

# In-order traversal of the above tree: 4, 2, 5, 1, 3

# Post-order traversal: Recursively do a post-order traversal of the left subtree, then do a post-order traversal of the right subtree, and finally visit the root node.

# Post-order traversal of the above tree: 4, 5, 2, 3, 1

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

def pre_order_traversal(node):
    if node is not None:
        # Process Node
        print(node.val, end=" ")
        # Recursively traverse the left subtree
        pre_order_traversal(node.left)
        # Recursively traverse the right subtree
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is not None:
        # Recursively traverse the left subtree
        in_order_traversal(node.left)
        # Process Node
        print(node.val, end=" ")
        # Recursively traverse the right subtree
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node is not None:
        # Recursively traverse the left subtree
        post_order_traversal(node.left)
        # Recursively traverse the right subtree
        post_order_traversal(node.right)
        # Process Node
        print(node.val, end=" ")

print(pre_order_traversal(root))
print(in_order_traversal(root))
print(post_order_traversal(root))


class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class FlattenBinaryObj:
    def __init__(self) -> None:
        """Flatten Binary Tree into Linked List with an In-Order Traversal"""
        self.prevLLNode: LinkedListNode | None = None
        self.head: LinkedListNode | None = None

    def flattenBinary(self, curr_node: Node | None) -> LinkedListNode:
        print(curr_node, curr_node.val if curr_node is not None else "-", self.prevLLNode, self.head)

        if curr_node is not None:
            self.flattenBinary(curr_node.left)

            # process node
            if self.prevLLNode is None: 
                self.prevLLNode = self.head = LinkedListNode(curr_node.val)
                print('head', self.head, self.head.val)
            else:
                # add the pointer to the next LL node which is created
                print()
                self.prevLLNode.next = LinkedListNode(curr_node.val)
                self.prevLLNode = self.prevLLNode.next
                print("append...............", curr_node.val)
                print()

            self.flattenBinary(curr_node.right)

    def run(self, binRoot: Node | None) -> LinkedListNode | None:
        self.flattenBinary(binRoot)
        return self.head
    

flattenObj = FlattenBinaryObj()
newHead = flattenObj.run(binRoot=root)
print(newHead.val, newHead.next.val, newHead.next.next.val, newHead.next.next.next.val, newHead.next.next.next.next.val, newHead.next.next.next.next.next)
