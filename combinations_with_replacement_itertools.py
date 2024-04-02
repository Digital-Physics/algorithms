from itertools import combinations_with_replacement

string, k = input().split(" ")
k = int(k)

sorted_list = sorted([*string])

print(*["".join(tup) for tup in combinations_with_replacement(sorted_list, k)],sep="\n")