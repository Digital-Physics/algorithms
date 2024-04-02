from itertools import combinations

# >>> A = [1,1,3,3,3]
# >>> print list(combinations(A,4))
# [(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]

string, k = input().split(" ")
k = int(k)

sorted_list = sorted([*string])

# all possible up to size k
# careful on the for loop order; we initially got i not being defined 
# this code is equivalent to:
# for i in range(k):
#     for tup in combinations(sorted_list, i + 1):
#         print("".join(tup))
print(*["".join(tup) for i in range(k) for tup in combinations(sorted_list, i + 1)],sep="\n")