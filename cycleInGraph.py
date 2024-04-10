# time and space complexity could be done better
# could hold vector of information about what is in path to check for back edges
# optimal complexity still to code would be O(v+e) time amd O(v) space
def cycleInGraph(edges):
    for root in range(len(edges)):
        # breadth or depth fist search
        bfs_queue = []
        # don't want to see root right away so load in edges/children/other_nodes right away
        for other_node in edges[root]:
            bfs_queue.append(other_node)
        seen = {}

        while bfs_queue:
            curr_node = bfs_queue.pop(0) # should use deque's .popleft()
            print(curr_node)
            if curr_node == root:
                return True
            elif curr_node not in seen:
                seen[curr_node] = True
                for other_node in edges[curr_node]:
                    bfs_queue.append(other_node)

    return False
