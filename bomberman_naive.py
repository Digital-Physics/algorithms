from typing import List

def bomberMan(n: int, grid: List[str]) -> List[str]:
    # grid is the initialization, n is the steps in a Cellular Automaton kind of update but with timers
    rows = len(grid)
    cols = len(grid[0])
    counter_matrix = [[0 for _col in range(cols)] for _row in range(rows)]
    grid = [[char for char in row_str] for row_str in grid]
    neighbors = [[0,1], [1,0], [0,-1], [-1,0], [0, 0]]

    for t in range(1, n + 1):    
        print()
        to_blow_up = []

        # we could be more efficient look at bombs planted 3 steps ago, seeing what survived at t-2 = grid at t-2
        # so grid at t-2 are all bombs that are about to go off at t, on a full grid of bombs that were filled in at t-1
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O":
                    counter_matrix[i][j] += 1

                if counter_matrix[i][j] == 3:
                    to_blow_up.append([i, j])

        print("Bombs to blow up at time", t, ":")
        print(to_blow_up)
    
        # blow neighboring bombs up
        for blow_idx in to_blow_up:
            for neighbor in neighbors:
                row, col = blow_idx[0] + neighbor[0], blow_idx[1] + neighbor[1]
                if 0 <= row < rows and 0 <= col < cols:
                    grid[row][col] = "."
                    counter_matrix[row][col] = 0

        if t % 2 == 0 and t != 0:
            print(f"New bombs added for time {t=}, but counter keeps their age.")
            grid = [["O" for _col in range(cols)] for _row in range(rows)]

        print("Grid at time", t, ":") 
        print(grid)
        print("Counter matrix at time", t, ":")
        print(counter_matrix)

    return ["".join(row) for row in grid]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)
    print(result)

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()