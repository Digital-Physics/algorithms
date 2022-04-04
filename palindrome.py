# time: O(n) because we have n/2 steps
# space: O(1) because not recursive, and only saving index variables
def isPalindrome(string):
    l_idx = 0
    r_idx = len(string) - 1

    while l_idx < r_idx:
        if string[l_idx] != string[r_idx]:
            return False
        else:
            l_idx += 1
            r_idx -= 1

    return True

