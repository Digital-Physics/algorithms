# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# time: O(n) since you visit each node
# space: O(h) which is the max height the call stack grows to
def binaryTreeDiameter(tree):
    return get_vals(tree).diam

class Node(): # not sure this needs to be a class object.
    def __init__(self, diam, height):
        self.diam = diam
        self.height = height

def get_vals(tree: BinaryTree) -> Node:
    print()
    if tree is None:  # leaf; sometimes it is written "if not tree:" or "if not root:" taking advantage of truthy/falsy
        print("leaf, so diameter and height calcs have hit bottom")
        return Node(0, 0)

    print("get vals of node(which will need to look at subtrees):", tree.value)
    l_node = get_vals(tree.left)
    r_node = get_vals(tree.right)

    # including parent node
    one_way = l_node.height + r_node.height
    print("diam going through current node", tree.value, ":", one_way)
    # one of the children may win without using parent node
    print("diam of subtrees:", l_node.diam, r_node.diam)
    diameter = max(l_node.diam, r_node.diam, one_way) # should this compare the height with the +1 ? 🧐 maybe not...
    print("best diam through this node:", diameter)
    # height calculated recursively after reaching leaves
    height = max(l_node.height, r_node.height) + 1
    print("height of", tree.value, ":", height)

    return Node(diameter, height)



