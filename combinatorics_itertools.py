# math solution
_ = input()
list_of_letters = input().split(" ")
choose = int(input())

a_s = list_of_letters.count("a")
n = len(list_of_letters)

prob = 1 # init

for i in range(choose):
    prob *= (n - a_s - i)/(n - i)

print(1 - prob)

# itertool solution would use the following somehow

from itertools import combinations

n_C_k_generator = combinations(list_of_letters, choose)
print(n_C_k_generator)
print([val for val in n_C_k_generator])
print([(i, j) for i in range(n) for j in range(i+1, n)])


