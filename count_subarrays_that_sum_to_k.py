from typing import List
from collections import defaultdict

# similar to 2sum, we need to store the complement we're after in a dictionary

def subarraySum(nums: List[int], k: int) -> int:
    """count the number of subarrays that sum to k. we don't want to slide windows of length 1 to len(n).
    instead, we are going to keep track of prefix/cumulative sums so that we can quickly check against k.
    note: if we saw prefix sum x and then k + x, we'd increment our counter. since sum(nums[i_x: i_k+x + 1]) = k
    actually, if we'd seen prefix sum x twice, and now we saw x + k, we'd be able to sum starting at the first 
    prefix sum occurrence or second prefix sum occurrence and stop where we are and have a value of k. so the incrementing is +2 in this case.
    so we just have to check the prefix_sum - k to see how many times this prefix_sum complement has happened.
    we can do this in constant time if the prefix sums are keys in a dictionary, 
    and we can increment correctly if we save the times that prefix sum has come up."""
    counter = 0 
    prefix_sum = 0
    prefix_sum_dict = defaultdict(int) # defaults to 0
    prefix_sum_dict[0] = 1  # we have an empty list which sums to 0   (k: 0 is the sum, v: count is currently 1)

    for num in nums:
        prefix_sum = prefix_sum + num

        if prefix_sum - k in prefix_sum_dict:
            counter += prefix_sum_dict[prefix_sum - k]

        prefix_sum_dict[prefix_sum] += 1

    return counter

if __name__ == "__main__":
    print(subarraySum([1,1,1], 2))
    print(subarraySum([1,2,3], 3))
