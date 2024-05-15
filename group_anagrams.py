from collections import defaultdict # Counter
from sortedcontainers import SortedDict
from typing import List

# time: O((n*max_word_length)*n I think.
# Clement did it another way...
# He sorted each word w/ sorted(on list of chars), and then sorted the joined words while bringing original and idx w/ it)
# space: O(n*max_word_length)
def groupAnagrams(words: List[str]) -> List[str]:
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


# 2

def groupAnagrams2(words: List[str]) -> List[str]:
    counter_to_word_list = defaultdict(list) # creates list() if no key; alternatively defaultdict(lambda: [])

    for word in words:
        # char_counter = Counter(word)
        char_counter = SortedDict()

        for char in word:
            if char in char_counter:
                char_counter[char] += 1
            else:
                char_counter[char] = 1

        # counter_to_word_list[char_counter].append(word)  # Counter isn't hashable. tuple(counter.items()) would be, but they won't be ordered
        counter_to_word_list[tuple(char_counter.items())].append(word)

    return list(counter_to_word_list.values())


if __name__ == "__main__":
    print(groupAnagrams(["tea", "eat", "tan", "nat", "bat", "ate"]))
    print(groupAnagrams2(["tea", "eat", "tan", "nat", "bat", "ate"]))
