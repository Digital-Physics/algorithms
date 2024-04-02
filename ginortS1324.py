list_of_chars = [*input()]

lower_strings = []
upper_strings = []
odd_nums = []
even_nums = []

for char in list_of_chars:
    if char.islower():
        lower_strings.append(char)
    elif char.isupper():
        upper_strings.append(char)
    elif char.isnumeric():
        if int(char) % 2 == 0:
            even_nums.append(char)
        else:
            odd_nums.append(char)

sorted_lists = [sorted(lower_strings), sorted(upper_strings),
                sorted(odd_nums), sorted(even_nums)]

extended_list = []

for l in sorted_lists:
    extended_list.extend(l)

print(extended_list)

print("".join(extended_list))
