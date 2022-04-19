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

        # now that we've used curr_node.next, reassign curr_node's "next" pointer
        # reassignment breaks the pointer so next_node, which we just assigned, will stay the same
        curr_node.next = previous_node

        # now that we've used previous_node, reassign it
        previous_node = curr_node

        # now that we've used curr_node in the first three steps, reassign it
        curr_node = next_node

    return previous_node


# time: O(n)
# space: O(1)
def reverseLinkedList2(head):
    curr_node = head
    previous_node = None

    while curr_node is not None:
        # don't lose this variable when you reassign the next arrow/pointer in the middle node
        next_node = curr_node.next

        # now that we've used curr_node.next, reassign curr_node's "next" pointer
        # reassignment breaks the pointer so next_node, which we just assigned, will stay the same
        curr_node.next = previous_node

        # now update the other two pointers
        previous_node, curr_node = curr_node, next_node

    return previous_node