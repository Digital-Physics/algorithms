from typing import Optional, List
import heapq # for prioritizing next node to choose, k could be big so we can get the best in log time (for inserting and removing) instead of linear
from copy import deepcopy # used to copy nodes for second test case (because first test case will mutate their .next pointers)

class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    # heapq doesn't have a key= argument like sorted() and .sort()
    # heapq is trying to compare the second element in the tuple for tie breaks, which is a ListNode, using "<" and "=="
    # to accommodate heapq, we'll define how "<" operator should work on the two operands
    # and now that we've done this, we might as well just store the node itself in the heap
    def __lt__(self, other):
        return self.val < other.val
    
    # def __eq__(self, other):
    #     return self.val == other.val

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """turn k sorted LL to one sorted LL"""
    min_heap = [] # next best
	
    dummy_head = tail = ListNode(0) # dummy head; tail is a temp dummy that will get changed
	
    # start the priority queue, min heap, with the k liked list nodes (heads)
    for head_node in lists:
        if head_node:
            heapq.heappush(min_heap, (head_node.val, head_node))
    
    while min_heap:
        node_to_add = heapq.heappop(min_heap)[1]
        
        # add to and the tail, and then update the tail pointer
        tail.next = node_to_add
        tail = tail.next
        
        if node_to_add.next: # add that linked list's next node that has been exposed to the priority queue of candidates (in log time)
            heapq.heappush(min_heap, (node_to_add.next.val, node_to_add.next))
    
    return dummy_head.next

def mergeKLists2(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """turn k sorted LL to one sorted LL. in this version, we just store the node in the heap 
    since we've now defined how to compare it using '<' which the heap needs"""
    min_heap = [] # next best
	
    dummy_head = tail = ListNode(0) # dummy head; tail is a temp dummy that will get changed
	
    # start the priority queue, min heap, with the k liked list nodes (heads)
    for head_node in lists:
        if head_node:
            heapq.heappush(min_heap, head_node)
    
    while min_heap:
        node_to_add = heapq.heappop(min_heap)
        
        tail.next = node_to_add
        tail = tail.next
        
        if node_to_add.next:
            heapq.heappush(min_heap, node_to_add.next)
    
    return dummy_head.next

if __name__ == "__main__":
    ll1 = ListNode(1)
    ll1.next = ListNode(4)
    ll1.next.next = ListNode(5)

    ll2 = ListNode(1)
    ll2.next = ListNode(3)
    ll2.next.next = ListNode(4)

    ll3 = ListNode(2)
    ll3.next = ListNode(6)

    list_of_ll = [ll1, ll2, ll3]
    list_of_ll2 = [deepcopy(node) for node in list_of_ll]

    node = mergeKLists(list_of_ll)
    while node:
        print(node.val)
        node = node.next

    node2 = mergeKLists2(list_of_ll2)
    while node2:
        print(node2.val)
        node2 = node2.next

        