from collections import Counter

fam_size = int(input())
list_of_room_nums = [int(val) for val in input().split()]
counter_dict = Counter(list_of_room_nums)
unique_rooms = set(list_of_room_nums)

# find the value with single count
for val in unique_rooms:
    if counter_dict[val] == 1:
        print(val)

