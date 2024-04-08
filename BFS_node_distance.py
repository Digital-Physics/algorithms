from typing import List
from collections import deque, defaultdict

def bfs(n: int, m: int, edges: List[List[int]], s: int) -> List[int]:
    """return distances for each node using a BFS search starting from s.
    nodes are labeled 1-n. m = len(edges)."""

    neighbors_dict = defaultdict(set) 
    # edge distance; edges have weight of 6, and -1 means unreachable
    output_list = [-1 for _ in range(n + 1)]  # we are going to let n nodes go from index 1 to n; we will slice into it starting at idx 1 when returned
    
    # these are normally processed in the neighbor adding step, so we should handle s as part of the initialization
    output_list[s] = 0 # since we are going to reference our current node's distance when adding the neighbor's distance 
    seen = {s}

    deq = deque([s])

    for k, v in edges:
        neighbors_dict[k].add(v)
        neighbors_dict[v].add(k)

    while deq:
        # 1) popleft (pop for DFS stack) and process
        curr_node = deq.popleft()

        # 2) add neighbors to queue (or stack for DFS)
        for neigh in neighbors_dict[curr_node]:
            if neigh not in seen:
                seen.add(neigh)
                output_list[neigh] = output_list[curr_node] + 6
                deq.append(neigh)

    # note: if s is 1, output_list[1:1] = [], which we want
    #       if s = n, output_list[6:] = [], which we want
    return output_list[1:s] + output_list[s+1:]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)
        print(result)

    #     fptr.write(' '.join(map(str, result)))
    #     fptr.write('\n')

    # fptr.close()
