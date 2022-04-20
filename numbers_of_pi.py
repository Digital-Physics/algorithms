# time: O(n**3+m)
# there are roughly n**2 substrings for our pi (n*(n+1)/2 actually) (e.g. 3141)
# 3, 31, 314, 3141
# 1, 14, 141
# 4, 41
# 1
# plus the slicing of the substring is another n in the same for loop
# space: O(n+m) values in our hash table associate w/ pi, m is for hash of numbers
#
def numbersInPi(pi, numbers):
    # store numbers for quick, constant time check instead of looking through list each time
    numbers_dict = {number: True for number in numbers}  # O(m) time
    min_spaces = get_min_spaces(pi, numbers_dict, {}, 0)

    return -1 if min_spaces == float("inf") else min_spaces


def get_min_spaces(pi, numbers_dict, answer_cache_dict, start_idx_in_pi):
    if start_idx_in_pi == len(pi):
        # we count a space after matching a string, but we don't need to count one at end
        # note: that if we gave a start_IDX of length-1, we'd go through once before hitting this base case
        return -1

    # store DP answer in cache so we don't need to recompute
    # this is the best over all possibilities because to get in dict, it ran through all possibilities in for loop...
    # starting from the start_idx and going through the rest of the pi string of different length...
    # this is one way to get all substrings (when starting at 0 and using all other idx as another starting point for a for loop)
    if start_idx_in_pi in answer_cache_dict:
        return answer_cache_dict[start_idx_in_pi]

    # below, we need to actually compute
    # initialize. will be overwritten if all strings and continuations are found. if not 1+inf or 2+inf = inf
    min_spaces_so_far = float("inf")

    # this could be done backwards starting from the end and looking over substrings
    # this does a lot of calls before it hits bottom, but we could do opposite
    for i in range(start_idx_in_pi, len(pi)):
        substring = pi[start_idx_in_pi:i + 1]  # sort of like a prefix if we ignore what came before start_idx
        if substring in numbers_dict:
            # how is this cache not stale when called? is it because it hits bottom and builds up without being stale?
            # or does the cache get updated before it gets called because all caches are pointing to same object?
            remaining_spaces = get_min_spaces(pi, numbers_dict, answer_cache_dict, i + 1)
            # overwritten when better/less partition/space/split is done over for loop; it doesn't just take first DFS split
            min_spaces_so_far = min(min_spaces_so_far, remaining_spaces + 1)

    # now that we've gone through all possible ending partitions and found the best, let's store it in our cache and then return it
    answer_cache_dict[start_idx_in_pi] = min_spaces_so_far
    return answer_cache_dict[start_idx_in_pi]
