n = int(input())
tup = tuple((int(val) for val in input().split()))
# print(tup, type(tup))

# all immutable types like tuples, int, float, str, and frozenset can be hashed
# mutable types like list, set, dict cannot be hashed
print(hash(tup))
