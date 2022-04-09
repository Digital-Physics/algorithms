# time: O(m*n) even though we do a BFS for some because we only do it on up to 4 (constant) nodes
# space: O(m*n) for the seen matrix
def riverSizes(matrix):
    help = bfsHelper(matrix)
    return help.scan()


class bfsHelper():
    def __init__(self, matrix):
        self.matrix = matrix
        self.seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.output_array = []

    def scan(self):
        # find next unseen by (inefficiently?) scanning through matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(i, j)
                if self.seen[i][j] is False:
                    print("not seen")
                    if self.matrix[i][j] == 0:
                        self.seen[i][j] = True
                    else:
                        # we will mark as seen in bfs
                        self.output_array.append(self.bfs(i, j))

        return self.output_array

    def bfs(self, i, j):
        # init stack or queue
        bfs_queue = [(i, j)]
        river_counter = 0

        while bfs_queue:
            # pop and process
            curr_node = bfs_queue.pop(0)
            i = curr_node[0]
            j = curr_node[1]

            if not self.seen[i][j]:
                if self.matrix[i][j] == 1:
                    self.seen[i][j] = True
                    river_counter += 1
                    # add children to bfs queue
                    for adj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                        if (0 <= adj[0] < len(self.matrix)) and (0 <= adj[1] < len(self.matrix[0])):
                            if not self.seen[adj[0]][adj[1]]:
                                bfs_queue.append(adj)
                else:
                    self.seen[i][j] = True

        return river_counter