from typing import List, Tuple
# 435
# List of tuples representing interval endpoints
# return min number of interval to remove so none overlap

# [1,           5]  (remove 1 line)
# [1, 2][2, 3]

# 1) start with intervals sorted by left
# 2) we will assume we have the left side sorted up to some point that we track 
# 3) Induction kind of step to fold the next one in (when comparing two, choose one whose right side ends first, since they are both get you up to check_point)  

def nonoverlapping_intervals(arr: List[Tuple[int]]) -> int:
    """return min num intervals to remove to ensure nonoverlapping intervals remain"""
    if not arr:
        return 0
    
    sorted_intervals = sorted(arr, key=lambda x: x[0])

    curr_end = sorted_intervals[0][1]
    counter = 0

    for start, end in sorted_intervals[1:]:
        if start >= curr_end:
            curr_end = end
        elif curr_end >= end: # remove interval with curr_end
            counter += 1
            curr_end = end
        elif curr_end < end: # remove contender interval
            counter += 1

# chatgpt's version (are they equivalent?)
def nonoverlapping_intervals(arr: List[Tuple[int, int]]) -> int:
    """Return the minimum number of intervals to remove to eliminate all overlaps."""
    if not arr:
        return 0

    # Sort by end time (greedy strategy)
    sorted_intervals = sorted(arr, key=lambda x: x[1])

    counter = 0
    curr_end = sorted_intervals[0][1]

    for start, end in sorted_intervals[1:]:
        if start < curr_end:
            # Overlap, must remove this interval
            counter += 1
        else:
            # No overlap, update current end
            curr_end = end

    return counter
            
            
        


