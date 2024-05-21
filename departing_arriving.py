from typing import List
from bisect import bisect_left


def lowest_cost(d: List[int], r: List[int]) -> int:
    """calc the lowest cost of a roundtrip flight. inputs are lists that represent the cost to fly on that day.
    this is the max of an upper triangular matrix, with return_flight_idx/cols >= departure_day/rows, which would take O(n**2). 
    
    we'll do it in O(n*log(n)) by having an ordered departure list (O(n*log(n)) step)
    that we'll only have to iterate through once over an outer for loop (O(n) step)
    """

    # O(n*log(n))
    return_flights = sorted([(i, v) for i, v in enumerate(r)], key=(lambda x: x[1]))

    best = float("inf")
    j = 0 # pointer to ordered return flights still available

    for i in range(len(d)):
        while return_flights[j][0] < i: 
            j += 1
        
        if d[i] + return_flights[j][1] < best:
            best = d[i] + return_flights[j][1]

    return best


if __name__ == "__main__":
    print(lowest_cost([20, 12, 8, 23, 11], [10, 12, 8, 2, 11]))







