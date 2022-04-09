# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # time: O(v+e) see each node once and each children
    # why not O(v)?
    # 1) you have a for children loop in while loop
    # 2) you put nodes in the stack without processing them; need to wait to pop it
    # space: O(v) since we build up an array
    def breadthFirstSearch(self, array):
        # initialize dfs stack or bfs queue
        bfs_queue = []
        bfs_queue.append(self)

        while bfs_queue:
            # pop (first) and process
            curr_node = bfs_queue.pop(0)
            array.append(curr_node.name)
            for child in curr_node.children:
                bfs_queue.append(child)

        return array