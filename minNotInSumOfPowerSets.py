# O(nlogn) time for the sorting... nlogn + n in total
# O(1) space complexity since the sorting takes constant space since it is done in place and all we store is one number in the second step
def nonConstructibleChange(coins):
    # sort in place (if ok) to do it in constant space
    coins.sort()
    max_thus_far = 0
    for coin in coins:
        if coin > max_thus_far + 1:
            return max_thus_far + 1
        else:
            max_thus_far += coin

    return max_thus_far + 1