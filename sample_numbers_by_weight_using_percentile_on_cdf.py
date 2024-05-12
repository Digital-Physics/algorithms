from typing import List
import random

def sample_random_by_weight(w: List[int]) -> int:
    """This function samples items from a list based on weights provided"""

    total_weights = sum(w)
    # getting the pdf will involve float which might make the binary search to determine the index more difficult, so we won't use it
    # w = [val/total_weights for val in w]

    # like a cdf, but not going to 1 
    prefix_cumulative_sums = [0] * len(w)
    prefix_cumulative_sums[0] = w[0]

    for i in range(1, len(w)):
        prefix_cumulative_sums[i] = w[i] + prefix_cumulative_sums[i-1]

    # then get a uniformly sampled percentile using random.random() 
    # we'll get a float, but that's what we want. an int will make us think we are matching on an index when we want to end up between somewhere
    random_number = (random.random() * total_weights)

    # binary search on a sorted list in log time instead of searching through ~cdf in linear time
    # even if we did linear search to figure out which index to return, it wouldn't be the bottle neck. we'd still have same time complexity, and it would be a little more straight forward
    high_idx = len(w) - 1
    low_idx = 0

    # do binary search to see where the random number falls in the ~cdf
    # the value may not exist, so it's sort of like where it would get inserted
    # once the interval consists of indices that are just one apart, we're done finding where to insert it
    while high_idx > low_idx:
        mid_idx = (high_idx + low_idx)//2

        if random_number < prefix_cumulative_sums[mid_idx]:
            high_idx = mid_idx
        elif random_number > prefix_cumulative_sums[mid_idx]:
            low_idx = mid_idx + 1
        else:  # == 
            print("this should happen with probability 0")
            return mid_idx

    # return low_idx if random_number != high_idx else high_idx   # this should happen with probability 0. the chance a float happened to be an exact index
    return low_idx
    

if __name__ == "__main__":
    print(sample_random_by_weight([1, 2, 3]))
    # [1, 3, 6]
    # index 0 gets 0 to 1/6
    # index 1 gets 1/6 to 1/2
    # index 2 gets 1/2 to 1
    # 0.55 => 3.3 => 3.0 => ind

    dist = [0, 0, 0]
    for _ in range(1000):
        random_idx = sample_random_by_weight([1, 2, 3])
        dist[random_idx] += 1
    
    print(dist)