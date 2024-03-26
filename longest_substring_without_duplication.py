# time: O(n) (we traverse the list just once, with our index never moving backwards)
# space: O(min(n,a)) where a is unique letters in string; that's dictionary size. could it be just O(a)? I think so.
def longestSubstringWithoutDuplication(string: str) -> str:
    i = 0 # index of string which we will traverse once in linear time
    letter_dict = {} # key: letter, value: most recent position index (to track if it appeared in the current no-repeat-substring contender run)

    # reigning no-repeat-substring champ. these will be written to when they are beaten.
    best = 0
    best_start_idx = None
    best_end_idx = None

    # current run contender (sometimes it keeps adding to its record, writing to the three best vars each step)
    current_start_idx = 0 
    counter = 0 

    while i != len(string): # equivalent to "while < len(string):" in this situation since we increment by 1 each step
        # three possibilities
        if string[i] not in letter_dict: #1
            letter_dict[string[i]] = i 
            counter += 1
            if counter > best:
                best = counter
                best_start_idx = current_start_idx
                best_end_idx = i
            i += 1
        else: #2
            if letter_dict[string[i]] < current_start_idx: # if the letter appeared before the start of the current contender run, just treat it like a non-repeat 
                letter_dict[string[i]] = i
                counter += 1
                if counter > best:
                    best = counter
                    best_start_idx = current_start_idx
                    best_end_idx = i
                i += 1
            else: #3
                # counter reset, but not all the way. we know the prefix string partitioned by the duplicate character has already been registered with best, so we take the truncated suffix as our new starting string run.
                counter = counter - (letter_dict[string[i]] - current_start_idx) 
                current_start_idx = letter_dict[string[i]] + 1 # so keep the current letter, and make sure you start the string after it's last instance
                letter_dict[string[i]] = i 
                i += 1

    return string[best_start_idx: best_end_idx + 1]


def longestSubstringWithoutDuplication2(string: str) -> str:
    i = 0 # index of string which we will traverse once in linear time
    letter_dict = {} # key: letter, value: most recent position index (to track if it appeared in the current no-repeat-substring contender run)

    # current run contender (sometimes it keeps adding to its record, writing to the three best vars each step)
    current_start_idx = 0 
    counter = 0 

    # reigning no-repeat-substring champ. these will be written to when they are beaten.
    best = 0
    best_start_idx = None
    best_end_idx = None

    while i != len(string): # equivalent to "while < len(string):" in this situation since we increment by 1 each step
        letter_dict[string[i]] = i # most recent index for the given letter

        # two possibilities
        if letter_dict[string[i]] < current_start_idx: # if the letter appeared before the start of the current contender run, just treat it like a non-repeat 
            counter += 1

            # no counter contender reset, so check for best
            if counter > best:
                best = counter
                best_start_idx = current_start_idx
                best_end_idx = i # only set on max
        else:
            # counter reset, but not all the way. we know the prefix string partitioned by the duplicate character has already been registered with best, so we take the truncated suffix as our new starting string run.
            counter = counter - (letter_dict[string[i]] - current_start_idx) 

            # no best check because we reset, but we need to move up the start index
            current_start_idx = letter_dict[string[i]] + 1 # so keep the current letter, and make sure you start the string after it's last instance

        i += 1

    return string[best_start_idx: best_end_idx + 1]