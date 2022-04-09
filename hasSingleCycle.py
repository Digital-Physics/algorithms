# time: O(n) need to complete the hack/cycle
# space: O(n) for the recursive calls or the True/False array we save
def hasSingleCycle(array):
    return recursiveHelper(array, 0, 0, [False for _ in range(len(array))])


def recursiveHelper(array, idx, true_count, seen_already):
    if true_count == len(array) and idx == 0:
        return True
    elif seen_already[idx]:
        return False
    else:
        seen_already[idx] = True  # flag it
        true_count += 1
        next_idx = (idx + array[idx]) % (len(array))

        return recursiveHelper(array, next_idx, true_count, seen_already)

# this was a check of AlgoExpert's solution; it does work
def hasSingleCycle2(array):
        numElementsVisited = 0
        currentIdx = 0
        while numElementsVisited < len(array):
            if numElementsVisited > 0 and currentIdx == 0:
                return False
            numElementsVisited += 1
            currentIdx = getNextIdx(currentIdx, array)
        return currentIdx == 0

def getNextIdx(currentIdx, array):
        jump = array[currentIdx]
        nextIdx = (currentIdx + jump) % len(array)
        return nextIdx if nextIdx >= 0 else nextIdx + len(array)


test_case = [2,0,-2,0]

print(hasSingleCycle(test_case))
print(hasSingleCycle2(test_case))

