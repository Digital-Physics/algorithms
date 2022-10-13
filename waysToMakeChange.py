# time: O(d*n)
# space: O(n)
def numberOfWaysToMakeChange(n, denoms):
    number_of_ways = [0 for _ in range(n + 1)]
    number_of_ways[0] = 1  # number of ways to make no change

    print("note: you can't do the for loops the opposite way. you must add coins one at a time to use this formula.")
    for coin in denoms:
        for check_idx in range(1, n + 1):
            if coin <= check_idx:
                # keep the ways we've made each target amount without using the coin
                # and add the new way with using the coin
                number_of_ways[check_idx] += number_of_ways[check_idx - coin]

    return number_of_ways[n]