class LinkedListNode:
    def __init__(self, val: int | None) -> None:
        self.val = val
        self.next = None

def getDec(head: LinkedListNode | None) -> int:
    total = 0
    curr_node = head

    while curr_node is not None:
        total = 2*total + curr_node.val

        curr_node = curr_node.next

    return total

headNode = LinkedListNode(1)
headNode.next = LinkedListNode(0)
headNode.next.next = LinkedListNode(0)
headNode.next.next.next = LinkedListNode(1)
headNode.next.next.next.next = LinkedListNode(0)

print(getDec(headNode))

