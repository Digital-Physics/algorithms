from typing import List
from bisect import bisect_left

def lengthOfLIS(nums: List[int]) -> int:
        """length of longest increasing subsequencesuence. one-dimensional dynamic programming. 
        N -> N+1: take the max over valid history-continuations +1 to get the next step.
        but this is O(n**2) because we're looking back across the entire history at each step."""
        best_runs_ending_here = [1] * len(nums)

        # A DP, bottom-up approach for constructing the next item in the list of best runs through index i :
        # go through each prefix bests and see which was the best to add 1 to (Assuming it is higher than the previous bests through that number)
        for i in range(len(nums)):
            for prev in range(i):
                if nums[i] > nums[prev] and best_runs_ending_here[i] < best_runs_ending_here[prev] + 1:
                    best_runs_ending_here[i] = best_runs_ending_here[prev] + 1
        return max(best_runs_ending_here)


def lengthOfLIS2(nums: List[int]):
    """get the subsequencesuence of the LIS. We'll do this n*log(n) time by keeping the subsequences items sorted"""
    subsequences = [] # this will have the longest subsequences and other subsequencesuences being written right on top of it. 

    for i, x in enumerate(nums):
        # if it allows the subsequences to increase (who cares by how much? => future continuations harder)
        if len(subsequences) == 0 or subsequences[-1] < x:
            subsequences.append(x)
        else:
            # find smallest number greater than x in the current best run (composite) & replace it 
            # (we're essentially using the subsequences array to store several subsequences at once)
            # for example [2,4,7,3], would have subeq as [2, 4, 7] and then when 3 can't continue the longest run, [2, 3, 7] which has both [2,3] and [2, 4, 7] implicitly
            insertion_idx = bisect_left(subsequences, x)
            subsequences[insertion_idx] = x

    return len(subsequences)


def pathOfLIS(nums: List[int]):
    """get the subsequencesuence of the LIS. We'll do this n*log(n) time by keeping the subsequences items sorted"""
    subsequences = [] # this will have the longest subsequences and other subsequencesuences being written right on top of it. only the indices in the end will create the path.
    sub_idx = [] 
    trace = [-1] * len(nums)  # we'll stop at -1 in a while loop

    for i, x in enumerate(nums):
        # if it allows the subsequences to increase (who cares by how much? => future continuations harder)
        if len(subsequences) == 0 or subsequences[-1] < x:
            if sub_idx:
                trace[i] = sub_idx[-1]
            subsequences.append(x)
            sub_idx.append(i)
        else:
            # find smallest number greater than x in the current best run (composite) & replace it 
            # (we're essentially using the subsequences array to store several subsequences at once)
            # for example [2,4,7,3], would have subeq as [2, 4, 7] and then when 3 can't continue the longest run, [2, 3, 7] which has both [2,3] and [2, 4, 7] implicitly
            insertion_idx = bisect_left(subsequences, x)
            if insertion_idx > 0:
                trace[i] = sub_idx[insertion_idx - 1]
            
            # replace
            subsequences[insertion_idx] = x
            sub_idx[insertion_idx] = i

    # return len(subsequences)

    path = []
    subseq_path_idx = sub_idx[-1] # start with last index in list associated with the longest run
    print("length:", len(subsequences))

    while subseq_path_idx >= 0:
        path.append(nums[subseq_path_idx])
        subseq_path_idx = trace[subseq_path_idx]

    # reverse the end-to-beginning construction
    return path[::-1]

if __name__ == "__main__":
    print(lengthOfLIS([2, 6, 8, 3, 4, 5, 1]))  # 4
    print(lengthOfLIS2([2, 6, 8, 3, 4, 5, 1]))  # 4
    print(pathOfLIS([2, 6, 8, 3, 4, 5, 1]))  # [2, 3, 4, 5]