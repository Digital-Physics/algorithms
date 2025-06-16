from typing import List, Set, Tuple

# time complexity: m x n x 3**word_length

def word_search(target: str, matrix: List[List[str]]) -> bool:
    rows, cols = len(matrix), len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target[0]:

                stack = [(i, j, 0, set([(i, j)]))]  # (row, col, target_idx matched on, visited_set)

                while stack:
                    r, c, idx, visited = stack.pop()

                    if idx == len(target) - 1:
                        return True

                    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and matrix[nr][nc] == target[idx + 1]):
                            stack.append((nr, nc, idx + 1, visited | {(nr, nc)}))

    return False


# ['a', 'b', 'c', 'e'],
# ['s', 'f', 'c', 's'], 
# ['a', 'd', 'e', 'e']

if __name__ == "__main__":
    print(word_search("seep", [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]))
    print(word_search("seed", [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]))