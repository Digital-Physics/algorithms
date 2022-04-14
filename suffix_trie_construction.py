# Ed Fredkin, a Digital Physics pioneer, invented/discovered the trie structure
# tries are nested hash tables (dictionaries in Python, objects in JavaScript)
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # time: O(n**2) two nested for loops
    # space: O(n**2) we might have to store every char as an suffix starting point (children of root)
    # ...and as subsequent char in the suffix
    def populateSuffixTrieFrom(self, string):
        for suffix_start in range(len(string)):
            self.insertSuffix(string[suffix_start:])

    # fast for searching for a string within another string (not two for loops)
    # time: O(m) for the size of the string of m chars (constant time hash/char)
    # space: O(1) since we don't create anything new wehen searching through the suffix tree
    def contains(self, string):
        # start at root
        curr_node = self.root

        for char in string:
            if char not in curr_node:
                return False
            else:
                curr_node = curr_node[char]

        if self.endSymbol in curr_node:
            return True
        else:
            return False

    def insertSuffix(self, string):
        # point to root
        curr_node = self.root

        for char in string:
            if char not in curr_node:
                curr_node[char] = {}
            # redefine "root", sort of, or rather, the starting point as we put more hash table nodes in tree
            # we have either added an edge to our trie/tree, or followed one to the next node/hash/dict
            curr_node = curr_node[char]

        # the * key just needs to be in the hash table of the final node
        # curr_node["*"] = 1
        curr_node[self.endSymbol] = True

