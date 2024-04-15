# time: O(n) since we have to go through each character in string
# space: O(n) since we are storing and/or concatenating the stored words
# could have made this differently by " ".join() instead of "".join()
def reverseWordsInString(string):
    list_of_words = []
    start_idx = 0
    more_than_one_word = False

    for i in range(len(string)):
        if string[i] == " ":
            more_than_one_word = True
            print("hit a space")
            if not list_of_words:
                print("first word won't have a space at the end")
                list_of_words = [string[start_idx:i]] + list_of_words
            else:
                list_of_words = [string[start_idx:i + 1]] + list_of_words
            start_idx = i + 1

    # last word didn't hit a space so write it
    print("last word never hit a space so add it (if it isn't the only word)")
    if more_than_one_word:
        list_of_words = [string[start_idx:len(string)]] + [" "] + list_of_words
    else:
        list_of_words = [string[start_idx:len(string)]]

    print(list_of_words)
    return "".join(list_of_words)

