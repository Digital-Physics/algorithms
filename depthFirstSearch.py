# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    # used for grader to construct node list
    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # note: array = [] as input; it will be modified and returned as output
        # initialize DFS priority stack
        DFS_stack = []
        # put starting/root node in stack to process
        DFS_stack.append(self)

        while DFS_stack:
            # pop and process
            current_node = DFS_stack.pop()
            array.append(current_node.name)

            # children are other node objects
            while current_node.children:
                # pop from list of children and put in DFS stack
                DFS_stack.append(current_node.children.pop())

        return array

    # recursive approach
    def depthFirstSearch2(self, array):
        # O(V+E) time complexity for recursive implementation
        # Worst: O(V) space in the case of a tree with just one branch
        array.append(self.name)
        for child in self.children:
            # note: the recursive call doesn't need a return...
            # the recursive call is just making an update to something that gets passed in
            # the final answer will only get returned once
            child.depthFirstSearch(array)
        return array
