# almost sounds like LUCA, last universal common ancestor
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

# time: O(h) since we are at most going up 2 branches the height of the tree
# space: O(h) because we have a recursive call stack and a dictionary
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


# not sure what problem we were doing above where we had an Ancestral tree; I'll have to look back into later. In the meantime, here's this approach:

class Node:
    def __init__(self, key, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

# Lowest Common Ancestor of a Binary Tree of node A and B
# step 1: Find the paths to node A & B.
# Step 2: See where paths diverge. The last note they had in common before they diverge is the the LCA

def findPath(root, path, k):
    if root is None:
        return False
    
    path.append(root.key) # discarded at end if not used
    print(root.key, path, k)
 
    if root.key == k:
        return True
 
    # Check if k is found in left or right sub-tree
    if ((root.left != None and findPath(root.left, path, k)) or (root.right != None and findPath(root.right, path, k))):
        return True
 
    path.pop()
    return False
 
# Returns LCA if node n1 and n2 are present in the given binary tree, otherwise return -1
def findLCA(root, n1, n2):
    path1 = []
    path2 = []
 
    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1
 
    # Compare path to see where they diverge
    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]
 
 
# Driver program to test above function
if __name__ == '__main__':
     
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
     
    print("LCA(4, 5) = %d" % (findLCA(root, 4, 5,)))
    print("LCA(4, 6) = %d" % (findLCA(root, 4, 6)))
    print("LCA(3, 4) = %d" % (findLCA(root, 3, 4)))
    print("LCA(2, 4) = %d" % (findLCA(root, 2, 4)))

