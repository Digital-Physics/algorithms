from typing import List

def trap(height: List[int]) -> int:
    """find the amount of rain water that will pool if we have walls
    of heights given. you can assume heights[-1] = height[n] = 0"""

    curr_left_max = 0
    curr_right_max = 0
    
    max_to_left = []

    for i in range(len(height)):
        max_to_left.append(curr_left_max)
        curr_left_max = max(curr_left_max, height[i])
    
    max_to_right = []

    for i in range(len(height) -1, -1, -1):
        max_to_right.append(curr_right_max)
        curr_right_max = max(curr_right_max, height[i])
    
    max_to_right.reverse()

    print([max(min(max_to_left[i], max_to_right[i]) - height[i], 0) for i in range(len(height))]) 

    return sum([max(min(max_to_left[i], max_to_right[i]) - height[i], 0) for i in range(len(height))])    

if __name__ == "__main__":
    print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))