def longestPalindromeSubseq(s: str) -> int:
    """returns length of longest palindromic subsequence (not substring)
    this is the same as the longest common subsequence algorithm, but with one string going in reverse.
    """
    t=s[::-1]  #idea is reverse t and compare t with s
    
    # we add an extra row and column for the base case of 0
    # rows = last letter added of characters of s (starting with empty)
    # cols = last letter added characters of s.reverse() (starting with empty)
    # entries = longest palindromic subsequence for s[:i] and s[::-1][:j] knowing that you'll match on the other end since you matched to start
    dp_matrix = [[0 for _ in range(len(s)+1)] for __ in range(len(s)+1)] 
    
    # we
    for i in range(1,len(s)+1):  
        for j in range(1,len(s)+1):
            if s[i-1] == t[j-1]:
                # (e.g. race_c vs race_c => 4 + 1) or (b_a vs bbb_a => 1 + 1)
                dp_matrix[i][j] = dp_matrix[i-1][j-1] + 1 
            else:                                    
                # they don't match, so no extension; just choose the better of (e.g. raceca_r vs rac_e => max((racecar, rac)=3, (raceca, race)=4)) = 4
                dp_matrix[i][j] = max(dp_matrix[i][j-1], dp_matrix[i-1][j])
    
    
    return dp_matrix[-1][-1] # bottom_right (raceca_r, raceca_r) or (baabb_b vs. bbbaa_b => 3 + 1) (previously, 3 = baabb vs bbbaaa has baa... we know it will end on a b)

print(longestPalindromeSubseq("bcab"))
print(longestPalindromeSubseq("raceca"))