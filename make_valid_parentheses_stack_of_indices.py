def minRemoveToMakeValid(s: str) -> str:
    """remove the minimum number of parentheses to create a valid string...
    open and closed parentheses matching can be done with stacks... pushing left ones onto the stack and popping right ones off the stack.
    but here we'll push the indices so we can go back and remove open parentheses..."""

    # we have two bad situations and each of them always need to be removed... 
    # 1) closing parentheses that don't have a start (i.e. there's an empty stack when you see a ")") 
    # (note: we aren't allowed to add characters, i.e. an open "(" before it, so we HAVE to remove it.)
    # 2) an open parenthesis "(" never finds a ")" (we'll only know this after going through the complete string once and popping all the ones that have matches)
    parentheses_stack = []

    # we're going to want to mutate characters (make "") when something doesn't close right, and you can't mutate a string
    s = [*s] 

    for i, character in enumerate(s):
        if character == "(":
            # instead of putting the "(" on the stack, we put the idx on so we can know to clear it in step #2
            # if we didn't need step #2, we could put anything on the stack because there is only one type of parentheses (essentially a counter)
            # if we have more than one type of parentheses (i.e. "{", "[", "("), we could put tuples on the stack (i, "{")
            parentheses_stack.append(i)
        elif character == ")":
            if parentheses_stack:
                parentheses_stack.pop()
            else: # deal w/ issue # 1
                s[i] = ""
    
    # deal w/ issue # 2
    while parentheses_stack:
        s[parentheses_stack.pop()] = ""
    
    return "".join(s)


if __name__ == "__main__":
    print(minRemoveToMakeValid("lee(t(c)o)de)"))