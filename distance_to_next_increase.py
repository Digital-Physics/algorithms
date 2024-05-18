from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    """return list of days to next higher temp. if none exist, then return 0"""

    output = [0] * len(temperatures) # if the temps never see a warmer day, they'll remain 0
    stack = [] # every index will get pushed/appended to the stack; it's just a question of how long until it's popped.
    # the index on the stack will allow us to look up the temperature and calculate the number of days. 
    

    for day_i, curr_temp in enumerate(temperatures):
        # we won't have to pop beyond the last day that the curr_temp can't beat, because that day's temp should have popped any below it from the stack already
        while stack and temperatures[stack[-1]] < curr_temp:
            day_i_waiting_for_warmer = stack.pop()
            output[day_i_waiting_for_warmer] = day_i - day_i_waiting_for_warmer 

        # the current day will always be waiting at least one day to be popped from the stack.    
        stack.append(day_i)

    return output

if __name__ == "__main__":
    print(dailyTemperatures([70, 68, 64, 62, 72, 72, 60]))
    print(dailyTemperatures([80, 68, 72, 74]))