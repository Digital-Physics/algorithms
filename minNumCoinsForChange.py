# time: O(d*n)
# space: O(n)
def minNumberOfCoinsForChange(n, denoms):
    min_coins = [-1 for _ in range(n + 1)]  # return -1 if you can't make change
    min_coins[0] = 0  # don't need any coins to make 0
    
    for coin in denoms:
        print()
        print(coin, "coin is now at our disposal")
        print("min coins needed to make various amounts of money using combos of previous coins:")
        print(min_coins)
        for check_idx in range(1, n + 1):
            if coin <= check_idx:
                if min_coins[check_idx - coin] >= 0:
                    # you don't need to use the latest coin
                    # if you force using it by referencing the current row only, it could be worse than the last way you did it
                    # consider coins 1,3,4 and trying to make 6 after finding min coins using 1,3 was 2
                    if min_coins[check_idx] > -1:
                        min_coins[check_idx] = min(min_coins[check_idx - coin] + 1, min_coins[check_idx])
                    else:
                        min_coins[check_idx] = min_coins[check_idx - coin] + 1

    return min_coins[n]