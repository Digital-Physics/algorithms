import bisect
# there is also a binarytree library, but it must be installed
# why is BST not a standard library?
# I guess we can just used ordered dictionaries? No, those are based on key insertion order, not the value order

l = [3, 4, 2, 1, 5]

sorted_list = sorted(l)

# O(log(n)) insert without setting up a Binary search on the sorted list
bisect.insort(sorted_list, 3)

print(sorted_list)

# remove items in O(log(n))? No linear O(n)
idx = bisect.bisect_left(sorted_list, 4)
# sorted_list.pop(idx) # linear time, in at least part of the list, I think
del sorted_list[idx] # is this any better?
print(sorted_list)

idx_l = bisect.bisect_left(sorted_list, 3)
idx_r = bisect.bisect_right(sorted_list, 3)
idx_for_insert = bisect.bisect_right(sorted_list, 4)
print("Note: value returned is index of location, IF it exists, else it is the place to be INSERTED", idx_l, idx_r, idx_for_insert)