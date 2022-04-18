# https://www.pythonmorsels.com/pointers/
# variables are pointers to objects
# some objects like lists are mutable, others like ints are not
# Mutation vs. Assignment
# Mutations change objects; Assignment changes variables and the objects they point to
# Objects don't contain objects; they point to objects
# Data structures like dictionaries and lists contain pointers to objects, not objects themselves


a = [1,2,3]
b = a
b.append(9)
print("1) a and b still point to the same obj since neither a nor b was ever overwritten/redefined/rebound/re-assigned, one was just mutated")
print(a, b)
print()

a = [1,2,3]
b = a
a.append(9)
print("2) a and b still point to the same obj since neither a nor b was ever overwritten/redefined/rebound/re-assigned, one was just mutated")
print(a, b)
print()

a = [1,2,3]
b = a
a = a + [9]
print("3) different; (re)assignment of variable a to point to a new object happened, not a mutation of the previous object a pointed to")
print(a, b)
print()

a = [1,2,3]
b = a
a = [99]
print("4) different; one variable was reassigned to a new object, so now a and b point to different objects")
print(a, b)
print()

a = 10
b = a
a = a + 99 # same situation with += 99 (both operators cannot mutate the int(10) object; they re-assign a to a new object
print("5) different; one variable was reassigned (you cannot mutate the int object a points to) to a new object")
print("...so now a and b point to different objects")
print(a, b)
print()

print("rule to avoid errors (or deep copy usage):")
print("question: is the object mutable?")
print("question: are you using the variable as a temp variable? Or do you need the object to persist in memory to the eventual output?")
print("problem: if you are using = as a way to get a starting object from which you will mutate it (and you still need the original object)")
print("it is ok to set one variable equal to another if either object will later be re-assigned")
print("if a variable is reassigned (not mutated) the pointers will then point to different objects")

print("note: appending is mutating")
print("note: popping is mutating")
print("note: concatenation is reassigning")

width = 10
height = 5
area = width*height
print(area)
width = 20
print(area)
# need to reassign area or else it will point to the old version of width in memory
print("if a variable is reassigned (not mutated) the pointers will then point to different objects. one will point to the stale version.")
print("also, area is fully evaluated up front is just pointing to the int(50) object")
area = width*height
print(area)