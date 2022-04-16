test_dictionary = {}

# dictionaries with keys based on multiple inputs
test_dictionary[1,True,"a"] = 77

print(test_dictionary)

# can access dictionary value using a tuple or with just the elements of the tuple
print(test_dictionary[1,True,"a"])
print(test_dictionary[(1,True,"a")])

# but if one of the elements is a list you have a problem
test_dict2 = {}
#test_dict2[1,True,["a", "b", "c"]] = 99
#list_var = ["a", "b", "c"]
#test_dict2[*list_var] = 99
# #test_dict2[1, True, *list_var] = 99
#print(test_dict2)

test_dict3 = {}
list_var = ["a", "b", "c"]
print("unpack list normally:", *list_var)

test_dict3[1, True, "a", "b", "c"] = 88
print(test_dict3)

# this is the way you should unpack your list and combine it with other elements
test_dict4 = {}
keys = 1, True, *list_var
test_dict4[keys] = 55
print(test_dict4)