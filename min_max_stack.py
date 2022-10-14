from __future__ import annotations


# time: O(1) constant time
# space: O(1) constant space
class MinMaxStack:
    def __init__(self) -> None:
        """this function will have a 3-tuple of values at each layer of the stack:
        [min through this number in the stack, max through this number at this height of the stack, number]"""
        # storing this info allows us constant time methods; we don't need to take min/max over unsorted stack
        self.min_max_stack = []

    def peek(self) -> int | float | None:
        return self.min_max_stack[-1][2] if self.min_max_stack else None

    def pop(self) -> int | float | None:
        return self.min_max_stack.pop()[2] if self.min_max_stack else None

    def push(self, number: int | float) -> None:
        if self.min_max_stack:
            next_el = (min(self.get_min(), number), max(self.get_max(), number), number)
        else:
            next_el = (number, number, number)

        self.min_max_stack.append(next_el)

    def get_min(self) -> int | float | None:
        return self.min_max_stack[-1][0] if self.min_max_stack else None

    def get_max(self) -> int | float | None:
        return self.min_max_stack[-1][1] if self.min_max_stack else None


test_min_max_stack = MinMaxStack()
test_min_max_stack.push(7)
test_min_max_stack.push(6.5)
print(test_min_max_stack.get_max(), test_min_max_stack.get_min())
test_min_max_stack.pop()
print(test_min_max_stack.peek())
test_min_max_stack.push(3.5)
print(test_min_max_stack.get_min())
test_min_max_stack.pop()
test_min_max_stack.pop()
test_min_max_stack.pop()
test_min_max_stack.pop()
test_min_max_stack.pop()
test_min_max_stack.pop()
print(test_min_max_stack.get_max())
