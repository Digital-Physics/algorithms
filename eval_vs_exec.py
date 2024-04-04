x = 1

# returns something
print("eval() takes an expression in a str that evaluates to something and returns it")
print(eval("x + 1"), "is like", x+1)

# returns nothing
print("exec() executes code, but doesn't return anything.")
print(exec("y = 1"), y)

