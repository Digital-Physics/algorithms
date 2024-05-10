from collections import deque #, defaultdict (not used in favor of the SortedDict instead)
from sortedcontainers import SortedDict
from typing import Optional # Union[blah, None] = Optional[blah]
# I'm not sure why the "|"" with type in quotes for the type being defined didn't work. https://peps.python.org/pep-0484/#forward-references

class TreeNode:
    # def __init__(self, val: int = 0, left: None | 'TreeNode' = None, right: None | 'TreeNode' = None, col: int = 0):
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None, col: int = 0):
        self.val = val
        self.left = left
        self.right = right
        self.col = col # how left or negative; root = 0, left = -1, right = 1, left.left = -2

def vertical_order_traversal(root: TreeNode | None):
    """we store """
    if root is None: # handle empty call
        return []

    # A BFS will allow us to get the most Vertical elements first, which should end up in our output list first
    queue = deque([root])
    # dict_of_cols_lists = defaultdict(list)
    sorted_dict_of_cols_lists = SortedDict()

    while queue:
        # pop, process, add children to queue/stack

        # pop
        curr_node = queue.popleft()
    
        # process for output
        if curr_node.col in sorted_dict_of_cols_lists:
            sorted_dict_of_cols_lists[curr_node.col].append(curr_node.val)
        else:
            sorted_dict_of_cols_lists[curr_node.col] = [curr_node.val] # inserting into ordered, sorted-by-key-list is O(log(n))

        # add children
        if curr_node.left is not None:
            curr_node.left.col = curr_node.col - 1
            queue.append(curr_node.left)
        if curr_node.right is not None:
            curr_node.right.col = curr_node.col + 1
            queue.append(curr_node.right)

    output = []

    for val_list in sorted_dict_of_cols_lists.values():
        output.extend(val_list)

    return output

# Example usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(vertical_order_traversal(root))