from collections import Counter

def isValid(s: str) -> str:
    counter_dict = Counter(s)
    remove_available = True

    # once we identify, than anything count + 1 or 1 can be removed to make valid
    print([count for count in counter_dict.values()])
    # top most_common(1)
    # first one most_common(1)[0] in list of length n (if you picked something greater than top 1)
    # the key value, most_common(1)[0][0] which was in this case a count
    most_common_count = Counter([count for count in counter_dict.values()]).most_common(1)[0][0]

    for letter in counter_dict.keys():
        if counter_dict[letter] == most_common_count:
            print("count matched", most_common_count)
            next
        elif counter_dict[letter] in [1, most_common_count + 1] and remove_available:
            print("used life line for", counter_dict[letter])
            remove_available = False
            next
        else:
            return "NO"
    
    return "YES"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()