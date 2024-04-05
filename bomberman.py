from typing import List
# from collections import OrderedDict

# future research: i wanted to memoize steps which are m*n nested array so I could see if a repeating pattern would start forming. 
# i realized lists are mutable, so i needed a key that was immutable, like a tuple or str. 
# with the dictionary of previous states, I thought, we might actually want an OrderedDict so if we see a state again, 
# we can conclude it depended on any or all of the previous steps/keys in the dictionary. 
# we don't assume that the previous state alone determines the next state, but that there is some logic that can be applied on a subset of the previous states to predict the future.
# the idea would be to have an algorithm figure out how to represent the relative states and find the pattern, like how a human would come up with the code below. 
# so in the case of bomberman, the goal would be to figure out that after a certain point n >= 3, 
# the state of the system for computing the next step could just depend on the last two steps.

def bomberMan(n: int, grid: List[str]) -> List[str]:
    # main helper nested function
    def explode_bombs_from_t_minus_2_on_t_minus_1(grid):
        """bombs planted t-3, that survived explosions at t-2 = ending grid of bombs at t-2 
        (all bombs remaining at t-2 grid are of the same age (1 at that point and 3 on this next step)).
        so explode those bombs on step t-1, a fully filled grid with bombs."""
        rows = len(grid)
        cols = len(grid[0])
        t_minus_1_grid = [["O" for _ in range(cols)] for _ in range(rows)]

        # print(n, "in")
        # print(grid)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "O": # grid from step t-2 passed in
                    print("bomb to explode, along with range-checked neighbors")
                    t_minus_1_grid[i][j] = "."
                    t_minus_1_grid[min(i+1, rows - 1)][j] = "."
                    t_minus_1_grid[max(i-1, 0)][j] = "."
                    t_minus_1_grid[i][min(j+1, cols - 1)] = "."
                    t_minus_1_grid[i][max(j-1, 0)] = "."
        
        # print("out")
        # print(t_minus_1_grid)
        
        return ["".join(row) for row in t_minus_1_grid]

    # grid is the initialization, n is the steps in a Cellular Automaton kind of update but with timers
    
    if n < 2:
        return grid
    elif n % 2 == 0:
        return ["O"*len(grid[0])]*len(grid)
    elif n % 4 == 3:
        # return step 3 after you create it from step 1 (which is step 0, initialized grid)
        # 3 is first explosion. then 5, which has a different type. then 7 which has the same pattern afterwards as 3
        return explode_bombs_from_t_minus_2_on_t_minus_1(grid) # grid is from t-2
    elif n % 4 == 1:
        # return step 5 after you create it from step 3 (which we showed how to create above)
        grid = explode_bombs_from_t_minus_2_on_t_minus_1(grid)
        return explode_bombs_from_t_minus_2_on_t_minus_1(grid)
    else:
        print("something went wrong in our logic")


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
    print(f"{result=}")

    # fptr.write('\n'.join(result))
    # fptr.write('\n')

    # fptr.close()