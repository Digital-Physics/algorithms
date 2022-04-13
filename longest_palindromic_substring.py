# time: O(n**2) since for each index you check, you might have to spread out in both directions n/2 times
# space: O(n) since you output a string of up to length n, could be O(1) if you chunked it out, i think
# did not follow "don't repeat yourself" code, but it is straight forward
def longestPalindromicSubstring(string):
    # go through and from each i spread out until i-n and i+1 are different
    # this works for odd palindromes
    # for even check, check if it was equal to i-1, and then start the spread
    best_count = 0

    print("string", string)
    print("looking for odd length palindromes")
    for i in range(len(string)):
        print("look around", string[i])
        l_idx = i
        r_idx = i
        count = -1

        while l_idx >= 0 and r_idx < len(string):
            print("inspect substring", string[l_idx:r_idx + 1])
            if string[l_idx] == string[r_idx]:
                count += 2
                if count > best_count:
                    print("best so far")
                    best_count = count
                    start_idx = l_idx
                    end_idx = r_idx
                l_idx -= 1
                r_idx += 1
            else:
                break

    print("looking for even length palindromes", string)
    for i in range(1, len(string)):
        print("look around", string[i])
        if string[i - 1] == string[i]:
            l_idx = i - 1
            r_idx = i
            count = 0

            while l_idx >= 0 and r_idx < len(string):
                print("inspect substring", string[l_idx:r_idx + 1])
                if string[l_idx] == string[r_idx]:
                    count += 2
                    if count > best_count:
                        print("best so far")
                        best_count = count
                        start_idx = l_idx
                        end_idx = r_idx
                    l_idx -= 1
                    r_idx += 1
                else:
                    break

    return string[start_idx: end_idx + 1]


