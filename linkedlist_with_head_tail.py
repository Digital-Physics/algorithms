import sys
print(sys.version)

class LinkedListNode:
    def __init__(self, val: int | None) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def append(self, val: int | None) -> None:
        new_node = LinkedListNode(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, val: int | None) -> None:
        new_node = LinkedListNode(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_list(self) -> None:
        current = self.head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage (unchanged)
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend(0)

llist.print_list()