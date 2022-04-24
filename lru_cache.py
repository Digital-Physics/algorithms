# LRU is like Memoization but it sets a (memory) limit of how many key-value pairs it caches
# instead of storing value directly in dict, store reference to value in doubly linked list node
# if you have the pointer/position of a value in a doubly linked list, you can update it in constant time
# keep track of head (last keyed/inserted value) and tail (node to remove from cache if it reaches limit)
# LRU is a compound data structure using a dictionary/hash table in conjunction with a doubly linked list
# So just as efficient as Memoization via a hash/dict, but we can limit the memory size and drop infrequently used values from Memory
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.cache = {}
        self.doubly_linked_list = Doubly_linked_list()


# time: O(1); space: O(1)
def insertKeyValuePair(self, key, value):
    print()
    print("insert", key)
    if key not in self.cache and len(self.cache.keys()) == self.maxSize:
        print("need to drop the LRUsed tail to make space for the new key-value pair")
        del self.cache[self.doubly_linked_list.tail.key]
        self.doubly_linked_list.remove_tail()

    if key not in self.cache:
        print("make a new node for key-value pair that isn't in cache")
        doubly_node = Doubly_linked_list_node(key, value)
        print("make new node the head of the doubly linked list since it was last keyed or added")
        self.doubly_linked_list.set_head_to(doubly_node)
        print()
        print("put the node, already properly inserted in to the Doubly LL, into the cache/dict/hash")
        self.cache[key] = doubly_node
    else:
        self.cache[key].value = value
        self.doubly_linked_list.set_head_to(self.cache[key])


# time: O(1); space: O(1)
def getValueFromKey(self, key):
    print()
    print("get value from key:", key)
    if key in self.cache:
        if key == self.doubly_linked_list.tail.key:
            if self.doubly_linked_list.tail != self.doubly_linked_list.head:
                print("getVal requires us to update tail, not just head, since value of tail was requested")
                self.doubly_linked_list.tail = self.doubly_linked_list.tail.prev
                print("new tail:", self.doubly_linked_list.tail)
        print("updating head of doubly linked list")
        self.doubly_linked_list.set_head_to(self.cache[key])
    return self.cache[key].value
    else:
    return None


# time: O(1); space: O(1)
def getMostRecentKey(self):
    if self.doubly_linked_list.head is not None:
        return self.doubly_linked_list.head.key
    else:
        return None


class Doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head_to(self, node):
        # edge case; first time
        print()
        print("set head")
        print("self.head.key before update", self.head.key if self.head is not None else None)
        if self.head is None:
            self.head = node
            self.tail = node
        # return
        else:
            self.head.prev = node

        # remove bindings & connect adjacent nodes
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev

        node.next = self.head
        node.prev = None
        self.head = node
        print("self.head.key after update", self.head.key)
        print("self.tail.key after update", self.tail.key)

    def remove_tail(self):
        if self.tail == self.head:
            self.head = None
            self.tail = None
        if self.tail is not None:
            self.tail = self.tail.prev
            self.tail.next = None


class Doubly_linked_list_node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None





