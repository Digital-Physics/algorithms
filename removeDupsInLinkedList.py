# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# time: O(n) since we visit every node in linked list once (even with nested while loops)
# space: O(1) since we only use a few constant variables of auxiliary space
def removeDuplicatesFromLinkedList(linkedList):
    # until curr_node is updated, it is a pointer to the linkedList
    # so when we update curr_node, we updat linkedList (to start, before variable is overwritten)
    curr_node = linkedList
    while curr_node is not None:
        potential_next = curr_node.next
        while potential_next is not None and curr_node.value == potential_next.value:
            # the variable (which is a pointer in memory) is updated
            potential_next = potential_next.next

        # after finding next different node and exiting while loop...
        # set address which also updates linkedList since
        # both variables are pointing to same memory
        curr_node.next = potential_next
        # after overwriting, now the connection to the original linkedList is broken
        curr_node = potential_next

    return linkedList