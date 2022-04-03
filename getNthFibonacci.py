# Time: O(n)
# Space: O(1)

# Naive: O(2**n) time and O(n) space because there is a branching binary tree of function calls put on the stack
# Function call stack gets built from going down left side until it hits bottom
# i.e. f(n) = f(n-1) + f(n-2)

# iterative while loop version
def getNthFib(n):
    idx = 1
    penultimate = 0
    last = 1

    def nextFibHelp(last, penultimate):
        last, penultimate = penultimate + last, last
        return last, penultimate

    while idx < n:
        last, penultimate = nextFibHelp(last, penultimate)
        idx += 1

    return penultimate

# is this tail recursion? the last call returns just one function call not two like
# time complexity is O(n) and not O(2**n)
# but even tail-recursion has more space complexity, O(n), because build up of call function frames on the stack
def getNthFib2(n):
    def nextFibHelp(n, last=1, penultimate=0, idx=1):
        if idx < n:
            return nextFibHelp(n, last + penultimate, last, idx + 1)
        else:
            return penultimate  # slightly bad name convention

    return nextFibHelp(n)

# there is also a memoization approach too where a dictionary/hash table is used to memoize
# but the fixed-memory iterative while loop which just stores the last two values is the best for time and space complexity

