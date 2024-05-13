def calculate(s: str) -> int:
    """evaluate a sting with a basic algebraic equation (+,-,*,/ operators and (,) too) without using eval().
    we'll create a stack of numbers to sum and also recursively call calculate() when we find an open parenthesis"""

    def update_stack(op, x):
        """creates a stack of things to sum up. 
        This is already done for "+ x" and "- x" as we iterate through the list.
        For "w * x", we'll have to pop the last number off the stack and then push/append the product on.
        """
        nonlocal stack_to_sum  # should only look up one context level and shouldn't mess with our recursion 

        if op == "+": 
            stack_to_sum.append(x)
        if op == "-": 
            stack_to_sum.append(-x)
        if op == "*": 
            stack_to_sum.append(stack_to_sum.pop() * x)           
        if op == "/": 
            stack_to_sum.append(int(stack_to_sum.pop() / x))      

    i = 0
    num = 0
    stack_to_sum = []
    operator = "+" # the first num to put on the stack implicitly was preceded by a + operator (we only put numbers on the stack when we see the next operator, but we use the previous operator)
    
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] in "+-*/":
            update_stack(operator, num) # we pass the last symbol we saved
            num = 0
            operator = s[i] # update for next time; remembering the last symbol we've seen will be helpful when we have to put something on the stack
        elif s[i] == "(":                                        
            sum_of_recursive_stack, end_idx = calculate(s[i + 1:])  # recursive call through the end of the string, but we'll return the ending index to pick up at
            num = sum_of_recursive_stack
            i = i + end_idx
        elif s[i] == ")":  # end the recursive call (by returning the sum of its stack & where to pick up after the ")")                                
            update_stack(operator, num)
            return sum(stack_to_sum), i + 1
        # notice we'll implicitly just skip over spaces " "
        i += 1

    # handle whatever num is open and not put on the stack (with the last symbol operator)
    update_stack(operator, num)

    return sum(stack_to_sum)

if __name__ == "__main__":
    print(calculate("(3*4 + 2)/(6 + 1) - 5"))
    print(calculate("10 0 * 3")) # note: this function accommodates incorrect syntax


