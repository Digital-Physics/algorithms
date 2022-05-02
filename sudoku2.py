# thanks Computerphile and Prof. Thorsten Altenkirch

class Sudoku_solver:
    def __init__(self, grid):
        self.grid = grid
        self.solution = None

    def solve(self):
        print(self.grid)
        for y in range(9):
            for x in range(9):
                print("look at cell", y, x)
                if self.grid[y][x] == 0:
                    for n in range(1,10):
                        print(f"try {n} in row,col: {y},{x}")
                        if self.is_valid(y,x,n):
                            print("it works. use it.")
                            self.grid[y][x] = n
                            print("We now just need to solve the same but smaller problem. Recursive call to solve().")
                            self.solve()
                            print("Dead end. solve() didn't kick off another solve() or get to the end. Our assumption was wrong.")
                            print("Backtrack. Set our cell back to 0. Continue our for loop search until those possibilities run out.")
                            self.grid[y][x] = 0
                    return  # return (with nothing) to the for loop that called us
        print("save solution (because we essential assume it is wrong and backtrack because solve() wasn't kicked off again.")
        print("at the end, we will output the last saved solution out of all possibilities")
        self.solution = [row[:] for row in self.grid]

    def is_valid(self, y, x, n):
        for i in range(9): # check cols
            if self.grid[y][i] == n:
                print('1')
                return False

        for i in range(9): # check rows
            if self.grid[i][x] == n:
                print('2')
                return False

        x_start = (x//3)*3  # 012345678 => 000333666
        y_start = (y//3)*3

        for i in range(3):
            for j in range(3):
                if self.grid[y_start+i][x_start+j] == n:
                    print('3')
                    return False

        return True

grid = [
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

solver = Sudoku_solver(grid)
solver.solve()
print(solver.solution)