from typing import List 
import math

def getMinimumCost(k: int, c: List[int]) -> int:
    """calc min cost, with multiplier consideration for people
    of size k purchasing more than 1 flower out of c list of flowers."""

    c = sorted(c)

    if len(c) <= k:
        # purchase one of each at the original cost
        return sum(c)
    else:
        cost_total = 0
        # 9/3 = 3 - 1 rounds; 10/3 = 4 - 1 = 3 rounds. factors: 1, 2, 3, 4
        multiplier_rounds = math.ceil(len(c)/k) - 1
        last_round = len(c) % k if len(c) % k != 0 else k

        # multiplier rounds and one non-multiplier round
        for i in range(1, multiplier_rounds + 1):
            start = -i*k
            end = -(i-1)*k

            if end == 0:
                cost_total += sum(c[start:])*i
            else:
                cost_total += sum(c[start:end])*i
        
        # big multiplier round
        cost_total += sum(c[:last_round])*(multiplier_rounds + 1)
    
    return cost_total

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)
    print(minimumCost)

    # fptr.write(str(minimumCost) + '\n')

    # fptr.close()