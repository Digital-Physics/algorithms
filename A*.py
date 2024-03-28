# time: O(n*log(n)) = O((w*h)log(w*h))
# while heap not empty, worst = w*h (pop off heap and refresh log(w*h) + insert 4*log(w*h))
# space: O(n) = O(w*h) for minHeap storage
# A* is an informed search algorithm that uses a heuristic to determine what node to explore out from next
# Best First Search (at least "best" according to a remaining distance heuristic that doesn't overestimate) 
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    print("start")
    # matrix_info is just like the input matrix but with more info per node/cell
    matrix_info = initialize_nodes_in_matrix(graph, startRow, startCol, endRow, endCol)

    curr_node = matrix_info[startRow][startCol]

    # a priority queue w/ log time to get min would be better than linear search for best node to explore next
    # sorting would take O(n*Log(n)) time to create, constant time O(1) for getting min, and O(log(n)) time to insert
    # Min Heap can be constructed in linear time O(n), O(log(n)) to get min (for Sift Down refresh), and O(log(n)) to insert
    # Initialize Min Heap (which is a tree, but really is just a list with certain properties and methods)
    nodes_to_check = Min_heap([curr_node])

    while nodes_to_check.length > 0:
        curr_node = nodes_to_check.remove()  # remove the min root in the heap and Sift Down to rebuild
        print()
        print("curr node i, j", curr_node.i, curr_node.j)
        print("distance from start", curr_node.distance_from_start)
        print("est distance left (lower bound)", curr_node.est_distance_left)
        print("total estimate (lower bound)", curr_node.total_est_distance)

        if curr_node.i != endRow or curr_node.j != endCol:
            neighbors = get_valid_neighbors(curr_node, matrix_info)
        else:
            break

        for neighbor in neighbors:
            print("neighbor i j", neighbor.i, neighbor.j)
            if not neighbor.seen:
                neighbor.distance_from_start = curr_node.distance_from_start + 1
                neighbor.parent = curr_node
                neighbor.seen = True
                nodes_to_check.insert(neighbor)
            else:
                if curr_node.distance_from_start + 1 < neighbor.distance_from_start:
                    neighbor.distance_from_start = curr_node.distance_from_start + 1
                    neighbor.parent = curr_node
                    # total est distance updates automatically, but object in heap is out of place
                    nodes_to_check.refresh(neighbor)

        # we've seen all the neighbors
        curr_node.processed = True

    return get_path(endRow, endCol, matrix_info)


class Node_info():
    def __init__(self, i, j, val, startRow, startCol, endRow, endCol):
        self.i = i
        self.j = j
        self.wall = True if val == 1 else False
        # "g" will get updated during search based on walls hit; can't calc Manhattan Dist est. before seen
        self.distance_from_start = 0 if (i == startRow and j == startCol) else None
        # the fact that our graph is also a matrix allows us to estimate a distance to another node we haven't seen
        # our heuristic is the Manhattan dist estimate to the end node, assuming no walls
        # this heuristic works because it never overestimates the remaining distance...
        # so if we find the goal, we know there aren't other nodes we could have searched out from which would have gotten there in less steps
        self.est_distance_left = abs(endRow - i) + abs(endCol - j)  # "h" for heuristic
        self.parent = None  # will allow us to trace back path
        self.processed = False  # True after visiting all valid neighbors
        self.seen = False

    # making total distance a method since attributes with functions don't automatically refresh
    # the property decorator allows us to call the method without the brackets and treat it like an attribute
    @property
    def total_est_distance(self):
        if self.distance_from_start is not None:
            return self.distance_from_start + self.est_distance_left  # f
        else:
            return None


def initialize_nodes_in_matrix(matrix_graph, startRow, startCol, endRow, endCol):
    matrix_info = []

    for i, row in enumerate(matrix_graph):
        temp_row = []
        for j, val in enumerate(row):
            temp_row.append(Node_info(i, j, val, startRow, startCol, endRow, endCol))
        matrix_info.append(temp_row)

    return matrix_info


def get_valid_neighbors(curr_node, matrix_info):
    potential_neighbor_idx = [[curr_node.i + 1, curr_node.j],
                              [curr_node.i - 1, curr_node.j],
                              [curr_node.i, curr_node.j + 1],
                              [curr_node.i, curr_node.j - 1]]

    neighbor_node_list = []

    for i, j in potential_neighbor_idx:
        if 0 <= i < len(matrix_info) and 0 <= j < len(matrix_info[0]):
            if not matrix_info[i][j].wall and not matrix_info[i][j].processed:
                neighbor_node_list.append(matrix_info[i][j])

    return neighbor_node_list


def get_path(endRow, endCol, matrix_info):
    path = []
    curr_node = matrix_info[endRow][endCol]

    if curr_node.distance_from_start is None:
        return []

    while curr_node.distance_from_start != 0:
        print("path", path)
        print("curr_node position idx and distance", curr_node.i, curr_node.j, curr_node.distance_from_start)
        # rather than path = path + [curr_node.parent] concatenation which take time, append and reverse
        path.append([curr_node.i, curr_node.j])
        curr_node = curr_node.parent

    # append start node
    path.append([curr_node.i, curr_node.j])

    return path[::-1]


# modification note: elements in our Min Heap array are Node Class objects, not just integers
class Min_heap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    @property
    def length(self):
        return len(self.heap)

    def node_idx(self, node):
        return self.heap.index(node)

    # time: O(n) constructing a min heap and removing the min is quicker than sorting in O(n*log(n)) and having BST retrieval
    # space: O(1) swaps of elements in array/heap done in place
    def buildHeap(self, array):
        # use siftDown over siftUp since it is faster for majority of nodes (towards bottom)
        # last parent in tree is needed...
        # you don't need to siftDown any leaf nodes so just start with the last parent in heap-list tree
        # heap index property: min is 0 index, then l_idx = curr_idx * 2 + 1 and r_idx = curr_idx * 2 + 2
        last_parent_idx = ((len(array) - 1) - 1) // 2
        for curr_idx in reversed(range(last_parent_idx + 1)):  # +1 to include it in range
            self.siftDown(curr_idx, array)
        return array  # for init method

    # time: O(logn)
    # space: O(1)
    def siftDown(self, curr_idx, heap):  # (in a min heap, not a max heap)
        l_idx = curr_idx * 2 + 1

        while l_idx <= len(heap) - 1:
            r_idx = curr_idx * 2 + 2
            if r_idx > len(heap) - 1:
                r_idx = None

            if r_idx is not None and heap[r_idx].total_est_distance < heap[l_idx].total_est_distance:
                potential_swap = r_idx
            else:
                potential_swap = l_idx

            if heap[potential_swap].total_est_distance < heap[curr_idx].total_est_distance:
                heap[potential_swap], heap[curr_idx] = heap[curr_idx], heap[potential_swap]
                potential_swap, curr_idx = curr_idx, potential_swap
                l_idx = curr_idx * 2 + 1
            else:
                break

    # time: O(logn)
    # space: O(1)
    def siftUp(self, curr_idx, heap):  # (used for adding a new element in a Min Heap)
        parent_idx = (curr_idx - 1) // 2
        # do iterative instead of recursion
        while curr_idx > 0 and heap[parent_idx].total_est_distance > heap[curr_idx].total_est_distance:
            heap[parent_idx], heap[curr_idx] = heap[curr_idx], heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

    # time: O(1)
    # space: O(1)
    def peek(self):
        return self.heap[0]

    # time: O(logn)
    # space: O(1)
    def remove(self):  # (the top of the heap) (and return it)
        # (since heap not sorted, it is not meant for quick removal of other values)
        # swap first/top and last and then remove last(which was top) before siftDown on temp top
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        removed_value = self.heap.pop()
        self.siftDown(0, self.heap)
        return removed_value

    # time: O(logn)
    # space: O(1)
    def insert(self, node):
        # add val to the end of the heap tree, and then sift it up into place
        self.heap.append(node)
        self.siftUp(len(self.heap) - 1, self.heap)

    def refresh(self, node):
        self.siftUp(self.node_idx(node), self.heap)


# test
graph = [
  [0, 0, 0, 0, 0],
  [0, 1, 1, 1, 0],
  [0, 0, 0, 0, 0],
  [1, 0, 1, 1, 1],
  [0, 0, 0, 0, 0]]

path = aStarAlgorithm(0, 1, 4, 3, graph)

print(path)