from typing import List
from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:
    """guards are gone for h hours. 
    
    Koko can eat k bananas/hour, but can't switch piles within an hour.

    Eg. piles = [3, 6, 7 , 11]
    guards gone 8 hours 

    11/hour => 4 hours
    3/hour takes sum[1, 2, 3, 4] => 10

    In this case, it's eating rate is between 3 and 11.
    
    what is the slowest eating rate such that Koko
    still completes in h hours or less?
    """
    rate_upper_bound = max(piles) # Koko can get through each pile in an hour and len(piles) <= h
    rate_lower_bound = 1 # need to finish the bananas

    while rate_upper_bound > rate_lower_bound:
        mid_rate = (rate_lower_bound + rate_upper_bound)//2

        if sum([ceil(val/mid_rate) for val in piles]) < h: # eating too quickly
            rate_upper_bound = mid_rate - 1
        elif sum([ceil(val/mid_rate) for val in piles]) > h: # eating too slowly
            rate_lower_bound = mid_rate + 1
        else:
            break

    mid_rate = (rate_lower_bound + rate_upper_bound)//2  # lower bound = upper bound or the last mid rate which broke is recalculated

    return mid_rate

if __name__ == "__main__":
    print(minEatingSpeed([3,6,7,11], 8))
    print(minEatingSpeed([30,11,23,4,20], 5))
    print(minEatingSpeed([30,11,23,4,20], 6))