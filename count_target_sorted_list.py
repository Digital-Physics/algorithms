from typing import List
from bisect import bisect_left, bisect_right

def count_target(l: List[int], target: int) -> int:
    """count: lists are sorted"""

    # find if it exists in log time
    target_exists = False
    insertion_idx = bisect_left(l, target)
    target_exists = insertion_idx < len(l) and l[insertion_idx] == target # first checks that it isn't the next idx beyond the length

    if target_exists:
        l_idx = bisect_left(l, target)
        r_idx = bisect_right(l, target)

        return r_idx - l_idx
    else:
        return 0

if __name__ == "__main__":
    print(count_target([1,2,3,3,4], 3))
    print(count_target([1,2], 3))
    print(count_target([1,2,3,4], 3))