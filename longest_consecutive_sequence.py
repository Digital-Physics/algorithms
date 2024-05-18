from typing import List
from collections import defaultdict

def longestConsecutive(nums: List[int]) -> int:
    """returns count of longest consecutive sequence of integers in O(n) time. 
    we can start at any node and clear the entire sequence it is part of in linear time.
    although we move backwards sometimes, we never see the same int twice 
    (because we pop() & remove() before the next round, and we jump back to where we started at n after moving backwards)"""
    longest = 0
    num_set = set(nums) # linear time; 1) allows to do constant time checks going forward and 2) eliminates analyzing duplicates

    while num_set:
        n = num_set.pop()

        if (n-1) not in num_set: # can we start counting just going forward?
            length = 1 # we have n as our first number in this consecutive sequence

            while (n + length) in num_set:
                num_set.remove(n + length)
                length += 1

            longest = max(longest, length)
        else: # or should we count backwards first, before going forward?
            reset_num = n # for reset after counting backwards which involves changing n

            while (n-1) in num_set:
                num_set.remove(n - 1)
                n -= 1
            
            prefix_count = reset_num - n

            length = 1

            while (reset_num + length) in num_set:
                num_set.remove(reset_num + length)
                length += 1
                
            longest = max(longest, prefix_count + length)
    
    return longest


# def longestConsecutive2(nums: List[int]) -> int:
#     num_set = set(nums)
#     table = {}

#     longest = 0

#     for num in num_set:
#         one_lower = table.get(num - 1, 0)
#         one_higher = table.get(num + 1, 0)

#         val = one_lower + one_higher + 1

#         table[num - one_lower] = val
#         table[num + one_higher] = val
#         longest = max(longest, val)

#     return longest

if __name__ == "__main__":
    print(longestConsecutive([100,4,200,1,3,2]))
    print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    # print(longestConsecutive2([100,4,200,1,3,2]))
    # print(longestConsecutive2([0,3,7,2,5,8,4,6,0,1]))