# time: O(m*n)
# space: O(m*n) for the output array
def spiralTraverse(array):
    traversing_row = True  # flips after each for loop
    row_forward, col_forward = True, True  # doesn't flip after each for loop
    output_array = []

    top_row = 0
    bottom_row = len(array) - 1
    first_col = 0
    last_col = len(array[0]) - 1

    while top_row <= bottom_row and last_col >= first_col:
        if traversing_row:
            if row_forward:
                for i in range(first_col, last_col + 1):
                    output_array.append(array[top_row][i])
                top_row += 1
                row_forward = False
                traversing_row = False
            else:
                for i in range(last_col, first_col - 1, -1):
                    output_array.append(array[bottom_row][i])
                bottom_row -= 1
                row_forward = True
                traversing_row = False
        else:
            if col_forward:
                for i in range(top_row, bottom_row + 1):
                    output_array.append(array[i][last_col])
                last_col -= 1
                col_forward = False
                traversing_row = True
            else:
                for i in range(bottom_row, top_row - 1, -1):
                    output_array.append(array[i][first_col])
                first_col += 1
                col_forward = True
                traversing_row = True

    return output_arrayy