# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # time: O(1)
    # space: O(1)
    def setHead(self, node):
        if self.head is None:  # empty linkedList
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)

    # time: O(1)
    # space: O(1)
    def setTail(self, node):
        if self.tail is None:  # empty linkedList
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)

    # time: O(1)
    # space: O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return  # nothing to do, so return exits

        # handles two cases: whether in the list or not
        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        # do you need to update head references?
        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert
        node.prev = nodeToInsert

    # time: O(1)
    # space: O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return  # nothing to do, so return exits

            # handles two cases: whether in the list or not
        self.remove(nodeToInsert)

        nodeToInsert.prev = node
        nodeToInsert.next = node.next

        # do you need to update tail references?
        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert
        node.next = nodeToInsert

    # time: O(p) where p is position
    # space: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
        else:
            curr_node = self.head
        counter = 1  # index of linked list starts at 1 not 0

        while curr_node is not None and counter != position:
            counter += 1
            curr_node = curr_node.next

        if curr_node is not None:
            self.insertBefore(curr_node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)

    # time: O(n)
    # space: O(1)
    def removeNodesWithValue(self, value):
        curr_node = self.head

        while curr_node is not None:
            # save before we remove
            next_node = curr_node.next

            if curr_node.value == value:
                self.remove(curr_node)

            curr_node = next_node

    # time: O(1)
    # space: O(1)
    def remove(self, node):
        # check to see if node is head and/or tail
        if self.head == node:
            self.head = self.head.next
            print("head updated")
        if self.tail == node:
            self.tail = self.tail.prev

        # update bindings on three nodes
        self.updateBindings(node)

    # time: O(n)
    # space: O(1)
    def containsNodeWithValue(self, value):
        curr_node = self.head

        while curr_node is not None:
            if curr_node.value == value:
                return True
            else:
                curr_node = curr_node.next

        return False

    def updateBindings(self, node):
        # update adjacent nodes
        if node.prev is not None:
            print("previous's next updated")
            node.prev.next = node.next
        if node.next is not None:
            print("next's previous updated")
            node.next.prev = node.prev
        # updated node
        node.prev, node.next = None, None

