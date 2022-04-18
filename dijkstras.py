# dijkstra's algorithm is a (greedy) algorithm for finding min distances from a start node to all other nodes in a graph
# to find min distances to all other nodes, it starts with the current shortest distance from start node to all nodes
# note: min Heap was not used to find the vertex w/ shortest distance, but it would be quicker
# time: O(v**2 + e) where if we used a Min Heap it would be O(v+e)*log(v)
# space: O(v)
def dijkstrasAlgorithm(start, edges):
    # initialize distances from start node idx to all other node idxs
    min_distances = [float("inf") for _ in range(len(edges))]
    min_distances[start] = 0

    # could have used list since we'd have the index and therefore could do constant time insertion and retrieval
    # could have used dictionary/hash with constant time insertions and retrieval
    # all three have constant time ways to check if an element has been visited
    visited = set()

    while len(visited) != len(edges):
        vertex, curr_min_distance = get_min_dist_vertex(min_distances, visited)

        if curr_min_distance == float("inf"):
            # since it is a greedy algorithm, there's no more nodes to analyze
            break

        visited.add(vertex)

        # now go through adjacency edges for min distance (from start node) vertex
        for edge in edges[vertex]:
            destination_vertex_idx, distance_to_dest = edge

            if destination_vertex_idx in visited:
                # if we've already visited it, we won't find a better path to it
                # ...since our algorithm is greedy
                continue
            else:
                path_dist_for_consideration = curr_min_distance + distance_to_dest

                if path_dist_for_consideration < min_distances[destination_vertex_idx]:
                    min_distances[destination_vertex_idx] = path_dist_for_consideration

    return [distance if distance != float("inf") else -1 for distance in min_distances]


def get_min_dist_vertex(distances, visited):
    # initialize for search in this round
    shortest_distance = float("inf")

    # important: we could create a Min Heap in linear time and get the mins in log time
    for i, distance in enumerate(distances):
        if i in visited:
            continue
        elif distance <= shortest_distance:  # <= because we still want to return infinity nodes at the end
            vertex = i
            shortest_distance = distance

    return vertex, shortest_distance
