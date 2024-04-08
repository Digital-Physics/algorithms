from typing import List

def lilysHomework(arr: List[int]) -> int:
    """counts min number of swaps needed to sort list. (either forwards or backwards... that's why it is called "beautiful" in prob.)
    create directed graph showing where each number in list needs to get to, the position in the list. 
    note: connected components in a directed graph are subgraphs which can be reordered 
    all nodes can be reached from any node in the connected component of the graph. 
    there is a cycle. the nodes flow through like a patterned snake the directed graph... 
    but swapping reduces the snake length by one segment, except on the last where it reduces it by two. 
    Therefore, the min swaps needed to sort a connected component subgraph is #nodes_in_comp - 1.

    """
    n = len(arr)
    arr_w_idx = [(i, val) for i, val in enumerate(arr)]
    arr1 = sorted(arr_w_idx, key=lambda x: x[1])
    arr2 = reversed(arr1)

    destination_graph1 = [tup[0] for tup in arr1]
    destination_graph2 = [tup[0] for tup in arr2]

    def run_twice(destination_graph):
        global_swap_count = 0
        visited_sorted = [False] * n

        # one dfs traversal counts n-1 edges in a component
        # but 994 open recursive calls lead to a recursion error, maximum recursion depth exceeded... 
        # we don't need to do it this way with open recursive calls... we can do it iteratively
        # def dfs(node):
        #     nonlocal global_swap_count
        #     visited_sorted[node] = True
        #     for neighbor in [destination_graph[node]]:
        #         if not visited_sorted[neighbor]:
        #             global_swap_count += 1
        #             dfs(neighbor)

        def dfs(node):
            """iterative, not recursive"""
            nonlocal global_swap_count
            visited_sorted[node] = True

            while not visited_sorted[destination_graph[node]]:
                node = destination_graph[node]  # there is only one neighbor in this directed graph
                visited_sorted[node] = True
                global_swap_count += 1
        
        for i in range(n):
            if not visited_sorted[i]:
                dfs(i)
        
        return global_swap_count
    
    return min(run_twice(destination_graph1), run_twice(destination_graph2))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    # arr = [i+2 for i in range(100000)] + [1]

    result = lilysHomework(arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
