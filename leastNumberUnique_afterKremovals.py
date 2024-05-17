from collections import Counter
import heapq  # performs heapify(list) and heappop(list) in place on list object
from typing import List

def findLeastNumOfUniqueInts(arr: List[int], k: int) -> int:
    """prioritize removing the least common elements w/ the k removals you have available,
    and what's left is the least number of unique integers after k removals.
    (wort case) time: O(n*log(unique_elements)); space: O(unique_elements)
    
    if k is small, this heap algorithm runs a little quicker than sorting in n*log(n) (vs n + k*log(n))"""
    counter_dict = Counter(arr)
    min_heap_counts = list(counter_dict.values())

    print("before list is sifted up in heapify:", min_heap_counts)
    heapq.heapify(min_heap_counts) # this will heapify in place in O(n) time, instead of sorting in O(n*log(n)) time, although our time complexity won't change
    print("Can you verify this is a min heap? Does it obey the counts[i] < counts[2i + 1] and counts[2i + 2] rule?", min_heap_counts)

    while k > 0:
        # it is not a method on a heap object, but rather a function run on a list with the heap property.
        print(min_heap_counts, type(min_heap_counts), id(min_heap_counts))
        k -= heapq.heappop(min_heap_counts) # note: w/ heappop (unlike .pop() or .popleft() ), we take in the list/heap as the argument. 
        
    # if removing the last kind of element took the counts past the number k of removals we had allocated, we have to add it back in w/ +1
    return len(min_heap_counts) + 1 if k < 0 else len(min_heap_counts) 

if __name__ == "__main__":
    print(findLeastNumOfUniqueInts(arr = [4,3,1,1,3,3,2], k = 3))

    print("a normal list can also reduce in size and be mutated in place (in linear time)")
    normal_list = [1, 2, 3]
    print("normal list", normal_list, type(normal_list), id(normal_list))
    normal_list.pop(0)
    print("normal list", normal_list, type(normal_list), id(normal_list))