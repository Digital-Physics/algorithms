# time: O(n*r) where n is length of blocks and r is length of reqs
# space: O(n*r) where n is length of blocks and r is length of reqs
def apartmentHunting(blocks, reqs):
    distances = [[float("inf") for _ in range(len(reqs))] for _ in range(len(blocks))]
    for i, req in enumerate(reqs):
        if blocks[0][req]:
            distances[0][i] = 0

    for block_idx in range(1, len(blocks)):
        for req_idx, place in enumerate(reqs):
            if blocks[block_idx][place]:
                distances[block_idx][req_idx] = 0
            else:
                distances[block_idx][req_idx] = distances[block_idx - 1][req_idx] + 1
        print("front pass distances:", distances)

    best_metric = max(distances[-1])
    best_index = len(distances) - 1
    print()

    back = [[float("inf") for _ in range(len(reqs))] for _ in range(len(blocks))]
    for i, req in enumerate(reqs):
        if blocks[-1][req]:
            back[-1][i] = 0

    for block_idx in reversed(range(len(blocks) - 1)):
        for req_idx, place in enumerate(reqs):
            if blocks[block_idx][place]:
                back[block_idx][req_idx] = 0
            else:
                back[block_idx][req_idx] = back[block_idx + 1][req_idx] + 1

            if back[block_idx][req_idx] < distances[block_idx][req_idx]:
                # overwrite
                distances[block_idx][req_idx] = back[block_idx][req_idx]

        print()
        print("distances after update", distances)
        print("back", back)
        max_dist = max([distances[block_idx][i] for i in range(len(reqs))])
        print("distance for block", block_idx, "is", max_dist)

        if max_dist < best_metric:
            best_metric = max_dist
            best_index = block_idx

        print("best", best_metric, best_index)

    return best_index
