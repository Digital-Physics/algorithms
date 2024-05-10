from typing import List, Union

NestedList = Union[int, List[int], "NestedList"]

def depth_sum(nested_list: NestedList) -> int:
    """
    sum(int * nested_depth)
    """
    total = 0

    def helper(curr_list, depth):
        nonlocal total
        for item in curr_list:
            if isinstance(item, int):
                total += item * depth
            elif isinstance(item, list): # more explicit but equivalent to a catch-all "else"
                helper(item, depth + 1)

    helper(nested_list, 1)

    return total

if __name__ == "__main__":
    print(depth_sum([1, 2, [3, [4]], 5]))