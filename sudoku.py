# we did not use backtracking; we saved the sate of the board at DFS node, which takes more memory
# we did however narrow down the DFS search by eliminating some possibilities up front
# watch Tim's method of backtracking.
# I think you could do backtracking after narrowing down possibilities, but it gets messy
#
def solveSudoku(board):
    possibilities = [[[i for i in range(1, 10)] for _ in range(9)] for _ in range(9)]

    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                possibilities = update_possibilities(board[i][j], i, j, possibilities)

    print("initial possibilities:", possibilities)

    # initialize DFS stack
    moves = []
    first_i, first_j = next_open_cell(0, 0, board)
    new_moves = possibilities_into_children_moves(possibilities, first_i, first_j, board)
    for move in new_moves:
        moves.append(move)

    while moves:
        i, j, idx_poss, board = moves.pop()
        print()
        print("next play is", possibilities[i][j][idx_poss], "in cell", i, j)
        print("sum of board cells before next play:", sum([sum(row) for row in board]))

        # generator comprehension allows us to avoid generating a whole list of Falses if one was all we needed
        if all(sum(row) == 45 for row in board):
            return board

        if is_valid(possibilities[i][j][idx_poss], i, j, board):
            board[i][j] = possibilities[i][j][idx_poss]

            # get next open cell
            idx_i, idx_j = next_open_cell(i, j, board)

            new_moves = possibilities_into_children_moves(possibilities, idx_i, idx_j, board)

            for new_move in new_moves:
                moves.append(new_move)
        else:
            print("not valid play")


def next_open_cell(i, j, board):
    for idx_i in range(i, len(board)):
        for idx_j in range(0, len(board[0])):
            if board[idx_i][idx_j] == 0:
                return idx_i, idx_j

    return 0, 0


def possibilities_into_children_moves(possibilities, i, j, board):
    moves = []
    board = [row[:] for row in board]  # shallow copy

    for idx_poss in reversed(range(len(possibilities[i][j]))):
        moves.append([i, j, idx_poss, board])

    return moves


def update_possibilities(value, i, j, possibilities):
    print("updating possibilities based on play of", value, "at i, j:", i, j)

    # frozen_possibilities = [row[:] for row in possibilities]
    # frozen_board = [row[:] for row in board]

    # handle same square
    for idx, row in enumerate(possibilities):
        if 0 <= i < 3:
            box_i = 0
        elif 3 <= i < 6:
            box_i = 1
        else:
            box_i = 2

        if 0 <= j < 3:
            box_j = 0
        elif 3 <= j < 6:
            box_j = 1
        else:
            box_j = 2

        for i_res in range(3):
            for j_res in range(3):
                if value in possibilities[box_i * 3 + i_res][box_j * 3 + j_res]:
                    possibilities[box_i * 3 + i_res][box_j * 3 + j_res].remove(value)

        # eliminate possibilities from same row
        if idx == i:
            for col_idx, cell in enumerate(row):
                if value in cell:
                    cell.remove(value)

                # eliminate possibilities from same column
        if value in row[j]:
            row[j].remove(value)

    possibilities[i][j] = [value]

    return possibilities


def is_valid(value, i, j, board):
    # check in 3x3 square
    for idx, row in enumerate(board):
        if 0 <= i < 3:
            box_i = 0
        elif 3 <= i < 6:
            box_i = 1
        else:
            box_i = 2

        if 0 <= j < 3:
            box_j = 0
        elif 3 <= j < 6:
            box_j = 1
        else:
            box_j = 2

        for i_res in range(3):
            for j_res in range(3):
                if value == board[box_i * 3 + i_res][box_j * 3 + j_res] and (box_i * 3 + i_res != i or box_j * 3 + j_res != j):
                    return False

        # check same row
        if idx == i:
            for col_idx in range(len(row)):
                if value == board[i][col_idx] and col_idx != j:
                    return False

        # check same column
        if value == board[idx][j] and idx != i:
            return False

    return True


