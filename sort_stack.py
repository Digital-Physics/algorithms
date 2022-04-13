# try recursive next time
# time: O(n**2) we remove every element from the stack first, then need to potentially go through all to insert back
# space: O(n) for the stacks
def sortStack(stack):
    # create another stack in memory to hold the popped items
    # pop items off the stack until empty
    # then reinsert them one at a time while keeping the stack sorted
    # to reinsert, pop until you find one less than or equal to
    # have a side_stack for the reversed sorted stack you put on the side while tyring to insert item into sorted stack
    other_stack = []  # unsorted stack
    side_stack = []  # reverse sorted stack
    sorted = False

    while not sorted:
        print(stack, other_stack, side_stack)
        if not stack:
            sorted = True
        else:
            popped = stack.pop()
            other_stack.append(popped)

    while sorted:
        print(stack, other_stack, side_stack)
        if not other_stack:
            return stack
        if not stack:
            # first item to put on empty but sorted stack
            popped = other_stack.pop()
            stack.append(popped)
            while side_stack:
                side_pop = side_stack.pop()
                stack.append(side_pop)
        else:
            popped = stack.pop()
            if popped <= other_stack[-1]:
                stack.append(popped)
                second = other_stack.pop()
                stack.append(second)
                while side_stack:
                    side_pop = side_stack.pop()
                    stack.append(side_pop)
            else:
                side_stack.append(popped)



