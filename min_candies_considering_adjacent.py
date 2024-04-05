from typing import List

def candies(n: int, arr: List[int]) -> int:
    """sum of candies. min candy is 1. 
    adjacent scores ordinal relationship must be mirrored in candy count.
    there is some symmetry here, but we process in once, from left to right, not right to left.
    our algorithm doesn't really leverage the symmetry. a more straight forward approach is
    pass in order and increase +1 if current greater than previous, then pass is reverse doing the same """
    previous_score = float("inf")
    candy_level = 0
    total_candies = 0
    students_since_last_peak = 0
    last_peak_val = float("inf")

    for score in arr:
        if previous_score > score:  # going down 
            students_since_last_peak += 1
            candy_level = 1 # reset
            total_candies += students_since_last_peak 
            if students_since_last_peak >= last_peak_val:
                total_candies += 1
                # print("plus 1")
            # print(students_since_last_peak)
            # this is like adding a candy for each of the students since last peak (but in reverse)
            #   0        0                  0 
            #  00   =>  000  in reality    00 0
            # 0000     00000              00000
        elif previous_score < score:  # going up
            students_since_last_peak = 0
            candy_level += 1
            last_peak_val = candy_level
            total_candies += candy_level
            # print(candy_level)
        else: # plateau
            students_since_last_peak = 0
            candy_level = 1  # reset
            last_peak_val = candy_level
            total_candies += candy_level
            # print(candy_level)

        previous_score = score

    return total_candies


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')   

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()