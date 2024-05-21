from typing import Set, List, Tuple, Optional

def string_to_valid_words(s: str, dictionary: Set[int]) -> List[str]:
    """there is a valid set of words in the string. return a valid string with spaces inserted.
    we'll use backtracking, the growing and shrinking odometer."""
    def is_valid(s, dictionary, start_idx) -> Tuple[bool, Optional[str], int]:
        """returns True/False, word, and next starting idx"""
        curr_idx = start_idx + 1

        while curr_idx < (len(s) + 1) and (s[start_idx: curr_idx] not in dictionary or s[start_idx: curr_idx] in words_tried[start_idx]):
            curr_idx += 1

        # did it hit end (and if so was it not a word) or did we just find the next word?
        if curr_idx == (len(s) + 1):
            if s[start_idx: curr_idx] in words_tried[start_idx]:
                print("backtrack (from, to):", start_idx, start_idx_stack[-2])
                output.pop()
                start_idx_stack.pop()
                curr_idx = start_idx_stack[-1] # backtrack (take a step back because we've exhausted the current/LSD in our odometer)
                return False, None, curr_idx
            
            words_tried[start_idx].add(s[start_idx: curr_idx])

            if s[start_idx: curr_idx] not in dictionary:
                curr_idx = start_idx  # spin the odometer
                return False, None, curr_idx
            else:
                return True, s[start_idx: curr_idx], curr_idx  # grow odometer
        else:
            words_tried[start_idx].add(s[start_idx: curr_idx])
            return True, s[start_idx: curr_idx], curr_idx
        
    output = []
    # for backtracking
    start_idx = 0
    start_idx_stack = [0]
    words_tried = [set() for _ in range(len(s))] # List[Set[str]]

    # we need to backtrack if we hit a dead end
    # the growing and shrinking "odometer" is the list of words we've matched so far
    # the Least Significant Digit of this growing and shrinking odometer is the last word in our list we are constructing
    while start_idx < len(s):
        word_found_bool, next_word, start_idx = is_valid(s, dictionary, start_idx)

        if word_found_bool:
            start_idx_stack.append(start_idx)
            output.append(next_word)
    
    return " ".join(output)
        

if __name__ == "__main__":
    print(string_to_valid_words("whoami", {"who", "am", "i", "bob", "wh"}))
