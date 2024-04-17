from typing import List

# def countLuck_v1(matrix: List[List[str]], k: int) -> bool:
#     """find only path and then count decision-making turns in path"""
#     # 1a) get start and end 
#     # 1b) create matrix that we can index into
#     for i, str_row in enumerate(matrix):
#         row_list = [*str_row]
#         matrix[i] = row_list

#         for j in range(len(row_list)):
#             if row_list[j] == "M":
#                 start = (i, j)
#                 print("start is", start)
#             if row_list[j] == "*":
#                 end = (i, j)
#                 print("end is", end)
    
#     # 2) find the one and only path (since that is what problem states)
#     # DFS (nodes will tuple of value in cell and path to get there)
#     stack = [(start, [start])]
#     visited = {start}

#     while stack:
#         curr_node, path = stack.pop()
#         # print(f"{curr_node} {path}")
#         row, col = curr_node

#         if curr_node == end:
#             final_path = path
#             # print("path is", final_path) 
#             break
        
#         for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
#                         max(min(col + neighbor[1], len(matrix[0]) - 1), 0))

#             if neigh not in visited and matrix[neigh[0]][neigh[1]] in [".", "*"]:
#                 visited.add(neigh)
#                 stack.append((neigh, path + [neigh]))
    
#     # 3) count turns in path (where there was more than one option for ways to go)
#     direction = None
#     turns = 0
#     prev_node = start
#     i = 0

#     for curr_node in final_path:
#         i += 1
#         if curr_node[0] == prev_node[0]:
#             if direction in ["horizontal", None]:
#                 # check to see if there was more than one way to go
#                 neighbor_set = set()
#                 for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                     neighbor_set.add((max(min(prev_node[0] + neighbor[0], len(matrix) - 1), 0), 
#                             max(min(prev_node[1] + neighbor[1], len(matrix[0]) - 1), 0)))
                    
#                 if sum([1 for neighbor in neighbor_set if matrix[neighbor[0]][neighbor[1]] in [".", "*"] and neighbor not in final_path[:i - 1]]) > 1:
#                     print("neighbor set paths > 1", neighbor_set, "for", prev_node)
#                     turns += 1
                
#             direction = "vertical"
#         else:
#             if direction in ["vertical", None]:
#                 # check to see if there was more than one way to go
#                 neighbor_set = set()
#                 for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#                     neighbor_set.add((max(min(prev_node[0] + neighbor[0], len(matrix) - 1), 0), 
#                             max(min(prev_node[1] + neighbor[1], len(matrix[0]) - 1), 0)))
                    
#                 if sum([1 for neighbor in neighbor_set if matrix[neighbor[0]][neighbor[1]] in [".", "*"] and neighbor not in final_path[:i - 1]]) > 1:
#                     print("neighbor set paths > 1", neighbor_set, "for", prev_node)
#                     turns += 1
                
#             direction = "horizontal"

#         prev_node = curr_node

#     print("turns where there was a decision", turns)

#     return "Oops!" if turns != k else "Impressed"

# def countLuck_v2(matrix: List[List[str]], k: int) -> bool:
#     """find only path and then count decision-making turns in path"""
#     # 1a) get start and end 
#     # 1b) create matrix that we can index into
#     for i, str_row in enumerate(matrix):
#         row_list = [*str_row]
#         matrix[i] = row_list

#         for j in range(len(row_list)):
#             if row_list[j] == "M":
#                 start = (i, j)
#                 print("start is", start)
#             if row_list[j] == "*":
#                 end = (i, j)
#                 print("end is", end)
    
#     # 2) find the one and only path (since that is what problem states)
#     # DFS (nodes will tuple of values cell, path to get there, and 1 if neighbors put on stack greater than 1)
#     stack = [(start, [start], [])]
#     visited = {start}

#     while stack:
#         curr_node, path, decisions = stack.pop()
#         # print(f"{curr_node} {path}")
#         row, col = curr_node
        
#         neighbor_set = set()

#         for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
#                         max(min(col + neighbor[1], len(matrix[0]) - 1), 0))
            
#             neighbor_set.add(neigh)

#         neighbor_set = {neigh for neigh in neighbor_set if neigh != curr_node and neigh not in visited and matrix[neigh[0]][neigh[1]] in [".", "*"]}
#         n_count = len(neighbor_set)

#         for neigh in neighbor_set:
#             visited.add(neigh)
#             stack.append((neigh, path + [neigh], decisions + [1 if n_count > 1 else 0]))
        
#         if curr_node == end:
#             final_path = path
#             final_decisions = decisions + [1 if n_count > 1 else 0]
#             # print("path is", final_path) 
#             break
    
#     # 3) count turns in path (where there was more than one option for ways to go)
#     direction = None
#     turns = 0
#     prev_node = start

#     print(final_path)
#     print(final_decisions)

#     for i, curr_node in enumerate(final_path[1:]):
#         if curr_node[0] == prev_node[0]:
#             if direction in ["horizontal", None]:
#                 # print(curr_node, i, final_decisions[i])
#                 # check to see if there was more than one way to go
#                 if final_decisions[i] == 1:
#                     turns += 1
                
#             direction = "vertical"
#         else:
#             if direction in ["vertical", None]:
#                 # print(curr_node, i, final_decisions[i])
#                 # check to see if there was more than one way to go
#                 if final_decisions[i] == 1:
#                     turns += 1
                
#             direction = "horizontal"

#         prev_node = curr_node

#     print("turns where there was a decision", turns)

#     return "Oops!" if turns != k else "Impressed"

# def countLuck_v3(matrix: List[List[str]], k: int) -> bool:
#     """find only path and then count decision-making turns in path"""
#     # 1a) get start and end 
#     # 1b) create matrix that we can index into
#     for i, str_row in enumerate(matrix):
#         row_list = [*str_row]
#         matrix[i] = row_list

#         for j in range(len(row_list)):
#             if row_list[j] == "M":
#                 start = (i, j)
#                 print("start is", start)
#             if row_list[j] == "*":
#                 end = (i, j)
#                 print("end is", end)
    
#     # 2) find the one and only path (since that is what problem states)
#     # DFS (nodes will tuple of values cell, path to get there, and 1 if neighbors put on stack greater than 1)
#     stack = [(start, [start], [])]
#     visited = {start}

#     while stack:
#         curr_node, path, decisions = stack.pop()
#         # print(f"{curr_node} {path}")
#         row, col = curr_node
        
#         neighbor_set = set()

#         for neighbor in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             neigh = (max(min(row + neighbor[0], len(matrix) - 1), 0), 
#                         max(min(col + neighbor[1], len(matrix[0]) - 1), 0))
            
#             neighbor_set.add(neigh)

#         neighbor_set = {neigh for neigh in neighbor_set if neigh != curr_node and neigh not in visited and matrix[neigh[0]][neigh[1]] in [".", "*"]}
#         n_count = len(neighbor_set)

#         for neigh in neighbor_set:
#             visited.add(neigh)
#             stack.append((neigh, path + [neigh], decisions + [1 if n_count > 1 else 0]))
        
#         if curr_node == end:
#             final_path = path
#             final_decisions = decisions + [1 if n_count > 1 else 0]
#             # print("path is", final_path) 
#             break
    
#     # 3) count turns in path (where there was more than one option for ways to go)
#     print(final_decisions, len(final_decisions))
#     print(final_path, len(final_path))

#     return "Oops!" if sum(final_decisions) != k else "Impressed"

# def countLuck_v4(matrix: List[List[str]], k: int) -> str:
#     # Find start and end points
#     for i, row in enumerate(matrix):
#         for j, cell in enumerate(row):
#             if cell == "M":
#                 start = (i, j)
#             elif cell == "*":
#                 end = (i, j)

#     # Perform DFS to find the path
#     stack = [(start, [start])]
#     visited = {start}
#     decisions = []  # Store the points where there was more than one option

#     while stack:
#         curr_node, path = stack.pop()
#         row, col = curr_node

#         if curr_node == end:
#             final_path = path
#             break

#         valid_neighbors = []
#         for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
#             neigh = (row + dr, col + dc)
#             if 0 <= neigh[0] < len(matrix) and 0 <= neigh[1] < len(matrix[0]) and matrix[neigh[0]][neigh[1]] in [".", "*"] and neigh not in visited:
#                 visited.add(neigh)
#                 valid_neighbors.append(neigh)

#         if len(valid_neighbors) == 1:
#             stack.append((valid_neighbors[0], path + [valid_neighbors[0]]))
#         elif len(valid_neighbors) > 1:
#             # print(curr_node, valid_neighbors)
#             stack.extend((neighbor, path + [neighbor]) for neighbor in valid_neighbors)
#             decisions.append(curr_node)

#     print(decisions)
#     return "Oops!" if len(decisions) != k else "Impressed"


def countLuck(matrix: List[List[str]], k: int) -> str:
    """find the only path (as stated by the problem) and then count decision-making turns in the path.
    note: path not needed, but it's nice to have because it shows how you can have it for other problems"""
    def get_valid_neighbors(node, visited):
        row, col = node
        neighbors = [(row + dr, col + dc) for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]]
        return [(r, c) for r, c in neighbors if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] in [".", "*"] and (r, c) not in visited]

    # Find start and end points
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if cell == "M":
                start = (i, j)
            elif cell == "*":
                end = (i, j)

    stack = [(start, [start], set(start), set())]  # (current node, current path, visited nodes, decisions)

    while stack:            
        curr_node, path, visited, decisions = stack.pop()
        
        if curr_node == end:
            # if len(get_valid_neighbors(curr_node, visited)) > 1:
            #     decisions.add(curr_node)
            break

        valid_neighbors = get_valid_neighbors(curr_node, visited)
        if len(valid_neighbors) == 1:
            stack.append((valid_neighbors[0], path + [valid_neighbors[0]], visited.union({curr_node}), decisions))
        else:
            for neighbor in valid_neighbors:
                stack.append((neighbor, path + [neighbor], visited.union({curr_node}), decisions.union({curr_node})))

    return "Oops!" if len(decisions) != k else "Impressed"

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)
        print(result)

    #     fptr.write(result + '\n')

    # fptr.close()