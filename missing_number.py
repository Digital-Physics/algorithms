# array of n distinct numbers in the range from 0 to n. One number is missing. find it.
from typing import List

def missing_num(arr: List[int]) -> int:
    set_of_nums = set(range(len(arr) + 1))
    
    for i in range(len(arr)):
        set_of_nums.remove(arr[i])

    return list(set_of_nums)[0]

def missing_num2(arr: List[int]) -> int:
    set_total = sum(range(len(arr) + 1))
    
    return set_total - sum(arr)

if __name__ == "__main__":
    print(missing_num([0, 1, 3]))
    print(missing_num2([0, 1, 3]))
