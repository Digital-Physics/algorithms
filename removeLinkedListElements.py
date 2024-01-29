# Input: head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]

class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

# linear time and constant auxialiary and total space
def remove_linked_list_elements(head: LinkedListNode | None, value: int) -> LinkedListNode | None:
    headNodeToReturn = head
    curr_node = head
    prev = None

    while curr_node is not None:
        if curr_node.val == value:
            if prev is not None:  # not head
                prev.next = curr_node.next
            else: # curr_node is head
                headNodeToReturn = curr_node.next

            # prev remains prev since we are removing
            curr_node = curr_node.next
        else:       
            prev, curr_node = curr_node, curr_node.next

    return headNodeToReturn


headNode = LinkedListNode(4)
headNode.next = LinkedListNode(22)
headNode.next.next = LinkedListNode(22)
headNode.next.next.next = LinkedListNode(4)

newHead = remove_linked_list_elements(headNode, 22)

print(newHead.val, newHead.next.val)

headNode = LinkedListNode(4)
headNode.next = LinkedListNode(22)
headNode.next.next = LinkedListNode(22)
headNode.next.next.next = LinkedListNode(4)

newHead2 = remove_linked_list_elements(headNode, 4)
print(newHead2.val, newHead2.next.val)