from typing import List
from collections import defaultdict
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int: 
    """Two Rotary locks of size N. Count spin units needed to enter code C of length M."""
    # key: (rotary lower num, rotary higher num), value: seconds to get to this state
    
    # starting state node
    state_dictionary = defaultdict(lambda: float("inf")) # defaultdict not needed here, but it's used to prime the brain for the main implementation
    state_dictionary[(1, 1)] = 0 # (low rotary value, high rotary value): total cost so far
    step = 0
    print(state_dictionary)

    while step < M:
        # some nodes/states will be pruned when inserted and the key/state/node already exists
        # defaults to infinity so we can compare current value and candidate value (whether key is in dict or not) 
        next_state_dictionary = defaultdict(lambda: float("inf")) 

        for k, v in state_dictionary.items():
            l_num, h_num = k
            total_cost = v
            target_num = C[step]

            # spin low rotary lock to number
            # we either get the normal distance, or we go through 0/N
            cost = min(abs(target_num - l_num), l_num + N - target_num)
            l_num_temp = target_num

            if l_num_temp < h_num:
                next_state_dictionary[(l_num_temp, h_num)] = min(cost + total_cost, next_state_dictionary[(l_num_temp, h_num)])
            else:
                next_state_dictionary[(h_num, l_num_temp)] = min(cost + total_cost, next_state_dictionary[(h_num, l_num_temp)])

            # spin high rotary lock to number
            cost = min(abs(target_num - h_num), h_num + N - target_num)
            h_num_temp = target_num

            if h_num_temp < l_num:
                next_state_dictionary[(h_num_temp, l_num)] = min(cost + total_cost, next_state_dictionary[(h_num_temp, l_num)])
            else:
                next_state_dictionary[(l_num, h_num_temp)] = min(cost + total_cost, next_state_dictionary[(l_num, h_num_temp)])

        state_dictionary = next_state_dictionary
        print(state_dictionary)
        step += 1

    return min(state_dictionary.values())

if __name__ == "__main__":
    print(getMinCodeEntryTime(10, 4, [9, 4, 4, 8]))
    print(getMinCodeEntryTime(10, 4, [9, 5, 5, 8]))