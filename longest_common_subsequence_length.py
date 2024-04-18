from functools import cache, lru_cache

# @cache
# @lru_cache(maxsize=None)
def commonChild_v1(s1: str, s2: str, memo={}) -> int:
    """return length of longest common subsequence (using dynamic programming).
    Break-down DP; A more intuitive way where we start with the the final f(vars) we want (f(s1, s2)),
    find the relationship to adjacent inputs vars f(vars + delta) where delta = -1 in this case because we are breaking-down, 
    and break it down to the simple base cases... sort of like mathematical induction but in reverse... 
    Looking for provable (or in the case of DP, easy to compute or reason through) base cases and a relationship from 'n to n+1' to chain it together"""
    if (s1, s2) in memo:
        return memo[(s1, s2)]

    i = len(s1) - 1
    j = len(s2) - 1

    # base case
    if i == -1 or j == -1:
        return 0

    # adjacent relationship; from "n" to "n - 1" (abstractly)
    # there are three adjacent input variable cells in this imaginary matrix if we are reducing i/rows and j/cols by one. 
    #  f(x-1, y-1) f(x, y-1)
    #  f(x-1, y) 
    # 1) if the last char matches, then the relationship is as below. (they both increment by -1) i/rows increments by -1, j/cols increment by -1.
    if s1[i]==s2[j]:
        # print("if the letters match on their last letter, your answer was 1 more than the previous diagonal box")
        memo[(s1, s2)] = 1 + commonChild(s1[:i], s2[:j])
        return memo[(s1, s2)]
    else:
        # print("if they didn't match, your answer was the max of the two other adjacent cells, because neither of them could increment.")
        memo[(s1, s2)] = max(commonChild(s1[:i], s2), commonChild(s1, s2[:j]))
        return memo[(s1, s2)]

def commonChild(s1: str, s2: str) -> int:
    memo = {}
    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == -1 or j == -1:
            return 0
        if s1[i] == s2[j]:
            result = 1 + dp(i-1, j-1)
        else:
            result = max(dp(i-1, j), dp(i, j-1))
        memo[(i, j)] = result
        return result
    return dp(len(s1) -1, len(s2) -1)
    

# js also had issues

# function commonChild(s1, s2) {
#     let cache = {};
#     let result;
    
#     function dp(i, j) {
#         if (cache[i + ',' + j] !== undefined) {
#             return cache[i + ',' + j];
#         }
#         if (i === -1 || j === -1) {
#             return 0;
#         }
#         if (s1[i] === s2[j]) {
#             result = 1 + dp(i - 1, j - 1);
#         } else {
#             result = Math.max(dp(i - 1, j), dp(i, j - 1));
#         }
#         cache[i + ',' + j] = result;
#         return result;
#     }

#     return dp(s1.length - 1, s2.length - 1);
# }

# C++ worked
# Instead of defining 2d matrix inside a function, define it globally. In this way it will acquire data segment instead of stack memory.

# int dp[5001][5001]; // Define the matrix globally

# int commonChild(const std::string& s1, const std::string& s2) {
#     int m = s1.length();
#     int n = s2.length();
    
#     for (int i = 0; i <= m; i++) {
#         for (int j = 0; j <= n; j++) {
#             if (i == 0 || j == 0) {
#                 dp[i][j] = 0;
#             } else if (s1[i - 1] == s2[j - 1]) {
#                 dp[i][j] = 1 + dp[i - 1][j - 1];
#             } else {
#                 dp[i][j] = std::max(dp[i - 1][j], dp[i][j - 1]);
#             }
#         }
#     }
    
#     return dp[m][n];
# }


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = commonChild(s1, s2)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()