# time: O(max(n,m)) where n, m are list lengths
# space: O(max(n,m)) (we just return the head, but we do put all these nodes in memory)
# Tim's algo is more elegant with respect to the is-not-None checks in one line
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    curr_node1 = linkedListOne
    curr_node2 = linkedListTwo

    remainder = 0
    previous_node = None

    while curr_node1 is not None or curr_node2 is not None or remainder != 0:
        print()
        if curr_node1 is not None:
            print("curr_node1 from LinkedListOne:", curr_node1.value)
        if curr_node2 is not None:
            print("curr_node2 from LinkedListTwo:", curr_node2.value)
        print("remainder:", remainder)
        if previous_node is not None:
            print("Previous Node's value (no .next yet):", previous_node.value)

        if curr_node1 is not None and curr_node2 is not None:
            new_node = LinkedList((curr_node1.value + curr_node2.value + remainder) % 10)
        elif curr_node1 is not None:
            new_node = LinkedList((curr_node1.value + remainder) % 10)
        elif curr_node2 is not None:
            new_node = LinkedList((curr_node2.value + remainder) % 10)
        elif remainder != 0:
            new_node = LinkedList((remainder) % 10)

        if previous_node is not None:
            previous_node.next = new_node
        else:  # save head
            head = new_node

        remainder = 0
        if curr_node1 is not None and curr_node2 is not None:
            if 20 > curr_node1.value + curr_node2.value + remainder > 9:
                remainder = 1
            elif curr_node1.value + curr_node2.value + remainder >= 20:
                remainder = 2
        elif curr_node1 is not None:
            if 20 > curr_node1.value + remainder > 9:
                remainder = 1
            elif curr_node1.value + remainder >= 20:
                remainder = 2
        elif curr_node2 is not None:
            if 20 > curr_node2.value + remainder > 9:
                remainder = 1
            elif curr_node2.value + remainder >= 20:
                remainder = 2

        # update for next round
        previous_node = new_node
        if curr_node1 is not None:
            curr_node1 = curr_node1.next
        if curr_node2 is not None:
            curr_node2 = curr_node2.next

    return head



