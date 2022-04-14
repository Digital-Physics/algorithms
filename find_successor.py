# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# Note: I did not leverage parent attribute. Look at Tim's solution for a better solution.
# time: O(n)?
# space: O(h)?
def findSuccessor(tree, node):
    # DFS is similar to an preorder traversal
    # But we are doing an in-order traversal
    # So it's like DFS but we don't pop&process the node until after our first left call
    obj = In_order_helper(node)
    obj.steps(tree)
    return obj.answer_found


class In_order_helper():
    def __init__(self, node):
        self.target = node.value
        self.answer_found = None
        self.in_order_list = [None]  # so we have a value right off the bat for our first -1 ref

    # recursive call left, process, recursive call right
    # don't pop and process right away like a pre-order
    def steps(self, tree):
        print()
        if tree is not None and self.answer_found is None:
            print("will do left subtree call. curr tree val", tree.value)
            self.steps(tree.left)

            if tree is not None and self.answer_found is None:
                print("process node")
                print("tree val:", tree.value)
                print("in-order list", self.in_order_list)

                if self.in_order_list[-1] == self.target:
                    print("found answer")
                    self.answer_found = tree
                else:
                    if tree is not None:
                        print("append", tree.value)
                        self.in_order_list.append(tree.value)

            if tree is not None and self.answer_found is None:
                print("will do right subtree call. curr tree val", tree.value)
                self.steps(tree.right)
