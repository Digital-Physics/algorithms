# Input: head = [1,2,3,4,5]
# Output: 3
# Input: head = [1,2,3,4,5,6]
# Output: 4

class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

# linear time and constant memory
def middleOfLinkedList(head: LinkedListNode | None) -> LinkedListNode | None:
    """this returns the middle node of a linked list if an odd length or right-middle if an even length."""
    fast, slow = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next 

    return slow


        
