# O(n) time where n is len(array). one pass through array is the most time it will take. assume array >= sequence
# O(1) space since you don't need to start a stack or queue that grows or anything

def is_valid_subsequence(array: list[int], sequence: list[int]) -> bool:
    """checks whether a list is a (non-consecutive) subsequence of another list.
    it does this by essentially dequeuing two lists and seeing which one runs out of elements first"""
    while len(sequence) > 0:
        print(sequence, array)
        if len(array) == 0:
            print("we've run out of choices to find our next number")
            return False
        else:
            if array[0] == sequence[0]:
                print("they match, so we can remove the first number and go to the next number we want to find")
                sequence = sequence[1:]
            print("we can shorten the string we are looking through whether they matched or not")
            array = array[1:]

    return True


test_array = [5, 1, 22, 25, 6, -1, 8, 10]
test_seq = [1, 6, -1, 10]

print(is_valid_subsequence(test_array, test_seq))
