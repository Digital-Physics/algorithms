from typing import List

def getWays(n: int, c: List[int]) -> int:
    number_of_ways = [0 for _ in range(n + 1)]
    number_of_ways[0] = 1  # number of ways to make no change

    # print("note: you can't do the for loops the opposite way. you must add coins one at a time to use this formula.")
    for coin in c:
        for check_idx in range(1, n + 1):
            if coin <= check_idx:
                # keep the ways we've made each target amount without using the coin
                # and add the new way with using the coin
                number_of_ways[check_idx] += number_of_ways[check_idx - coin]

    return number_of_ways[n]


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)

    # fptr.write(str(ways) + '\n')

    # fptr.close()