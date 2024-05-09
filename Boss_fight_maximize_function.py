from typing import List
from itertools import combinations

def getMaxDamageDealt2(N: int, H: List[int], D: List[int], B: int) -> float:
    """
    There's a word problem of warriors fighting a boss that I actually quite like, but it boils down to
    this formula that you are trying to maximize: (Di + Dj)*Hi/B + Dj(Hj/B).
    Since everything is a positive integer we can ignore the B, leaving us with Di*Hi + Dj*Hj + Dj*Hi.
    The following is a heuristic approach that shouldn't work in all situations because we ignore the interaction term.
    Also, the thing we are trying to maximize can be visualized as a the area of an L shape composed of three rectangles.
    """
    first = (None, float("-inf")) # (idx, val)
    second = (None, float("-inf"))
    
    for i in range(len(H)):
        damage_hours = H[i]*D[i]
        
        if damage_hours > first[1]:
            second = first
            first = (i, damage_hours)
        elif damage_hours > second[1]:
            second = (i, damage_hours)
    
    if H[first[0]] > H[second[0]]:
        i_guy = first[0]
        j_guy = second[0]
    else:
        i_guy = second[0]
        j_guy = first[0]

    return (D[i_guy] + D[j_guy])*H[i_guy]/B + D[j_guy]*H[j_guy]/B


def getMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    """
    brute force
    """
    tuple_choices = combinations(range(N), 2)
    best = float("-inf")

    for i, j in tuple_choices:
        curr = (D[i] + D[j])*H[i]/B + D[j]*H[j]/B
        curr2 = (D[j] + D[i])*H[j]/B + D[i]*H[i]/B

        better = max(curr, curr2)

        if better > best:
            best = better

    return best


def xgetMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    """
    We'd like to avoid trying every combination of two warriors which will be quadratic len(H)*(len(H)-1)
    We can sort them in n*log(n) time. But this approach isn't correct. We'd at least have to look at ties
    when it comes to damage-hours. But even then, it doesn't work. This code is being kept here in case I pick
    it back up.
    """

    candidate_list = sorted(zip(H, D), key=lambda x: x[1][0]*x[1][1], reverse=True) # Note: we don't bring along index

    best = float("-inf")

    for i in range(len(candidate_list) - 1):
        # consider the first two
        if candidate_list[i][0] > candidate_list[i+1][0]:
            i_guy = i
            j_guy = i + 1
        else:
            i_guy = i + 1
            j_guy = i

        curr = (D[i_guy] + D[j_guy])*H[i_guy]/B + D[j_guy]*H[j_guy]/B

        if curr > best:
            best = curr
    
    return best


def XgetMaxDamageDealt(N: int, H: List[int], D: List[int], B: int) -> float:
    """wrong approach"""
    if H[0] > H[1]:
        i_guy = 0
        j_guy = 1
    else:
        i_guy = 1
        j_guy = 0
    
    # area of first two
    area = (D[i_guy] + D[j_guy])*H[i_guy]/B + D[j_guy]*H[j_guy]/B

    for i in range(2, len(H)):
        if (D[i] + D[j_guy])*H[i]/B + D[j_guy]*H[j_guy]/B > area:
            if (D[i_guy] + D[i])*H[i_guy]/B + D[i]*H[i]/B > (D[i] + D[j_guy])*H[i]/B + D[j_guy]*H[j_guy]/B:
                area = (D[i_guy] + D[i])*H[i_guy]/B + D[i]*H[i]/B
                j_guy = i
            else:
                area = (D[i] + D[j_guy])*H[i]/B + D[j_guy]*H[j_guy]/B 
                i_guy = i
    
    return area



if __name__ == "__main__":
    print(getMaxDamageDealt(4, [1, 1, 2, 100], [1, 2, 1, 3], 8))
