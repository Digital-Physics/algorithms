from typing import Set, List, Tuple, Optional

def string_to_valid_words(s: str, dictionary: Set[int]) -> List[str]:
    """there is a valid set of words in the string. return a valid string with spaces inserted.
    we'll use backtracking (DFS), the growing and shrinking of an odometer that will eventually 
    grow to our solution length and be the solution."""

    def get_next_word(s, dictionary, start_idx) -> Tuple[bool, Optional[str], int]:
        """returns True/False depending on whether it finds the next word to append, the next word to append (or the rest of the string), and the end idx."""
        end_idx = start_idx + 1 # +1 because it is used as the end idx [start_idx: end_idx]

        # find next legal word's ending index (or end on the last idx)
        while end_idx < (len(s) + 1) and (s[start_idx: end_idx] not in dictionary or s[start_idx: end_idx] in words_tried[start_idx]):
            end_idx += 1
        
        if s[start_idx: end_idx] not in dictionary:
            return False, s[start_idx: end_idx], end_idx
        else:
            return True, s[start_idx: end_idx], end_idx  # grow odometer
        
    # for backtracking
    # the growing and shrinking "odometer" is the list of words we've matched so far
    # the Least Significant Digit of this growing and shrinking odometer is the last word in our list we are constructing in odometer
    odometer = []
    start_idx = 0
    start_idx_stack = [0]
    words_tried = [set() for _ in range(len(s))] # List[Set[str]]

    while start_idx < len(s):
        word_found_bool, next_word, start_idx = get_next_word(s, dictionary, start_idx)

        if word_found_bool:
            words_tried[start_idx_stack[-1]].add(next_word)
            start_idx_stack.append(start_idx)
            odometer.append(next_word)
        else:
            # backtrack
            odometer.pop()
            start_idx_stack.pop()
            start_idx = start_idx_stack[-1]

        print("curr output odometer:", odometer)
    return " ".join(odometer)   

if __name__ == "__main__":
    print(string_to_valid_words("whoami", {"who", "am", "i", "bob", "wh", "oa"}))
