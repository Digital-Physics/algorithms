class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

def mergeLL(list1: LinkedListNode, a: int, b: int, list2: LinkedListNode) -> LinkedListNode:
    headstart = b - a
    slow = fast = list1
    prev = None

    for _ in range(headstart): 
        fast = fast.next

    for _ in range(a):
        prev, slow, fast = slow, slow.next, fast.next

    if prev is not None:
        prev.next = list2 
    else:
        list1 = list2

    # get to node at end of inserted linked list
    while list2.next is not None:
        list2 = list2.next

    # list2 is tail now
    list2.next = fast.next

    return list1

listHead1 = LinkedListNode(0)
listHead1.next = LinkedListNode(1)
listHead1.next.next = LinkedListNode(2)
listHead1.next.next.next = LinkedListNode(3)
listHead1.next.next.next.next = LinkedListNode(4)

listHead2= LinkedListNode(11)
listHead2.next = LinkedListNode(22)

newListHead = mergeLL(listHead1, 2, 3, listHead2)
print(newListHead.val, newListHead.next.val, newListHead.next.next.val, newListHead.next.next.next.val, newListHead.next.next.next.next.val, newListHead.next.next.next.next.next)
