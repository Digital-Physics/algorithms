# question: number of ways to climb n stairs given you can take steps of size 1 or 2

class ClimbStairs:
    def __init__(self, n: int) -> None:
        self.n = n

    def solve(self) -> int:
        # number of ways to get to n: ?, 1, 2... 
        # but 2 is going to be # of ways from 1 + num ways from 0, so base case for 0 should be = 1 
        # i, val: (0,1), (1,1)
        if self.n == 0 or self.n == 1:
            return 1
        
        ways_to_two_back = 1
        ways_to_one_back = 1
        ways = 0

        for _ in range(2, self.n+1):
            ways = ways_to_two_back + ways_to_one_back
            # reset now
            ways_to_two_back, ways_to_one_back = ways_to_one_back, ways 

        return ways

print(ClimbStairs(10).solve())

