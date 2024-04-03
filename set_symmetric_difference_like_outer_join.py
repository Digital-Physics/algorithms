# sets can contain and immutable, hashable data type (strings, ints, tuples, frozensets) but not lists

# .add() works on one item where .update() works on an iterable
# .remove(val) will raise an error if val isn't in set, .discard(val) won't
# there is set1.union(set2) and set1.intersection(set2)
# there is set1.difference(set2)
# some of this could be done with iterating over a set of elements and using "if el in set1" etc.

m = int(input())
set1 = set([int(val) for val in input().split()])
n = int(input())
set2 = set([int(val) for val in input().split()])

output = set() # not necessary because unions, intersection, difference, and symmetric_difference\ don't mutate but return a new set
# alternatively
print(*sorted((set1 | set2).difference(set1 & set2)), sep="\n")
print(*sorted((set1 | set2) - (set1 & set2)), sep="\n")
print(*sorted((set1.symmetric_difference(set2))), sep="\n")
print(*sorted(output.union(set1).union(set2).difference(set1.intersection(set2))), sep="\n")
print(*sorted(set1.union(set2).difference(set1.intersection(set2))), sep="\n")