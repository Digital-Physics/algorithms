def natural_nums(n):
    yield n # stops here
    # but if you ask for next() it will recursively call it again, but incremented one higher
    yield from natural_nums(n+1)

def natural_nums2(n):
    while True:
        yield n
        n += 1

successor = natural_nums(0)
gen_obj = natural_nums2(0)

print("type of this function thing with a 'yield' instead of a 'return':", type(successor))

print(next(successor))
print(next(successor))
print(next(successor))
print()
print(next(gen_obj))
print(next(gen_obj))
print(next(gen_obj))

print("the generator function stops at the first yield")
print("but if you ask for more using next(generator_obj), it picks it up where it left off.")
print("with 'yield from' it recursively calls the generator function on a different input, here n+1")
print("'yield from' seems helpful if you have a sub-generator feeding your generator.")

print()
print("a famous algorithm for computing the primes can take advantage of the 'yield from'")
print("this Eratosthenes sieve generator doesn't generate all primes which has an infinite size, just one at a time")
print("and it leverages a sub-generator of natural numbers...")
print("this generator comprehension doesn't sieve out all future multiples of n... but how does it keep track of all previous primes?")
print("for instance, after generating 3, it needs to keep in mind only? 2 to avoid choosing 4, and then yielding at 5")
print("at 5, it only? has to remember 3 to avoid 6 and yield 7")
print("at 7, it only? needs to use 5 to avoid 8... no, it still needs to remember the 2 it generated")

def sieve_of_eratosthenes(natural_num_generator_stream):
    prime = next(natural_num_generator_stream)
    yield prime
    yield from sieve_of_eratosthenes((num for num in natural_num_generator_stream if num%prime != 0))

natural_numbers_generator_stream = natural_nums(2) # first prime
prime = sieve_of_eratosthenes(natural_numbers_generator_stream)

for _ in range(10):
    print(next(prime))