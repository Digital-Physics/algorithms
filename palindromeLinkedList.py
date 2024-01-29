# Input: head = [1,2,2,1]
# Output: true

class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

def isPalindrome(head: LinkedListNode | None) -> bool:
    """This function identifies whether or not the Linked List values form a palindrome."""
    # Naive: traverse the linked list O(n) to make a list
    # set up a left and right index and increment/decrement them until left > right (again O(n))
    # ... but we want a constant space (and making a list will be linear space)

    # 1) slow & fast(2x) pointers allow us to get find the middle (and end at the same step)
    slow, fast = head, head

    while fast is not None and fast.next is not None: #fast needs to look not 
        slow, fast = slow.next, fast.next.next

    # odd length: (e.g. 1->2>3 => slow is at 2 (middle), and fast is at 3 (end) (after one step)
    # even length: 1->2->3->4 => slow is at 3 and fast is at None (tail's next) (after two steps)
        
    # 2) reverse the second half of the linked list starting from essentially the middle (need to keep track of prev since not doubly linked list)
    prev_temp, slow = slow, slow.next

    while slow is not None:
        # flip pointer
        slow.next, prev_temp, slow = prev_temp, slow, slow.next
        # update for next iteration of while loop (no, 3-way or temp var needs to be done like above)
        # prev_temp, slow = slow, slow.next
    
    # 3) now do the normal palindrome check since our weird linked list looks like this 1->2->3<-4<-5
    # prev is at the tail and head is at the head
    backward = prev_temp
    forward = head

    if backward.val != forward.val:
        return False

    while forward.next != backward and forward.next != backward.next: # adjacent cells in the middle checked; only one left to check
        if forward.val != backward.val:
            return False
        
        forward = forward.next 
        backward = backward.next

    return True


headNode = LinkedListNode(4)
headNode.next = LinkedListNode(22)
headNode.next.next = LinkedListNode(22)
headNode.next.next.next = LinkedListNode(4)

print(isPalindrome(headNode))

headNode = LinkedListNode(4)
headNode.next = LinkedListNode(22)
headNode.next.next = LinkedListNode(4)

print(isPalindrome(headNode))

headNode = LinkedListNode(4)
headNode.next = LinkedListNode(22)
headNode.next.next = LinkedListNode(5)

print(isPalindrome(headNode))

headNode = LinkedListNode(4)
headNode.next = LinkedListNode(4)

print(isPalindrome(headNode))

headNode = LinkedListNode(4)
headNode.next = LinkedListNode(5)

print(isPalindrome(headNode))

