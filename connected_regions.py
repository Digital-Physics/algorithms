from typing import List
from collections import deque

def connectedCell_v1(matrix: List[List[int]]) -> int:
    """return the max connected region"""
    max_region = 0
    visited = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if (i, j) not in visited and matrix[i][j] == 1:
                # start BFS
                curr_region = 0
                q = deque([(i, j)])
                visited.add((i, j))

                while q:
                    row, col = q.popleft()

                    if matrix[row][col] == 1:
                        curr_region += 1
                        
                        if curr_region > max_region:
                            max_region = curr_region
                    
                    for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
                                 max(min(col + neighbor[1], len(matrix[0]) - 1), 0))

                        if neigh not in visited and matrix[neigh[0]][neigh[1]] == 1:
                            visited.add(neigh)
                            q.append(neigh)  
            else:
                visited.add((i, j))

    return max_region


def connectedCell_v2(matrix: List[List[int]]) -> int:
    """return the max connected region"""
    max_region = 0
    visited = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            visited.add((i, j))

            if matrix[i][j] == 1:
                # start BFS
                curr_region = 0
                q = deque([(i, j)])

                while q:
                    row, col = q.popleft()
                    # visited.add((row, col))  # the starting cell was already added, but that's ok

                    if matrix[row][col] == 1:
                        curr_region += 1
                        
                        if curr_region > max_region:
                            max_region = curr_region
                    
                        for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                            neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
                                    max(min(col + neighbor[1], len(matrix[0]) - 1), 0))

                            if neigh not in visited and matrix[neigh[0]][neigh[1]] == 1:
                                visited.add(neigh)
                                q.append(neigh)  

    return max_region

def connectedCell(matrix: List[List[int]]) -> int:
    """return the max connected region"""
    max_region = 0
    visited = set()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            visited.add((i, j))

            if matrix[i][j] == 1:
                # start BFS
                curr_region = 0
                q = deque([(i, j)])

                while q:
                    row, col = q.popleft()

                    if matrix[row][col] == 1:
                        curr_region += 1
                        
                        if curr_region > max_region:
                            max_region = curr_region
                    
                        for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:  # the number of neighbors != 4, but 8 (Von Neumann, Moore neighborhood)
                            neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
                                    max(min(col + neighbor[1], len(matrix[0]) - 1), 0))

                            if neigh not in visited and matrix[neigh[0]][neigh[1]] == 1:
                                visited.add(neigh)
                                q.append(neigh)  

    return max_region

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    m = int(input().strip())

    matrix = []

    for _ in range(n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = connectedCell(matrix)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()