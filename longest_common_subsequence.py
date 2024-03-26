# 'subsequence' can have deleted letters. "ace" is a subsequence of "abcde"
# subsequences are a generalization of a substring (which only consists of consecutive letters)

# thought about a trie, but it would still be O(n**2) just to construct it
# thought about a DP matrix with a cells containing counts and a dictionary that stored letters since last subsequence match that could still be matched on if you 
# increment one of the strings and look for that letter in the dictionary. . this may be similar to recursively going back in DP matrix for matches, but more complicated.

def longestCommonSubsequence(text1: str, text2: str) -> int:
    """Build-up DP. Increment index i and/or j through the strings, 
    making recursive calls, counting up and filling in dp matrix."""
    # init dynamic programming matrix that will get recursively populated
    dp_lcs_matrix = [[None]*len(text2) for _ in range(len(text1))]

    def lcs(i, j):
        # nonlocal keyword is like global, but is used to access nonlocal variables one scope up in a nested functions
        nonlocal dp_lcs_matrix 
        print(f"{i=}, {j=}, {abs(i-j)=}")
        print("DP matrix", dp_lcs_matrix)

        # base case, for when we've exhausted letters in either of the strings 
        print("what is this", len(text1), i, j)
        if i>=len(text1) or j>=len(text2): 
            print("one of the strings has no more characters, so return a 0 to the sum")
            return 0
        
        if dp_lcs_matrix[i][j] is not None: 
            print("We have a resulting number now")
            return dp_lcs_matrix[i][j]
        
        if text1[i]==text2[j]:
            print("Match. 1 + the value from a move diagonal in the dp matrix, down and to the right. (increment i and j)")
            dp_lcs_matrix[i][j]=1+lcs(i+1, j+1)
            return dp_lcs_matrix[i][j]
        else:
            print("no match, so we take the better of adjacent entries")
            dp_lcs_matrix[i][j]= max(lcs(i, j+1), lcs(i+1, j))
            return dp_lcs_matrix[i][j]
    
    return lcs(0, 0)


def longestCommonSubsequence_a(text1: str, text2: str) -> int:
    """Alice's solution is not correct"""
    print(text1, text2)

    i = len(text1) - 1
    j = len(text2) - 1

    # base case
    if i == -1 or j == -1:
        return 0

    # max of three adjacent cells (+1 if i j match)
    if text1[i]==text2[j]:
        return 1 + max(longestCommonSubsequence_a(text1[:i], text2[:j]), 
                       longestCommonSubsequence_a(text1[:i], text2),
                       longestCommonSubsequence_a(text1, text2[:j]))
    else:
        return max(longestCommonSubsequence_a(text1[:i], text2[:j]), 
                       longestCommonSubsequence_a(text1[:i], text2),
                       longestCommonSubsequence_a(text1, text2[:j]))


def longestCommonSubsequence_j(text1: str, text2: str) -> int:
    """DP, but with a more intuitive way"""
    i = len(text1) - 1
    j = len(text2) - 1

    # base case
    if i == -1 or j == -1:
        return 0

    # if the letters match at the end, your answer was 1 more than the previous diagonal's box
    if text1[i]==text2[j]:
        print("if the letters match on their last letter, your answer was 1 more than the previous diagonal box")
        return 1 + longestCommonSubsequence_a(text1[:i], text2[:j])
    else:
        print("if they didn't match, your answer was the max of the two other adjacent cells, because neither of them could increment.")
        return max(longestCommonSubsequence_a(text1[:i], text2), 
                   longestCommonSubsequence_a(text1, text2[:j]))

print(longestCommonSubsequence_j("abcde", "bqdaeeeeeeeeeeee"))
print("bde = 3")