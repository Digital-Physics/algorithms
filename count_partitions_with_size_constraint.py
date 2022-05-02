# note: this was not an algo_expert problem, as far as we know
# of partitions of n, with partition limit of size m
# a nice recursive visualizer: https://www.recursionvisualizer.com/
def count_partitions_with_limit_constraint2(n, m):
    if n == 0:
        return 1
    elif m == 0 or n < 0:
        return 0
    else:
        return count_partitions_with_limit_constraint(n-m,m) + count_partitions_with_limit_constraint(n,m-1)


def count_partitions_with_limit_constraint(n, m):
    if n == 1 or m == 1:
        return 1
    elif n <= m:
        return count_partitions_with_limit_constraint(n,n-1) + 1
    else:
        return count_partitions_with_limit_constraint(n-m,m) + count_partitions_with_limit_constraint(n,m-1)


print(count_partitions_with_limit_constraint(10,4))
print(count_partitions_with_limit_constraint2(10,4))