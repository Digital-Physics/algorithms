# time: O(m*n) even though we do a BFS for some because we only do it on up to 4 (constant) nodes
# space: O(m*n) for the seen matrix
def removeIslands(matrix):
    help = bfsHelper(matrix)
    return help.scan()


class bfsHelper():
    def __init__(self, matrix):
        self.matrix = matrix
        self.seen = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        # self.output_array = []

    def scan(self):
        # find next unseen by (inefficiently?) scanning through matrix
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(i, j)
                if self.seen[i][j] is False:
                    print("not seen")
                    print(self.matrix)
                if self.matrix[i][j] == 0:
                    self.seen[i][j] = True
                else:
                    # don't worry, we will mark this cell/node as seen in bfs
                    self.bfs(i, j)

    return self.matrix


def bfs(self, i, j):
    # init stack or queue
    bfs_queue = [(i, j)]
    hit_wall = False
    potential_nodes_to_flip = []


while bfs_queue:
    # pop and process
    curr_node = bfs_queue.pop(0)
    potential_nodes_to_flip.append(curr_node)
    i = curr_node[0]
    j = curr_node[1]

    if not self.seen[i][j]:
        if self.matrix[i][j] == 1:
            self.seen[i][j] = True
            # add children to bfs queue
            for adj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= adj[0] < len(self.matrix)) and (0 <= adj[1] < len(self.matrix[0])):
                    if not self.seen[adj[0]][adj[1]]:
                        bfs_queue.append(adj)
                        else:
                        hit_wall = True
    else:
        self.seen[i][j] = True

    if not hit_wall:
        for node in potential_nodes_to_flip:
            i = node[0]
    j = node[1]
    self.matrix[i][j] = 0

