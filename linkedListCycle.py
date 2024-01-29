# from typing import Optional, Union, List # dict, bool, int, str

class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

# this has linear space because we build up seen dict
# def hasCycle(head: Optional[ListNode]) -> bool:
def hasCycle(head: ListNode | None) -> bool:
    """this function tells you whether there is a loop in a linked list."""
    # seen = dict()
    seen = set()

    curr_node = head

    while curr_node is not None:
        print()
        print("id(curr_node), hex(id(curr_node))", id(curr_node), hex(id(curr_node)))

        print("seen set()", seen)

        if curr_node in seen:
            return True
        
        # seen[curr_node] = True
        seen.add(curr_node)
        curr_node = curr_node.next

    return False

node = ListNode(4)
node.next = ListNode(22)
node.next.next = ListNode(8)

print(hasCycle(node))

node.next.next.next = node.next

print(hasCycle(node))

print()
print("docstring: hasCycle.__doc__ :", hasCycle.__doc__)

