if __name__ == '__main__':
    string = input()
    answers = [False]*5

    # this has a linear time complexity O(n) since we do a constant 5 operations per character in string length n
    # if we were to use any(list of bool), we could also do it in O(n) by going through the entire list 5 times
    for character in string:
        if character.isalnum():
            answers[0] = True
        if character.isalpha():
            answers[1] = True
        if character.isdigit():
            answers[2] = True
        if character.islower():
            answers[3] = True
        if character.isupper():
            answers[4] = True
    
    print(*answers, sep="\n")
