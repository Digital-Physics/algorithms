#O(n) time where n is len(array). one pass through array is the most time it will take and we assume array >= sequence
# O(1) space since you don't need to start a stack or queue that grows or anything

def isValidSubsequence(array, sequence):
    while len(sequence) > 0:
        print(array, sequence)
        if len(array) == 0:
            return False
        else:
            if array[0] == sequence[0]:
                sequence = sequence[1:]
            array = array[1:]

    return True

