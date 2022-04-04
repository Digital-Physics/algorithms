# time: O(c+d)
# space: O(c)
def generateDocument(characters, document):
    dict_of_count = {}

    for i in range(len(characters)):
        if characters[i] not in dict_of_count:
            dict_of_count[characters[i]] = 1
        else:
            dict_of_count[characters[i]] += 1

    for i in range(len(document)):
        if document[i] not in dict_of_count:
            return False
        else:
            dict_of_count[document[i]] -= 1
            if dict_of_count[document[i]] < 0:
                return False

    return True