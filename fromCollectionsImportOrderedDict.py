from collections import OrderedDict # ordered by the order in which keys first get put in to the dict

n = int(input())
od = OrderedDict()

for _ in range(n):
    # it would be nice to also use an Ordered DefaultDict, but that may be confusing things
    inp = input() 
    if inp not in od:
        od[inp] = 1
    else:
        od[inp] += 1

print(len(od))
print(" ".join([str(val) for val in od.values()]))




