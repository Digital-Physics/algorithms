from typing import List

def findBuildings(heights: List[int]) -> List[int]:
    """return indices of buildings that have an ocean view, where the ocean is to the right.
    we'll start on the right and move to the left, therefore we'll know the max at that point."""
    max_height = 0
    output = [] # will be reversed

    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > max_height:
            output.append(i)
            max_height = heights[i]

    return output[::-1]