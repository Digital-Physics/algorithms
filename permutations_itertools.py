from itertools import permutations

string, k = input().split(" ")
k = int(k)

# Permutations are printed in a lexicographic sorted order. 
# So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
# we thought we might want unique letters so we ran it through set()
list_of_letters = sorted(list(set([*string])))
# list_of_letters = sorted([*string])

# k-tuple is a permutation (e.g. ('A', 'C', 'D'))
print(*["".join(tup) for tup in permutations(list_of_letters, k)], sep="\n")


