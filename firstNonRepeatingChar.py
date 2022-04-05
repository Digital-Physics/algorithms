# time: O(n); writing chars in dict n + looking through dict n
# space: O(1) since the dictionary is at most 26 chars
def firstNonRepeatingCharacter(string):
    dict_once = {}

    for char in string:
        # .get with extra param handles case of it not existing yet
        dict_once[char] = 1 + dict_once.get(char, 0)

    for i in range(len(string)):
        if dict_once[string[i]] == 1:
            return i

    return -1
