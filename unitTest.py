import unittest
import twoNumberSum
import isValidSubsequence

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        output = twoNumberSum.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
        self.assertTrue(len(output) == 2)
        self.assertTrue(11 in output)
        self.assertTrue(-1 in output)
        # print("yes, the test case ran. it must be ok if no error popped up.")

    def test_case_2(self):
        output = twoNumberSum.twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 19)
        self.assertTrue(len(output) == 2)
        self.assertTrue(8 in output)
        self.assertTrue(11 in output)
        # print("yes, the test case ran. it must be ok if no error popped up.")

    def test_case_3(self):
        array = [5, 1, 22, 25, 6, -1, 8, 10]
        sequence = [1, 6, -1, 10]
        self.assertTrue(isValidSubsequence.isValidSubsequence(array, sequence))

test = TestProgram()
test.test_case_1()
test.test_case_2()
test.test_case_3()