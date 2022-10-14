# thanks Computerphile and Prof. Thorsten Altenkirch
print("think DFS growing odometer (w/ faster numbers on right) password attempts")
print("once you exhaust all possibilities, backtrack and turn that back")


class SudokuSolver:
    def __init__(self, grid: list[list[int]]) -> None:
        self.grid = grid
        self.solution = None

    def solve(self) -> None:
        print(self.grid)
        for row in range(9):
            for col in range(9):
                print("look at cell", row, col)
                if self.grid[row][col] == 0:
                    for n in range(1, 10):
                        print(f"try {n} in row,col: {row},{col}")
                        if self.is_valid(row, col, n):
                            print("it works. use it.")
                            self.grid[row][col] = n
                            print("We now just need to solve the same but smaller problem. Recursive call to solve().")
                            self.solve()
                            print("Dead end. solve() didn't kick off another solve() or get to the end. Our assumption was wrong.")
                            print("Backtrack. Erase speculations we kow are wrong now. Set cell back to 0.")
                            print("Continue our for loop search until those possibilities run out.")
                            print("the for loop keeps increasing our flattened-sudoku-odometer-solution...")
                            print("and we've check all shorter & lower numbers already.")
                            self.grid[row][col] = 0
                    print("now we pick up after the recursive solve() call didn't find a solution")
                    return
        print("save solution (we essential assume the first sudoku solution is wrong and backtrack; solve() wasn't kicked off again.)")
        print("at the end, we will output the last saved sudoku solution out of all possibilities")
        self.solution = [row[:] for row in self.grid]

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
