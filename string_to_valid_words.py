from typing import Set, List, Tuple, Optional

def string_to_valid_words(s: str, dictionary: Set[int]) -> List[str]:
    """there is a valid set of words in the string. return a valid string with spaces inserted."""
    def is_valid(s, dictionary, start_idx) -> Tuple[bool, Optional[str], int]:
        """returns True/False, word, and next starting idx"""
        curr_idx = start_idx + 1

        while curr_idx < (len(s) + 1) and s[start_idx: curr_idx] not in dictionary:
            curr_idx += 1

        if curr_idx == (len(s) + 1) and s[start_idx: curr_idx] not in dictionary:
            return False, None, curr_idx
        else:
            return True, s[start_idx: curr_idx], curr_idx
        
    output = []
    start_idx = 0

    while start_idx < len(s):
        word_found, next_word, start_idx = is_valid(s, dictionary, start_idx)

        if word_found:
            output.append(next_word)
        else:
            return word_found
    
    return " ".join(output)
        

if __name__ == "__main__":
    print(string_to_valid_words("whoami", {"who", "am", "i", "bob"}))
