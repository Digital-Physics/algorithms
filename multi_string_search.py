# time: O(b**2 + ns) where n = # of small strings, s = len of longest small, b = len of big
# space: O(b**2)
# it would be quicker to build a trie for all of our small words and then go through our big string
# we would need to include stop characters "*" in that trie to indicate the ends of words
# time: O(ns + bs)
# space: O(ns)
def multiStringSearch(bigString, smallStrings):
    # create a trie of nested dictionaries
    trie_dict = trie_constructor(bigString)
    print("trie created")
    print()

    return [check_word(word, 0, trie_dict) for word in smallStrings]


def trie_constructor(bigString):
    trie_dict = {}
    for i in range(len(bigString)):
        print("get trie dict for all substrings starting at ith letter", i, "(including entire suffix)")
        trie_dict = trie_helper(bigString, trie_dict, trie_dict, i)
    return trie_dict


# to add to trie we need to let the recurssion go down levels to sub-tries
# but to return the entire trie at the end, we pass the root of the trie in each time
def trie_helper(bigString, trie, sub_trie_dict, i):
    print("process string through index", i)
    while i < len(bigString):
        if bigString[i] in sub_trie_dict:
            return trie_helper(bigString, trie, sub_trie_dict[bigString[i]], i + 1)
        else:
            sub_trie_dict[bigString[i]] = {}
            return trie_helper(bigString, trie, sub_trie_dict[bigString[i]], i + 1)
    return trie


def check_word(word, i, dictionary):
    print("string to check:", word)
    if i < len(word):
        print("string in dictiornary through", word[i])
        if word[i] in dictionary:
            return check_word(word, i + 1, dictionary[word[i]])
        else:
            print(word, "not in dict")
            return False

    print(word, "string in dict")
    return True


