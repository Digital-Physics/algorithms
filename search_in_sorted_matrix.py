time: O(m + n)
space: O(1)
def searchInSortedMatrix(matrix, target):
    # start the row and column idx at extremes
    # make it so that if target is too big/small it implies one move of idx
    i = len(matrix) - 1
    j = 0

    while i >= 0 and j <= len(matrix[0]):
        if matrix[i][j] == target:
            return [i, j]
        elif matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1

    return [-1, -1]
