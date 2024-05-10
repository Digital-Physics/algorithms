from typing import List
from collections import defaultdict
from sortedcontainers import SortedDict # keys maintained in sorted order

def getSecondsElapsed2(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    """calculate total time to tunnel time of K"""

    # starting and ending tunnel points will get sorted in the same order based on the fact that tunnels on this circular track don't overlap
    # but we can get a tunnel_time_to_total_time for residual distances in linear (in C) time, not O(n*log(n))
    tunnel_at_previous_unit = [0] * C  # will look like this eventually: [0, 0, 1, 1, 0, 0, 0, 1, 0, 0]

    # linear time population of tunnels unsorted tunnel starting (and ending) positions
    for current_tunnel_idx in range(len(A)):
        for i in range(A[current_tunnel_idx] + 1, B[current_tunnel_idx] + 1):
            tunnel_at_previous_unit[i] = 1

    # linear: 
    # sort of like a CDF... but a dictionary... and not on probabilities... so more like a monotonically increasing histogram... a prefix sum, a cumulative sum...
    tunnel_time_to_total_time = dict()  # for residual units (e.g. 1: 2, 2: 3)
    cumulative_sum = 0
    for i in range(C):
        cumulative_sum += tunnel_at_previous_unit[i]
        if tunnel_at_previous_unit[i] == 1:
            # [0, 0, 1, 2, 2, 2, 2, 3, 3, 3]
            tunnel_time_to_total_time[cumulative_sum] = i

    # quotient and remainder
    loops = K // cumulative_sum  # when evaluated, cumulative_sum == total tunnel time
    residual_tunnel_units = K % cumulative_sum

    return loops * C + tunnel_time_to_total_time[residual_tunnel_units]


def getSecondsElapsed(C: int, N: int, A: List[int], B: List[int], K: int) -> int:
    """calculate total time to tunnel time of K"""
    tunnel_units_in_loop = sum([b - a for a, b in zip(A, B)])

    sorted_tunnels = SortedDict({A[i]: B[i] for i in range(len(A))}) # sorted by key, which is helpful since our tunnels aren't ordered to begin with

    # quotient and remainder
    loops = K // tunnel_units_in_loop
    residual_tunnel_units = K % tunnel_units_in_loop

    if residual_tunnel_units == 0:
        loops = loops - 1
        residual_tunnel_units = tunnel_units_in_loop
    
    print(loops, residual_tunnel_units)

    # for residual tunnel units
    cumulative_total_meters = 0

    for k, v in sorted_tunnels.items():
        if residual_tunnel_units > (v - k):
            cumulative_total_meters += (v - cumulative_total_meters)
            residual_tunnel_units -= (v - k)
        elif 0 < residual_tunnel_units <= (v - k):
            cumulative_total_meters += (k - cumulative_total_meters) + residual_tunnel_units 
            break

    return loops * C + cumulative_total_meters

if __name__ == "__main__":
    print(getSecondsElapsed(10, 2, [1, 6], [3, 7], 7))
    print(getSecondsElapsed(50, 3, [39, 19, 28], [49, 27, 35], 15))
    print(getSecondsElapsed(50, 3, [39, 19, 28], [49, 27, 35], 25))
    print(getSecondsElapsed(50, 3, [39, 19, 28], [49, 27, 35], 26))