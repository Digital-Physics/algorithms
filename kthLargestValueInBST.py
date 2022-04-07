# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# time: O(h+k)? because we do 2h recursive calls (each call on a right tree has a left tree call)
# space: O(h) because the recursive stack only builds call frames to at most the height of the tree
def findKthLargestValueInBst(tree, k):
    print("we want the", k, "th largest value in the (sorted) BST")
    helper = Helper()
    return helper.reverseInOrderTraverse(tree, k)


class Helper():
    def __init__(self):
        self.counter = 0
        self.answer = None

    def reverseInOrderTraverse(self, tree, k):
        # modified reverse inorder traverse to exit recurssion quicker
        if self.answer is not None:
            pass
        elif tree is not None:
            print("value", tree.value)
            print("go to right BST subtree from", tree.value)
            self.reverseInOrderTraverse(tree.right, k)
            self.counter += 1
            print("counter", self.counter, "while tree val is", tree.value)
            if self.counter == k:
                print("write answer to obj attribute, but still need to finish recurrsion")
                self.answer = tree.value
            print("go left from", tree.value)
            self.reverseInOrderTraverse(tree.left, k)
        else:
            print("leaf, do nothing and go to the next call in the stack")

        return self.answer