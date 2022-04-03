# Time: O(n + p) where n is numbers and p is sets of parentheis
# Space O(d)... recursive calls, space on the call stack
def productSum(array):
    def sumHelper(specialList, level=1, fact_coef=1):
        if len(specialList) == 0:
            return 0
        elif isinstance(specialList[0], int):
            if len(specialList) == 1:
                return specialList[0] * fact_coef
            else:
                return specialList[0] * fact_coef + sumHelper(specialList[1:], level, fact_coef)
        else:
            return sumHelper(specialList[0], level + 1, fact_coef * (level + 1)) + sumHelper(specialList[1:], level, fact_coef)

    return sumHelper(array)

# next time: we should do a multiplier parameter which is only distributed after the sum of the sublist is returned
# O(n) time where n is elements AND subelements
# O(d) space where d is number of nesting that get put on the stack
def productSum2(array, coef=1):
    running_total = 0 # reset for each nested list
    for el in array:
        if isinstance(el, int):
            running_total += el
        else:
            running_total += productSum2(el, coef+1)
    return running_total*coef