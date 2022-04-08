# time: O(nm) where n and m are string lengths
# space: O(nm)
# could do in less space if we just saved the 3 surrounding boxes that matter, not the whole matrix
def levenshteinDistance(str1, str2):
    # Naive: generate all strings that are one operation away and check
    # insert every letter in alphabet before every letter in string and at end
    # delete every letter of current string in set  (quick)
    # insert every letter in alphabet for every letter in string
    # better: dynamic programming: generate substring distances up from the bottom
    # two-dim array (matrix) where each dimension is enumeration of first n chars or each string
    # build out from 0,0 = "",""
    # the letters for each row and col also act as a way to see if the ending letters are same
    # m = matrix of counts from input string up to i to output string up to j (~symmetric matrix)
    # base row is 0, 1, 2, 3...
    m = [[j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
    # base col is also 0, 1, 2, 3... so overwrite; middle of matrix will be overwritten
    for i in range(1, len(str1) + 1):
        m[i][0] = i

    for i in range(1, len(str1) + 1):
        print(m)
        for j in range(1, len(str2) + 1):
            # we started with empty string in table so corresponding string index shifts
            if str1[i - 1] == str2[j - 1]:
                # if the last letter is the same, edits to get from for e.g. abc->yc same as ab->y
                m[i][j] = m[i - 1][j - 1]
            else:
                # looking back...
                # could remove one off the output string (from that pov of the symmetric matrix) and then add on next letter you need (+1)
                # or you could see that the last letters are different and substitute the last letter (after stepping back) (+1)
                m[i][j] = min(m[i - 1][j], m[i][j - 1], m[i - 1][j - 1]) + 1

    return m[len(str1)][len(str2)]