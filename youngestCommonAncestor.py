# almost sounds like LUCA, last universal common ancestor
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


# time: O(h)? since we are at most going up 2 branches
# space: O(h)? because we have a recusive call stack and a dictionary
def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # once you find a value, write what's on the dfs stack, which is your path
    # when you find second value, compare what's on the stack to the first one you saved
    # wait, this problem doesn't have left and right child nodes, but youngest_ancestor/parent? attributes
    # alternative: take turns going back up the tree saving seen nodes in dictionary/hash
    ancestors_seen = {}
    return checker(descendantOne, descendantTwo, ancestors_seen)


def checker(node1, node2, seen_dictionary):
    if node1 is not None:
        print("check:", node1.name)
        if node1.name in seen_dictionary:
            return node1
        else:
            seen_dictionary[node1.name] = True
            return checker(node2, node1.ancestor, seen_dictionary)
    else:
        print("node was none, checking next:", node2.name, "None")
        return checker(node2, None, seen_dictionary)
