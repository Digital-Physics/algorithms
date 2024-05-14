from typing import List

def canJump(nums: List[int]) -> bool:
    """can you get to the last element starting from the first.
    you are allowed to jump a max of nums[i] indices at i
    e.g.
    [2, 3, 1, 1, 4] => jump sizes: sum(2, 1, 1) = (len(nums) - 1) - 0 => True
    [3, 2, 1, 0, 4] => False

    Note: only thing that prevents is a 0 (not every 0 will result in False),
    but it won't be the case that you jump past the end point because you can always jump less than the max.

    we can work with small lists of length 1, which is always True and length 2,
    which will be True if the first number >= (2-1) (i.e. not 0). so maybe dynamic programming.

    Can we find a relationship between list[:n] and list[:n+1]? 
    If True through n:
        True through n+1 if nums[n] > 0 or nums[n-1] > 1 or nums[n-2] > 2 ... else False (so let's work backwards)
    If False through n:
        False through n+1  # if you can't get to the end, you won't be able to hop by it by adding more numbers
    """
    currently_possible = True # it doesn't matter what the last number in the list is; we'll also start at the second to last
    counter = 0

    for i in range(len(nums) - 2, -1, -1): # reversed(range(len(nums) - 1))
        if currently_possible and nums[i] > 0:
            pass  # currently_possible = True
        elif currently_possible and nums[i] == 0:
            currently_possible = False
            counter += 1
        elif not currently_possible and nums[i] > counter:
            currently_possible = True
            counter = 0
        elif not currently_possible and nums[i] <= counter:
            counter += 1
    
    return currently_possible


if __name__ == "__main__":
    print(canJump([2, 3, 1, 1, 4]))
    print(canJump([3, 2, 1, 0, 4]))

        

