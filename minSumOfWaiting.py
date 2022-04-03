# O(nlogn) time for the sort; +n for the second step goes away
# O(1) space because sort in place and then just a fixed running total
def minimumWaitingTime(queries):
    queries.sort()
    # don't need to wait for the
    running_total = 0
    length = len(queries)

    for idx, time in enumerate(queries[:-1]):
        running_total += time * (length - idx - 1)

    return running_total