# time: O(n) one tree traversal (in-order)
# space: O(h) for the max size of the height of the recursive call stack
# it's a little easier to do an in-order traversal where we write to a list at the middle step, and then update links afterwards
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def flattenBinaryTree(root):
    leftest_of_root, rightest_of_root = flatten_helper(root)
    return leftest_of_root


def flatten_helper(node):
    print()
    if node.left is None:
        farthest_left = node
    else:
        print("parent node.value", node.value)
        print("recursive call to get rightest and leftest of the left subtree")
        # encode parent in variable name
        leftest_of_left, rightest_of_left = flatten_helper(node.left)
        print("update DLL pointer. one adjacent is rightest of the left subtree. Node.left should point to it.")
        create_links(rightest_of_left, node)
        farthest_left = leftest_of_left

    if node.right is None:
        farthest_right = node
    else:
        print("parent node.value", node.value)
        print("recursive call on the right subtree")
        leftest_of_right, rightest_of_right = flatten_helper(node.right)
        print("make another pointer. we want the leftest of the right subtree. Node.right should point to it.")
        create_links(node, leftest_of_right)
        farthest_right = rightest_of_right

    print("recursive output", [farthest_left, farthest_right])
    return [farthest_left, farthest_right]


def create_links(left_node, right_node):
    left_node.right = right_node
    right_node.left = left_node