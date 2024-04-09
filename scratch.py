from collections import Counter

print(Counter("aabbbccd").most_common(3))


print("python is case sensitive")
print("A" == "a", "A" == "A")

print(".title() capitalizes the first character in every word. Good to know? I'm not sure.")
print("jonathan", "jon".title(), "jon".upper(), "JoN".lower())

string = "   hello, world   "
print(string.capitalize())  # Output:    Hello, world
print(string.upper())       # Output:    HELLO, WORLD
print(string.lower())       # Output:    hello, world
print(string.title())       # Output:    Hello, World
print(string.strip())       # Output: hello, world

string = "hello, world"
print(string.replace("world", "Python"))  # Output: hello, Python

print(string.split(", "))   # Output: ['hello', 'world']

words = ["hello", "world"]
print(", ".join(words))     # Output: hello, world

string = "hello, world"
print(string.find("world"))    # Output: 7
print(string.index("world"))   # Output: 7, like find() but raises error if not found
print(string.count("l"))       # Output: 3
print(string.isalnum())        # Output: False
print("123".isdigit())         # Output: True
print("hello".isalpha())       # Output: True
print("   ".isspace())         # Output: True
print(string.startswith("hello"))  # Output: True
print(string.endswith("world"))    # Output: True

print([(x,y) for x in range(10, -1, -1) for y in range(5, -1, -1)])
print([[(x,y) for x in range(10, -1, -1)] for y in range(5, -1, -1)])

a_string = "helloThere"
print([*a_string])
# print(a_string.split()) # wrong
# print(a_string.split("")) # wrong