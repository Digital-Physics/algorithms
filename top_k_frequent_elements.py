# counter.most_common(k)
from collections import Counter
from typing import List

def most_common(arr: List[int], k: int) -> List[int]:
    """
    return the k most common integers.
    we will take advantage of the fact that counts will only range from 0 to len(arr).
    Note: if we were asking for kth largest element in an array, we'd have values that ranged from max(arr)-min(arr) >= len(arr),
    so it'd be linear (and cleaner than quick select), but linear in something larger than the list length. 
    Here, this isn't an issue because our count buckets will be of len(arr).
    Note2: we don't need the top k to be in order according to frequency.
    """
    counter_dict = Counter(arr) # linear time; we could do this from scratch with a dict/defaultdict if you wanted

    count_bucket = [[] for _ in range(len(arr) + 1)] # we use +1 so we can have the index match the count; we don't want count_bucket[3] to be out of range like for [4, 4, 4]

    for key, val in counter_dict.items(): # linear time (in the length of unique items in array); careful: don't redefine k here when you unpack keys and values (i.e. k, v) or you'll screw things up
        count_bucket[val].append(key)
    
    output = []
    j = len(count_bucket) - 1

    while len(output) < k:
        output.extend(count_bucket[j])
        j -= 1

    print(count_bucket)
    return output

if __name__ == "__main__":
    print(most_common([1,1,1,2,2,3], 2))
