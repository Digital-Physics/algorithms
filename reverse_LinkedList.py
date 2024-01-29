class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

def reverse_linked_list(head: Node) -> Node:
    """takes in a head node and returns the head node of that linked list reversed.
    it traverses once, flipping it's next pointer along the way. 1->2->3 => 3->2->1 (or 1<-2<-3)"""
    prev = None # visually, prev is to the left, next to the right (1 -> 2 -> 3 -> 4 -> 5)
    curr_node = head

    while curr_node is not None:
        next_node = curr_node.next # COPY before the flip overwrites it

        # this is the main function to apply to each node
        curr_node.next = prev # FLIP .next pointer on curr node (now that you copied the node the pointer pointed to)
        
        # initialize for next iteration now that the FLIP is done
        prev = curr_node # update "node on the left" for the next node to point to
        curr_node = next_node # for next iteration of loop (from start of loop)

    return prev


# Linear time (in the size of the linked list) O(n) and constant space alogrithm O(1)   
class Node2:
    def __init__(self, value: int):
        self.value = value
        self.next = None

def rev_linked_list(head: Node2) -> Node2:
    curr_node = head
    prev_curr_node = None

    while curr_node is not None:
        # copy
        next_node_to_process = curr_node.next 
        # next_node ----> Node obj 0x123
        # curr_node.next ---> Node obj 0x123

        # flip pointer
        curr_node.next = prev_curr_node 
        # (var was redefined, overwritten, not mutated)
        # next_node ----> Node obj 0x123
        # curr_node.next ---> None 

        # update for next iteration of the while loop
        prev_curr_node = curr_node
        curr_node = next_node_to_process

    return prev_curr_node


def rev_linked_list2(head: Node2) -> Node2:
    curr_node = head
    prev_curr_node = None

    while curr_node is not None:
        # flip pointer and redefine node in one line (not needed but...)
        next_node_to_process, curr_node.next = curr_node.next, prev_curr_node
    
        # redefine vars for next iteration of the while loop
        prev_curr_node, curr_node = curr_node, next_node_to_process

    return prev_curr_node


def too_ambitious_rev_linked_list3(head: Node2) -> Node2:
    curr_node = head
    prev_curr_node = None

    while curr_node is not None:
        # a one-liner won't work becuase you are overwriting curr_node.next info before it is used
        # redefine for for next loop, flip pointer and flip pointer???
        # prev_curr_node, curr_node, curr_node.next = curr_node, curr_node.next, prev_curr_node
        curr_node.next, prev_curr_node, curr_node = prev_curr_node, curr_node, curr_node.next

    return prev_curr_node
        

# Example usage:
# Assuming you have a linked list with nodes: 1 -> 2 -> 3 -> 4 -> 5
# Create the linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Reverse the linked list
new_head = too_ambitious_rev_linked_list3(head)

# Print the reversed linked list
while new_head is not None:
    print(new_head.value, end=" ")
    new_head = new_head.next