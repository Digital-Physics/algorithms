from sortedcontainers import SortedList, SortedDict, SortedSet
# better than bisect which doesn't have discard/remove in log time
# seems to be almost a replacement for when using sorted(), unless you are just using it once and aren't planning to add() or discard()

# 1) SortedList
print("", "SortedList", "", sep= "\n")

sorted_list = SortedList([1, 3, 32, 3, 6, 5, 4])

sorted_list.add(31)
print(sorted_list)

sorted_list.remove(6)
print(sorted_list)

sorted_list.remove(3) # discard() is a little safer to use
print(sorted_list)

# get the top 3 largest keys in a list 
top_three = sorted_list[-3:]
print(top_three)

# just like with sets, we have remove which can error and discard which will not
sorted_list.discard(99)
# sorted_list.remove(99)

# we have .update() instead of .extend()
sorted_list.update([88, 84, 87])
print(sorted_list)

# key for sorting
sorted_list_with_key = SortedList([(1, "c"), (1, "a"), (3, "b"), (2, "a"), (1, "a")], key=lambda x: (x[1], x[0])) # sort off second item, then the first
print(sorted_list_with_key)
print(sorted_list_with_key[:3])
sorted_list_with_key.add((4, "a"))
print(sorted_list_with_key)
print(sorted_list_with_key[:3])

# 2) SortedSet
print("", "SortedSet", "", sep="\n")

sorted_set = SortedSet([1, 3, 32, 3, 6, 5, 4])

sorted_set.add(31)
print(sorted_set)

sorted_set.discard(6)
print(sorted_set)

sorted_set.discard(3)
print(sorted_set)

top_three_unique = sorted_set[-3:]
print(top_three_unique)

sorted_set.update([88, 84, 87])
print(sorted_set)

# check for membership in set using the normal in operator
if 32 in sorted_set: 
    print('32 is present') 
else: 
    print('32 is not present') 

# .union() .intersection() included too
# sorted_set.union([101, 105, 105]) # does not mutate but returns a new set
sorted_set2 = SortedSet([101, 105, 105])
sorted_union = sorted_set.union(sorted_set2)
print(sorted_union)

sorted_union2 = sorted_set.union([101, 105, 105])
print(sorted_union2)

print(sorted_union2.intersection([87, 84]))

sorted_set_with_key = SortedSet([(1, "c"), (1, "a"), (3, "b"), (2, "a"), (1, "a")], key=lambda x: (x[1], x[0]))
print(sorted_set_with_key)
print(sorted_set_with_key[:3])

# 3) SortedDict (keys (not values) are maintained in sorted order)
print("", "SortedDict", "", sep="\n")

# notice that it takes in a dict (how else could it work without k: v pairs?), not a list like SortedList and SortedSet
sorted_dict = SortedDict({'b': 2, 'a': 1, 'c': 3, 'q': -3})
print(sorted_dict)

top_three_keys = list(sorted_dict.keys())[-3:]
values_of_top_three_keys = list(sorted_dict.values())[-3:] # these are still associated with the top keys
# top_three_values = list(SortedDict({'b': 2, 'a': 1, 'c': 3, 'q': -3}, key=lambda x: x[1]).items())[-3:] # get the value to sort by

print(top_three_keys)
print(sorted_dict.peekitem(-3), sorted_dict.peekitem(-2), sorted_dict.peekitem(-1))
print(sorted_dict.items()[-3], sorted_dict.items()[-2], sorted_dict.items()[-1])
print(values_of_top_three_keys)
# print(top_three_values)

sorted_dict['d'] = -4  # Add a new key-value pair
value = sorted_dict['c']  # Access the value for a key
print(sorted_dict.get("z", "no z found; default value returned"))
sorted_dict['a'] = 10  # Update the value for an existing key

del sorted_dict['b']  # Remove a key-value pair
sorted_dict.pop("a") # Remove a key-value pair
# sorted_dict.pop("q") # Remove a key-value pair that doesn't exists results in an error
# del sorted_dict["q"] # Remove a key-value pair that doesn't exists results in an error
# sorted_dict.reduce("q") # reduce() doesn't exits for dictionaries
if "q" in sorted_dict: sorted_dict.pop("q")

print([(k, v) for k, v in sorted_dict.items()])

# can use the key argument for sorting based on a function applied to the keys?
# cannot easily maintain sorting based on value
# sorted_dict2 = SortedDict({'b': 2, 'aa': 7, 'cccc': 3}, key=lambda x: len(x))
# print(sorted_dict2)
# print(list(sorted_dict2.keys()))
# print(list(sorted_dict2.values()))
# just use sorted()
print(sorted(sorted_dict.items(), key=lambda x: (x[1], x[0])))