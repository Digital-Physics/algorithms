# time: O(n)
# space: O(min(n,a)) where a is unique letters in string; that's dictioary size. could it be just O(a)?
# original approach was not linear time, but was a little more clean/intuitive in the else: part.
def longestSubstringWithoutDuplication(string):
    i = 0
    letter_dict = {}
    best = 0
    best_start_idx = None
    best_end_idx = None
    current_start_idx = 0
    counter = 0

    while i != len(string):
        if string[i] not in letter_dict:
            letter_dict[string[i]] = i
            counter += 1
            if counter > best:
                best = counter
                best_start_idx = current_start_idx
                best_end_idx = i
            i += 1
        else:
            if letter_dict[string[i]] < current_start_idx:
                letter_dict[string[i]] = i
                counter += 1
                if counter > best:
                    best = counter
                    best_start_idx = current_start_idx
                    best_end_idx = i
                i += 1
            else:
                counter = counter - (letter_dict[string[i]] - current_start_idx)
                current_start_idx = letter_dict[string[i]] + 1
                letter_dict[string[i]] = i
                i += 1

    return string[best_start_idx: best_end_idx + 1]