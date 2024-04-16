from dataclasses import dataclass
# for more advanced: https://www.youtube.com/watch?v=5mMpM8zK4pY

@dataclass
class Point:
    x: int = 0
    y: int = 0

# fills in the following dunder/magic methods
# __init__   (initializing)
# __repr__   (for string representation in the terminal)
# __eq__   (for overloading = operator and defining equality for this object)

p1 = Point(4, 5)
p2 = Point(4, 5)

print(p1)
print(p1 == p2)

