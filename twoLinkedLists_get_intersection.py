from typing import Optional

class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

# Linear time & constant auxiliary/total space 
def getIntersectionNode(headA: LinkedListNode, headB: LinkedListNode) -> Optional[LinkedListNode]:
    curr_nodeA = headA
    curr_nodeB = headB

    seen = set()

    while curr_nodeA is not None or curr_nodeB is not None:
        if curr_nodeA is not None:
            if curr_nodeA in seen:
                return curr_nodeA
            
            seen.add(curr_nodeA)
            curr_nodeA = curr_nodeA.next  
            
        if curr_nodeB is not None:
            if curr_nodeB in seen:
                return curr_nodeB
            
            seen.add(curr_nodeB)  
            curr_nodeB = curr_nodeB.next 


headNodeA = LinkedListNode(2)
headNodeB = LinkedListNode(44)

headNodeA.next = LinkedListNode(2)
headNodeB.next = LinkedListNode(5)

headNodeA.next.next = LinkedListNode(2)
headNodeB.next.next = LinkedListNode(5)

headNodeA.next.next.next = LinkedListNode(2)
headNodeA.next.next.next.next = LinkedListNode(55)
headNodeA.next.next.next.next.next = LinkedListNode(2)
headNodeB.next.next.next = headNodeA.next.next.next.next

print(getIntersectionNode(headNodeA, headNodeB).val)

#what is the opposite of .add() method on set? .remove()?
print(dir(set()))





