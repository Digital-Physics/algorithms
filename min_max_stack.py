# time: O(1) constant time!
# space: O(1) constant space!
class MinMaxStack:
    def __init__(self):
        # will hold stacks of [min here & below, max here & below, number]
        # storing this info allows us constant time methods
        # we do not have to compute min & max after popping through looking at nums in a unsorted stack
        self.min_max_stack = []

    def peek(self):
        return self.min_max_stack[-1][2]

    def pop(self):
        pop = self.min_max_stack.pop()

        return pop[2]

    def push(self, number):
        if len(self.min_max_stack) == 0:
            temp = [number, number, number]
        else:
            temp = [self.getMin(), self.getMax(), number]

            if number < temp[0]:
                temp[0] = number
            elif number > temp[1]:
                temp[1] = number

            temp[2] = number

        self.min_max_stack.append(temp)

    def getMin(self):
        return self.min_max_stack[-1][0]

    def getMax(self):
        return self.min_max_stack[-1][1]
