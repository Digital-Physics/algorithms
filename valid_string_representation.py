def validWordAbbreviation(word: str, abbr: str) -> bool:
    """check to see if the abbreviation is valid. can replace substrings with len(substrings) int > 1 and no leading 0s in general.
    can't have consecutive numbers in abbreviation. e.g. 'digital' == 'd3t2' and is valid.
    notice 'd42' is ambiguous if you want it to stand for 4 and then 2 and 42 and therefore not allowed."""
    word_i = 0  # word can increment by 1 or int(string of numbers)
    abbr_i = 0  # will always increment by 1 (including when it is the only thing incrementing while reading in digits)
    
    # we while loop based on the word_i and check the abbr_i inside, although we could flip this
    while word_i < len(word):
        if abbr_i >= len(abbr): # not through the word yet, but we don't have more characters in the abbreviation representation
            return False
            
        if word[word_i] == abbr[abbr_i]:
            word_i += 1
            abbr_i += 1
            continue
        elif not abbr[abbr_i].isdigit(): # we already saw it didn't match on letters above, so if the abbr is a letter, it's not valid
            return False
            
        # the abbr index pointer is at the start of a number at this point, so handle it 
        start_index = abbr_i
        while abbr_i < len(abbr) and abbr[abbr_i].isdigit(): # range check and next significant digit check
            abbr_i += 1
        num_str = abbr[start_index:abbr_i]  # keep it a string so we can check for a leading 0
        
        if num_str[0] == '0':
            return False
        
        word_i += int(num_str) 
        
    # make sure we haven't overshot on the last word index number-jump
    # make sure we have used up all of our abbreviation characters (because we exit the while loop on the word index, not the abbreviation index)
    return word_i == len(word) and abbr_i == len(abbr)

if __name__ == "__main__":
    print(validWordAbbreviation("digital", "d3t2"))
    print(validWordAbbreviation("digital", "d3t3"))