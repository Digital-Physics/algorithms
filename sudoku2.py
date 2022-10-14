# thanks Computerphile and Prof. Thorsten Altenkirch
print("think: ~DFS growing odometer (w/ faster numbers on right). can you grow it to length m*n through repeated is_valid guesses?")
print("once you exhaust all possibilities at one length, backtrack, roll your odometer, and keep searching")


class SudokuSolver:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.solution = None

    def solve(self) -> None:
        print(self.grid)
        for row in range(9):
            for col in range(9):
                print("look at cell to see if it's blank/0", row, col)
                if self.grid[row][col] == 0:
                    for n in range(1, 10):
                        print(f"try {n} in row,col: {row},{col}")
                        if self.is_valid(row, col, n):
                            print("it's a valid move. use it.")
                            self.grid[row][col] = n
                            print("We have updated a value in the sudoku matrix we are for looping over to find first blank cell")
                            print("We now just need to start at the beginning of that loop. Recursive call to solve().")
                            print("It's the same problem to solve, but smaller. we are now one step closer to finding a solution")
                            self.solve()
                    print("Dead end. solve() didn't kick off another solve() (or if got out of for loop to the end/solution).")
                    print("=> Our assumption was wrong.")
                    print(f"we exhausted all 9 possibilities for cell {row, col}")
                    print("Backtrack. Set cell back to 0 & increment the last move that lead to dead end. The growing odometer turns over")
                    print("The odometer shrinks for only a moment when cell set to 0, assuming only one num turns over (not followed by 9)")
                    print("After the 'return', we'll continue where our for loop left off, one solve() level up")
                    print("our flattened-sudoku-odometer analogy is also like looking through a dictionary in order")
                    print("we check solutions 7, 8, 1, everything else, before we check solutions starting with 7, 8, 2, ...")
                    self.grid[row][col] = 0
                    print("now we pick up at where the solve()'s for loop was one nested level up, before we called a dead end solve()")
                    return
        print("we got through our for loop so we must be to the end and found a valid solution")
        print("save solution (we essential assume the first sudoku solution is wrong and let the outer solve()s keep going")
        print("at the end, we will output the last saved sudoku solution out of all possibilities")
        self.solution = [row[:] for row in self.grid]
        print("a solution:", self.solution)
        print("last recursive solve() call is popped off the stack and we go up a level to previous solve()")

    def is_valid(self, y: int, x: int, n: int) -> bool:
        for i in range(9):  # check cols
            if self.grid[y][i] == n:
                print('issue #1: col has number n already')
                return False

        for i in range(9):  # check rows
            if self.grid[i][x] == n:
                print('issue #2: row has number n already')
                return False

        x_start = (x//3)*3  # 012345678 => 000333666
        y_start = (y//3)*3

        for i in range(3):
            for j in range(3):
                if self.grid[y_start+i][x_start+j] == n:
                    print('issue #3: 1/3 by 1/3 box has n already')
                    return False

        return True


test_grid = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
  ]

solver = SudokuSolver(test_grid)
solver.solve()
print(solver.solution)
