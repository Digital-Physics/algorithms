class linkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def removeKthNodeFromEnd(start: linkedListNode, k: int):
    first_node = start

    # head start
    for _ in range(k):
        first_node = first_node.next

    trailer_node = start

    while first_node.next:
        trailer_node = trailer_node.next
        first_node = first_node.next

    trailer_node.next = trailer_node.next.next

    return start

# 0 -> 1 -> 2 -> 3 -> 4 -> 5
# remove k = 2 
# output:
# 0 -> 1 -> 2 -> 3 -> 5

# 0, 2
# 1, 3
# 2, 4
# 3, 5


if __name__ == "__main__":
    head = linkedListNode(1)
    head.next = linkedListNode(2)
    head.next.next = linkedListNode(3)
    head.next.next.next = linkedListNode(4)
    head.next.next.next.next = linkedListNode(5)

    ll = removeKthNodeFromEnd(head, 2)

    while ll:
        print(ll.val)
        ll = ll.next
        