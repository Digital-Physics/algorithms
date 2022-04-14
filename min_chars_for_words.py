# time: O(n*max_word_length)
# space: O(c) where c (c<n*max_word_length) is the number of characters with them potentially all being needed and unique
def minimumCharactersForWords(words):
    # go through words and store chars in dictionary

    list_of_dicts = []
    total_chars_dict = {}
    output_array = []

    for word in words:
        letters_used_dict = {}
        for char in word:
            if char not in total_chars_dict:
                total_chars_dict[char] = 1  # will also use this as a best initialization

            if char not in letters_used_dict:
                letters_used_dict[char] = 1
            else:
                letters_used_dict[char] += 1

        list_of_dicts.append(letters_used_dict)

    for key in total_chars_dict.keys():
        for d in list_of_dicts:
            if d.get(key, 0) > total_chars_dict[key]:
                total_chars_dict[key] = d.get(key, 0)

        for _ in range(total_chars_dict[key]):
            output_array.append(key)

    return output_array
