from typing import List

def twoPluses(grid: List[str]) -> int:
    """find two largest pluses on good cells and take (maximum?) product.
    they can't overlap, which will make this hard even if you save a plus size for each (i, j)
    this might not have an elegant solution... skipping for now"""
    seen = set() # (i, j)

    # sizes = 1, 5, 9, 13...
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            if grid[i][j] == "G":
                pass



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = twoPluses(grid)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()