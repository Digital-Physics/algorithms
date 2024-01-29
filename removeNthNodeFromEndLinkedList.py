class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


def removeNthLast(head: LinkedListNode | None, n: int) -> LinkedListNode | None:
    """Removes the nth element form the tail and returns the head."""
    #first strategy: flip the .next as we go through first time. Then use a counter from the tail and flip back. remove element when found. end at head.
    # linear time, but two passess. can you do it in one pass?

    # strategy #2: fast node is always n steps ahead of slow node. stop at tail, remove slow, return head
    # fast id not a 2x fast, but a n step head start fast
    slow, fast = head, head

    for _ in range(n):
        fast = fast.next

    if fast is None:
        # implicitly removes head 
        return head.next
    
    while fast.next is not None:
        # it almost feels like we need a prev, but we are going to change .next since while loop is looking ahead
        slow, fast = slow.next, fast.next

    slow.next = slow.next.next

    return head


headNode = LinkedListNode(1)
headNode.next = LinkedListNode(2)
headNode.next.next = LinkedListNode(3)

newHead = removeNthLast(headNode, 2)

print(newHead.val, newHead.next.val)


