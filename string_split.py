
n, m = input().split(" ")

array = list(input().split(" "))

pos_set = set(input().split(" "))
neg_set = set(input().split(" "))

happiness = 0

for val in array:
    if val in pos_set:
        happiness += 1
    if val in neg_set:
        happiness -= 1

print(happiness)