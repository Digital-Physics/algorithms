from typing import List
from collections import defaultdict
import heapq

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    """"return up to 3 product strings associated with each prefix of searchWord. like autocomplete.
    e.g. searchWord: "mouse" =>
    ["m", "mo", "mou", "mous", "mouse"] => [["mailbox", "motorcycle", "mouse"], ...["mouse", "mousepad"]]

    Let's use Ed Fredkin's (prefix) Trie, which is like a nested hash table.

    # "aba", "bar", "bab"
    {'a':{'b':{'a':{'end': True}}, 'b':{'a':{'r': {'end': True}}}

    but let's make a custom class to keep track of the top three words at that node (in a priority heap).
    """
    class TrieNode:
        def __init__(self):
            self.children = defaultdict(TrieNode)
            # we also need a top 3 items at each Trie node (which corresponds to a prefix, e.g. "mou" )
            # if someone puts in m, o, u, the algo keys m and get dictionaries with "ma", "me", "mo" keys, then "mo" returns...
            self.max_heap = [] # we want a max heap so we can pop off the last lexicographically ordered word
        
        def add_suggestion(self, product: str) -> None:
            if len(self.max_heap) < 3:
                # heappush suggestion because we haven't hit size limit yet
                heapq.heappush(self.max_heap, MaxHeapStr(product))
            else:
                # if the heaps last word (top of the max_heap) comes after it alphabetically 
                if self.max_heap[0].string > product: 
                    heapq.heappop(self.max_heap)
                    heapq.heappush(self.max_heap, MaxHeapStr(product))
        
        def get_suggestion(self) -> None: # it's in the heap of size 3 words, but it needs to be reversed
            # we want it from a -> z but it was sorted the opposite way for eviction/popping purposes
            return sorted(self.max_heap, reverse = True)
    
    class MaxHeapStr(str):
        """this custom class with dunder methods is made to accommodate heapq not being able to do string comparisons"""
        def __init__(self, string: str): 
            self.string = string

        def __lt__(self, other: "MaxHeapStr") -> bool: # operator overload on ">" so heaps can compare to of these objects
            return self.string > other.string
        
        def __eq__(self, other: "MaxHeapStr") -> bool: # operator overload for "=="
            return self.string == other.string
    
    root = TrieNode()

    # construct trie
    for product in products:
        node = root # each word starts at the root which gets mutated from word to word
        
        for character in product:
            node = node.children[character] # node is a TrieNode (new or existing) one nested level deeper
            node.add_suggestion(product) # add the whole word for ranking at this level
    
    output = []
    node = root

    for char in searchWord:
        node = node.children[char]
        output.append(node.get_suggestion()) # already available and created during the trie construction (just reversed here)

    return output