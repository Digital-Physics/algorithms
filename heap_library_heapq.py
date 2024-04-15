import heapq

# Create an empty heap
heap = []

# Push elements onto the heap
heapq.heappush(heap, 5)
heapq.heappush(heap, 3)
heapq.heappush(heap, 7)
heapq.heappush(heap, 1)

print("Heap after pushing elements:", heap)

# Pop the smallest element from the heap
smallest = heapq.heappop(heap)
print("Smallest element popped from the heap:", smallest)
print("Heap after popping smallest element:", heap)

# Push a new element onto the heap
heapq.heappush(heap, 2)
print("Heap after pushing a new element (2):", heap)

# lesson 2:
# if you have a list to start, you can turn it into a min-heap in terms
# of obeying the parent < children with the heapify function

# Create a list
lst = [5, 3, 7, 1, 2]
print("original list", lst)

# Convert the list into a heap, in place
heapq.heapify(lst)

print("Heapified list:", lst)

# lesson 3:
# heapq only provides functions for creating and manipulating min-heaps. 
# max-heap can be made with negation.

# Create a list
lst = [5, 3, 7, 1, 2]
print("original list", lst)

# Negate the values to simulate a max-heap
negated_lst = [-x for x in lst]

# Convert the negated list into a heap
heapq.heapify(negated_lst)

print("Max-heapified list:", negated_lst)

# Pop the largest element (which was the negated smallest element)
largest = -heapq.heappop(negated_lst)
print("Largest element popped from the max-heap:", largest)

# lesson 4:
# what if you want to key off a value associated with some object
# can we do something similar to how we use key with sorted() and .sort()?

class MyObject:
    def __init__(self, number, string):
        self.number = number
        self.string = string

    def __lt__(self, other): # __lt__ overloads the < operator 
        if self.number == other.number:
            return self.string < other.string # sort alphabetically 
        return self.number < other.number

# Create a list of objects
objs = [
    MyObject(5, "apple"),
    MyObject(7, "kiwi"),
    MyObject(3, "orange"),
    MyObject(3, "banana"),
    MyObject(5, "pear")
]

# Use a list comprehension to create a tuple for each object
# with the number as the first element, string as the second element, and the object itself as the third element
# although this doesn't explicitly use the key parameter, putting sorted categories
# in a tuple with the first one being the most significant, is like key=lambda x: (x.value, x.other_attribute_to_sort_by_in_event_of_tie_on_value)
heap = [(obj.number, obj.string, obj) for obj in objs]
print("list of tuples containing objects and the values we want to create a priority queue/heap from", heap)
heapq.heapify(heap)
print("after heapifying the tuples", heap)

# Extract the objects from the heap
# Note: the heap may have an order, but when we start popping them off they'll come in sorted order
# because under the hood it is sifting down (the last leaf value (last item in list) put at the root (index 0))
result = [heapq.heappop(heap)[2] for _ in range(len(heap))]

# Print the sorted objects.
for obj in result:
    print(obj.number, obj.string, end=' ')

# lesson 5:
# can we do this without messing around with __lt__ and overloading the < operator?

class MyObject2:
    def __init__(self, number, string):
        self.number = number
        self.string = string

# Create a list of objects
objs = [
    MyObject2(5, "apple"),
    MyObject2(3, "banana"),
    MyObject2(7, "kiwi"),
    MyObject2(3, "orange"),
    MyObject2(5, "pear")
]

heap = [(obj.number, obj.string, obj) for obj in objs]
heapq.heapify(heap)

# Extract the objects from the heap
result = [heapq.heappop(heap)[2] for _ in range(len(heap))]

# Print the sorted objects
print()
for obj in result:
    print(obj.number, obj.string, end=' ')
print()