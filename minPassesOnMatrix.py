# time: O(m*n)
# space: O(m*n)
def minimumPassesOfMatrix(matrix):
    # for all positives, go through bfs find all negatives of distance one, convert them for recursive call, round =+ 1
    seen = [[False for row in range(len(matrix[0]))] for col in range(len(matrix))]
    count_down = len(matrix[0]) * len(matrix)
    positives = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] > 0:
                positives.append((i, j))
                count_down -= 1
                seen[i][j] = True
            elif matrix[i][j] == 0:
                count_down -= 1
                seen[i][j] = True

    return bfsHelper(positives, matrix, seen, count_down)


def bfsHelper(positive_idxs, matrix, seen, count_down, round_counter=0):
    print(positive_idxs, round_counter, count_down)
    if len(positive_idxs) == 0:
        if count_down == 0:
            # why -1? it takes a round to just clear out initial positives
            return round_counter - 1
        else:
            return -1
    next_round_positive_idxs = []

    # like a BFS queue???
    while positive_idxs:
        curr_node = positive_idxs.pop(0)
        i = curr_node[0]
        j = curr_node[1]
        for adj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (0 <= adj[0] < len(matrix)) and (0 <= adj[1] < len(matrix[0])):
                if not seen[adj[0]][adj[1]]:  # must be negative, right? seen everything else
                    seen[adj[0]][adj[1]] = True
                    # if matrix[adj[0]][adj[1]] < 0:
                    print(adj[0], adj[1], matrix[adj[0]][adj[1]])
                    next_round_positive_idxs.append((adj[0], adj[1]))
                    count_down -= 1

    return bfsHelper(next_round_positive_idxs, matrix, seen, count_down, round_counter + 1)





