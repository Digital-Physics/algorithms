# time: O(n) for one pass
# space: O(n) for output we build up and pass
def sunsetViews(buildings, direction):
    output = []
    max_thus_far = 0

    if direction == "EAST":
        idx = len(buildings) - 1
        while idx >= 0:
            if buildings[idx] > max_thus_far:
                output = [idx] + output
                max_thus_far = buildings[idx]
            idx -= 1
    else:
        idx = 0
        while idx < len(buildings):
            if buildings[idx] > max_thus_far:
                output.append(idx)
                max_thus_far = buildings[idx]
            idx += 1

    return output
