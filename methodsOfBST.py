class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # time: avg: O(logn) worst: O(n) worst (one branch)
    # space: O(logn) or O(h) for recursive call that puts frames on the call stack
    # space (with iterative): O(1)
    def insert(self, value):
        curr_node = self  # will get overwritten
        # iterative is faster; will break loop once we insert at leaf
        # each iteration updates the curr_node to a subtree if not a leaf
        while True:
            if curr_node.value > value:  # going down left
                if curr_node.left is None:
                    curr_node.left = BST(value)
                    break
                else:
                    curr_node = curr_node.left
            else:
                if curr_node.right is None:
                    curr_node.right = BST(value)
                    break
                else:
                    curr_node = curr_node.right

        # Do not edit the return statement of this method.
        # for help with grading
        return self

    # time: avg: O(logn) worst: O(n) worst (one branch)
    # space (with iterative): O(1)
    def contains(self, value):
        curr_node = self
        while curr_node is not None:
            if curr_node.value > value:
                curr_node = curr_node.left
            elif curr_node.value < value:
                curr_node = curr_node.right
            else:  # equal
                return True
        return False


    # time: avg: O(logn) worst: O(n) worst (one branch)
    # space (with iterative): O(1)
    def remove(self, value, parent=None):
        curr_node = self
        while curr_node is not None:
            if curr_node.value > value:
                parent = curr_node  # we want to keep it so we can update it
                curr_node = curr_node.left
            elif curr_node.value < value:
                parent = curr_node
                curr_node = curr_node.right
            # find the succesor for the one we are going to remove
            else:
                # just swap in the leftmost leaf node on the right side of tree...
                # it is the new successor
                # symmetric rule to just swapping the rightmost/largest node on the left tree
                # first, check that it isn't leaf
                if curr_node.left is not None and curr_node.right is not None:
                    curr_node.value = curr_node.right.findMinVal()
                    # after successor put in place, remove old leaf instance
                    curr_node.right.remove(curr_node.value, curr_node)
                #
                # 0 or 1 child nodes below
                #
                # make sure it isn't the root node
                elif parent is None:
                    if curr_node.left is not None:
                        # move the left node up; use it to overwrite value
                        curr_node.value = curr_node.left.value
                        curr_node.right = curr_node.left.right
                        curr_node.left = curr_node.left.left
                    elif curr_node.right is not None:  # gotta use the right node to overwrite; it exists because 0 or 1 at this point
                        curr_node.value = curr_node.right.value
                        curr_node.right = curr_node.right.right
                        curr_node.left = curr_node.right.left
                    else:  # both None
                        pass  # can't remove root
                    # curr_node.value = None
                elif parent.left == curr_node:  # on a left subtree
                    if curr_node.left is not None:
                        # connect the left tree we are on up to the parent node
                        parent.left = curr_node.left
                    else:
                        parent.left = curr_node.right  # exists because 0 or 1 child nodes
                elif parent.right == curr_node:  # on a right subtree
                    if curr_node.left is not None:
                        # connect the right tree we are on up to the parent node
                        parent.right = curr_node.left
                    else:
                        parent.right = curr_node.right
                break
        # Do not edit the return statement of this method.
        return self


    # always called on right node, so always look left after that
    def findMinVal(self):
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left
        return curr_node.value
