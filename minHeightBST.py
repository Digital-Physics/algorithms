# time: O(nlogn); could do it O(n) if we passed in where we were in the tree...
# rather than using insert method which starts at the root
# space: O(n) ... the queue will build up and the BST with pointers will build up
def minHeightBst(array):
    median_idx = len(array) // 2
    tree = BST(array[median_idx])
    queue = []
    queue.append(array[:median_idx])
    queue.append(array[median_idx + 1:])

    while queue:
        curr_array = queue.pop(0)
        if len(curr_array) > 0:
            median_idx = len(curr_array) // 2
            tree.insert(curr_array[median_idx])
            queue.append(curr_array[:median_idx])
            queue.append(curr_array[median_idx + 1:])

    return tree


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
