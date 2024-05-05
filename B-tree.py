# https://www.youtube.com/watch?v=K1a2Bk8NrYQ
# B-trees can have several values within each node, n, which partition the pointers to n + 1 children nodes 
# the number of keys/values within each node will have a max, say 4
# the min number of keys within each node will be 4/2, so a node can have 2, 3, or 4 values
# you may have to do more comparisons than a binary tree within each node, but these are quick
# retrieving the children nodes is more expensive, and that is why B-trees may be better for databases
# adding and removing elements can be tricky, but keep in mind the properties a B-tree
# nodes can be half to fully full (e.g. 2-4)
# so if you insert and reach 5, you'll need to find the middle one and move it to the parent and split the other two into separate nodes
# this can be done recursively since what if moving the middle node to the parent caused it to overflow
# similarly, we'll have to do reorganization when removing keys/values in nodes if our count drops below 2

class Node:
    def __init__(self, leaf=True):
        self.leaf = leaf # it is a leaf at init, because no children yet
        self.keys = [] # analogous to .value in Binary Trees
        self.children = [] # we are used to .left and .right attributes, but here we work with ordered lists

    def split_child(self, i, child):
        new_node = Node(leaf=child.leaf)
        self.children.insert(i + 1, new_node)
        self.keys.insert(i, child.keys[2])
        new_node.keys = child.keys[3:]
        child.keys = child.keys[:2]

        if not child.leaf:
            new_node.children = child.children[2:]
            child.children = child.children[:2]

    def insert_non_full(self, value):
        i = len(self.keys) - 1
        if self.leaf: # we only insert new keys into leaves
            # use None to find the position so we have the correct number of elements
            # then insert the actual value to replace None
            self.keys.append(None)
            while i >= 0 and value < self.keys[i]:
                self.keys[i + 1] = self.keys[i]
                i -= 1
            self.keys[i + 1] = value
        else: # find the correct child node/path to insert into (we'll recursively check if it's a leaf)
            while i >= 0 and value < self.keys[i]:
                i -= 1
            i += 1 # we've gone too far in our check, so the path/partition is the key index + 1
            if len(self.children[i].keys) == 4:
                self.split_child(i, self.children[i])
                if value > self.keys[i]:
                    i += 1 # we've gone too far in our check, so the path/partition is the key index + 1
            self.children[i].insert_non_full(value)

    def insert(self, value):
        if len(self.keys) == 4:
            new_root = Node(leaf=False)
            new_root.children.append(self)
            new_root.split_child(0, self)
            new_root.insert_non_full(value)
            return new_root
        else:
            self.insert_non_full(value)
            return self

    def __str__(self):
        if self.leaf:
            return f"Leaf Node: {self.keys}"
        return f"Non-leaf Node: {self.keys}"


class BTree:
    def __init__(self):
        self.root = Node()

    def insert(self, value):
        self.root = self.root.insert(value)

    def __str__(self):
        """better string representation for printing the BTree object as a string in the terminal.
        we show the values of the root Node object, and how it is represented as a string."""
        return str(self.root)


# Example usage
btree = BTree()
for i in range(10, 100, 10):
    btree.insert(i)

print(btree)
print("children one level below:")
for child_node in btree.root.children:
    print(child_node)
