# time: O(n) to go through each character and do constant time operations
# space: O(n) for the stack build up
def balancedBrackets(string):
    stack = []
    match_dict = {
        ")": "(",
        "]": "[",
        "}": "{"}

    for i in range(len(string)):
        if string[i] in [")", "]", "}"]:
            if len(stack) == 0:
                return False
            else:
                popped = stack.pop()
                if match_dict[string[i]] != popped:
                    return False
        elif string[i] in ["(", "[", "{"]:
            stack.append(string[i])

    return False if stack else True
