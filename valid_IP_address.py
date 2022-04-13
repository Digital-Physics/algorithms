# time: O(1)
# space: O(1)
# Tim just chose to insert the periods and then checked to see if it was valid
# They implicitly make a DFS ternary tree with trying periods over 3 spaces
# and backtracking up the tree if it doesn't work out
# Tim's time was O(1) since the solution doesn't depend on size of input (plus it's limited to 12)
# There is a constant 1000**4 decimal strings that could be made, or (2**8)**4 bits that can fit into a IP size
def validIPAddresses(string):
    # check strings up to length 3, since 1000>256
    obj = NextDotHelper()
    obj.helper(string, "", 4)
    return obj.output


class NextDotHelper():
    def __init__(self):
        self.output = []

    def helper(self, string_left, partial_IP, dots_left):
        print()
        print("string left", string_left)
        print("partial_IP", partial_IP)
        print("dots left", dots_left)

        if dots_left == 0:
            if len(string_left) == 0:
                IP_address = partial_IP[:-1]  # remove dot
                self.output.append(IP_address)
                print("***************added", IP_address)
            else:
                print("don't do anything")
        else:
            for i in range(1, min(4, len(string_left) + 1)):
                if string_left[:i] is not None:
                    if int(string_left[:i]) < 256 and not (int(string_left[0]) == 0 and len(string_left[:i]) > 1):
                        new_partial_IP = partial_IP + string_left[:i] + "."
                        print("recursive call w/", string_left[i:], new_partial_IP, dots_left - 1)
                        self.helper(string_left[i:], new_partial_IP, dots_left - 1)

