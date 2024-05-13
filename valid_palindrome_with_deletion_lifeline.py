def validPalindrome(s: str) -> bool:
    """when you find a mismatch, we'll want to a return two recursive calls with an OR operator 
    (because there are two different remaining strings that could make a valid palindrome)"""
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            # we are working with pointers/indices for indexing into the string, but remember with a slice we'll have to add one back in to the end so we don't lose the last element
            delete_left = s[left + 1: right + 1]
            delete_right = s[left:right]
            
            return isNormalPalindrome(delete_left) or isNormalPalindrome(delete_right)
        left += 1
        right -= 1
    return True

def isNormalPalindrome(s: str) -> bool:
    """just reverse the string and see if it is the same. no left and right pointers needed!"""
    return s == s[::-1]