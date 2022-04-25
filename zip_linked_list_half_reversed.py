# Tim's way is to cleverly split the Linked List w/ a counter and 2x counter
# And then did a zip with the two lists (one is a reverse linked list (using three variables))
# This would be faster and make it doable in O(n) time
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def zipLinkedList(linkedList, looking_for=None, original_head=None):
    insert_after = linkedList  # to save until needed
    curr_node = linkedList  # to update
    if original_head is None:  # to save from first call (and pass until done)
        original_head = linkedList

    # base case
    if curr_node.next == looking_for:
        curr_node.next = None
        return original_head


    while curr_node.next != looking_for:
        curr_node = curr_node.next

    # make last node point to what will be it's next node
    curr_node.next = insert_after.next
    # insert after insert_after
    insert_after.next = curr_node
    # the new "tail" node doesn't point to None now, it points to our curr_node
    # but we want to start on the next node next time (hence curr_node.next as first argument)
    return zipLinkedList(curr_node.next, curr_node, original_head)
