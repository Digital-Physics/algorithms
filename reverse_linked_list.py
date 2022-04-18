# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# time: O(n)
# space: O(1)
def reverseLinkedList(head):
    curr_node = head
    previous_node = None

    while curr_node is not None:
        next_node = curr_node.next
        # now that we've used curr_node.next, reassign curr_node's "next" pointer before reassigning curr_node
        # reassignment breaks the pointer so next_node will stay the same
        curr_node.next = previous_node
        # now that we've used previous node, reassign it
        previous_node = curr_node
        # now that we've used curr_node in the first two steps, reassign it
        curr_node = next_node

    return previous_node