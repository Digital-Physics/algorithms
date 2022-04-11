# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# time: O(n)
# space: O(1)
def removeKthNodeFromEnd(head, k):
    counter = 1  # for lag node
    k_step_lag_node = head  # stops one before the node we want to remove
    curr_node = head

    while counter <= k:
        counter += 1
        curr_node = curr_node.next

    if curr_node is None:  # end of list; lag node should be removed now (and it's the head)
        print("remove head; edge case, be careful")
        head.value = head.next.value
        head.next = head.next.next
    else:
        # by looking one step out, this stops the lag node one step before the node we want to remove
        # this allows us to update our .next pointer from previous node to skip over removal node
        while curr_node.next is not None:
            # increment both since we are beyond k
            curr_node = curr_node.next
            k_step_lag_node = k_step_lag_node.next

        print("normal middle-of-the-list removal")
        k_step_lag_node.next = k_step_lag_node.next.next