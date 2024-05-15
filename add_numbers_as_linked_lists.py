from typing import Optional

class ListNode:
    def __init__(self, val: int, next: Optional["ListNode"] = None) -> None:
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head: Optional[ListNode] = None, tail: Optional[ListNode] = None) -> None:
        self.head = head
        self.tail = tail

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """add two numbers represented as linked lists and return the answer as a linked list in the same form.
    the numbers are in reverse order, from least significant to most significant, which makes it easier."""
    
    curr_num_node1 = l1
    curr_num_node2 = l2
    carry_digit = 0
    ll_output = LinkedList()

    while curr_num_node1 or curr_num_node2 or carry_digit > 0:
        num1 = curr_num_node1.val if curr_num_node1 else 0
        num2 = curr_num_node2.val if curr_num_node2 else 0

        value = num1 + num2 + carry_digit

        if value > 9:
            carry_digit = 1
        else:
            carry_digit = 0

        output_node = ListNode(value % 10)

        if ll_output.head is None:
            ll_output.head = output_node
            ll_output.tail = output_node
        
        ll_output.tail.next = output_node
        ll_output.tail = output_node  

        curr_num_node1 = curr_num_node1.next if curr_num_node1 else None
        curr_num_node2 = curr_num_node2.next if curr_num_node2 else None

    return ll_output.head

if __name__ == "__main__":
    number1 = ListNode(1)
    number1.next = ListNode(2)

    number2 = ListNode(2)
    number2.next = ListNode(9)
    number2.next.next = ListNode(4)

    output = addTwoNumbers(number1, number2)
    print(output)

    while output:
        print(output.val)
        output = output.next