# time: O((n*max_word_length)*n I think.
# Clement did it another way...
# He sorted each word w/ sorted(on list of chars), and then sorted the joined words while bringing original and idx w/ it)
# space: O(n*max_word_length)
def groupAnagrams(words):
    # anagrams have the same bucket counts
    # see if two dictionaries are the same

    # will be kept the same size
    word_list = []
    word_dict_list = []

    for word in words:
        word_dict = {}
        for char in word:
            if char in word_dict:
                word_dict[char] += 1
            else:
                word_dict[char] = 1

        if word_dict in word_dict_list:
            i = word_dict_list.index(word_dict)
            word_list[i].append(word)
        else:
            word_dict_list.append(word_dict)
            word_list.append([word])

    return word_list
