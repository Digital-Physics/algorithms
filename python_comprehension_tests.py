capacity = 10
items = [[1, 2], [4, 3], [5, 6], [6, 7]]

# if-else up front in list comprehension
first_row = [0 if (cap < items[0][1]) else items[0][0] for cap in range(capacity)]

print(first_row)

# note: standalone if is in the back of list comprehension
just_if = [0 for cap in range(capacity) if (cap < items[0][1])]

print(just_if)