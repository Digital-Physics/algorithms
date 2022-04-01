# time complexity O(n)
# space complexity O(n)
import unittest


def twoNumberSum(array, targetSum):
    dictionary = {}
    # store the targetSum's complement
    for num in array:
        if num in dictionary.keys():
            return [num, targetSum - num]
        else:
            dictionary[targetSum - num] = targetSum - num
    return []


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
        print("must be ok if no error")

    def test_case_2(self):
        output = twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 19)
        self.assertTrue(len(output) == 2)
        self.assertTrue(8 in output)
        self.assertTrue(11 in output)
        print("must be ok if no error")


test = TestProgram()
test.test_case_1()
test.test_case_2()
