# from collections import defaultdict

# s = input()
# str_len = len(s)

# third_place_score = float("-inf")
# third_place_letter = None
# counter_dict = defaultdict(int)
# top_three = set()

# for i in range(len(s)):
#     counter_dict[s[i]] += 1

#     if counter_dict[s[i]] == third_place_score:
#         if s[i] < third_place_letter:
#             top_three.add(s[i])
#             top_three.remove(third_place_letter)

#             third_place_score = counter_dict[s[i]]
#             third_place_letter = s[i]
#     elif counter_dict[s[i]] > third_place_score:
#         top_three.add(s[i])
#         top_three.remove(third_place_letter)

#         third_place_score = counter_dict[s[i]]
#         third_place_letter = s[i]

# top_three.sort(key=counter_dict.get)
# ...

############### 2nd approach

# from collections import Counter # for any iterable
# s = input()

# # problematic; this may preserve iterable order, like when sorting sets, not sort off of second criteria.
# letter_counter = Counter(s)

# for k, v in letter_counter.most_common(3):
#     print(k, v, sep=" ")


############### 3rd approach
from collections import defaultdict
s = input()

# the dictionary is not efficiently created; quadratic
# counter = {letter : s.count(letter) for letter in s}
counter = defaultdict(int)

for letter in s:
    counter[letter] += 1

# 
# sorted_list = sorted(counter.items(), key=lambda k, v: (-v, k))
sorted_list = sorted(counter.items(), key=lambda x: (-x[1], x[0]))

for k, v in sorted_list[:3]:
    print(k, v, sep=" ")