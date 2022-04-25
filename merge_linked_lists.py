# time: O(n+m) ?
# space: O(1) ?
# Clement used three variables as opposed to looking one ahead (to save curr_node for changing .next on)
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    if headOne.value < headTwo.value:
        in_place_node = headOne
        other_node = headTwo
        return_head = headOne
    else:
        in_place_node = headTwo
        other_node = headOne
        return_head = headTwo

    while other_node is not None:
        print()
        if in_place_node.next is None:  # handling edge case
            print("add the rest of the other_node list")
            last_in_place_node = in_place_node
            while other_node is not None:
                print("add", other_node.value)
                last_in_place_node.next = other_node
                last_in_place_node = last_in_place_node.next
                other_node = other_node.next

            print("final list:")
            curr_node = return_head
            while curr_node is not None:
                print(curr_node.value)
                curr_node = curr_node.next
            return return_head

        print("in-place & one-step-ahead-in-place pointer values", in_place_node.value, in_place_node.next.value)
        print("other list node pointer value", other_node.value)
        if in_place_node.next.value <= other_node.value:
            # increment through in-place list
            if in_place_node.next.next is not None:
                in_place_node = in_place_node.next
            else:
                print("add the rest of the other_node list")
                last_in_place_node = in_place_node.next
                while other_node is not None:
                    print("add", other_node.value)
                    last_in_place_node.next = other_node
                    last_in_place_node = last_in_place_node.next
                    other_node = other_node.next

                print("final list:")
                curr_node = return_head
                while curr_node is not None:
                    print(curr_node.value)
                    curr_node = curr_node.next
                return return_head
        else:
            next_other_node = other_node.next
            # get new pointer ready for insert after in-place node
            other_node.next = in_place_node.next
            # insert node, and increment other_node pointer
            in_place_node.next, other_node = other_node, next_other_node

    print("final list:")
    curr_node = return_head
    while curr_node is not None:
        print(curr_node.value)
        curr_node = curr_node.next
    return return_head



