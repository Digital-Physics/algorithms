# time: O(n+m)
# space: O(1)
# this graph problem forces us to move right or down at each step so we can leverage n choose k formula and avoid Dynamic Programming
def numberOfWaysToTraverseGraph(width, height):
    num_of_moves = (width - 1) + (height - 1)
    # choose where to put the rights (or downs)
    numerator = 1
    denominator = 1

    for i in range(num_of_moves, num_of_moves - (width - 1), -1):
        numerator *= i

    for i in range(width - 1, 0, -1):
        denominator *= i

    return numerator / denominator
