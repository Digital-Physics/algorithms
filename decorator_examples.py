from functools import cache
# https://www.youtube.com/watch?v=JgxCY-tbWHA

# example #1
# @property decorator for private, read-only attributes
class Circle:
    def __init__(self, radius):
        self._radius = radius # the _ before indicates it will be used as a private attribute

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            # raise Exception("Not right")
            raise ValueError("Radius must be positive.")
    
    # @radius.deleter
    # def radius(self):
    #     del self._radius
        
    @property
    def diameter(self):
        return self._radius * 2
    
c = Circle(5)
print(c.radius, c.diameter)

# c.radius = -1
c.radius = 10

print(c.radius)
print(c.diameter)

# del c.radius
# print(c.diameter)


# example #2
# @staticmethod decorator for methods that are not specific to an instance

class Math:
    @staticmethod
    def add(x, y): # Note: because we don't need the instance, we don't pass self as first argument
        return x + y
    
    @staticmethod
    def multiply(x, y):
        return x*y
    
print(Math.add(3, 4)) # notice how I can call the class method without creating an instance first
print(Math.multiply(3, 4))


# example 3
# @classmethod decorators for getting things associated with a class not an instance
# Note: unlike @staticmethod, @classmethod can access attributes of the class

class Person:
    species = "homo sapiens"

    @classmethod
    def get_species(cls):
        print(cls)
        return cls.species
    
print(Person.get_species()) # again, no instance needed to be created first

# example 4
# @functools.cache is an easy way to implement a memoized cache (e.g. def fib(n, memo={}))
@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# example 5
# @dataclass decorator is for storing data in a class without implementing __init__, __eq__, __repr__
# see dataclasses_library.py file

# example 6
# simple decorator example
def with_greeting(func):
    def wrapper(*args, **kwargs):
        print("Hello World!")
        return func(*args, **kwargs)
    
    return wrapper

@with_greeting
def add(x, y):
    """this is a doc string of my function"""
    return x + y

print("when add function is called, it actually calls the wrapper function now")
print(add(5, 6))
print(add.__name__)
print(add.__doc__)

