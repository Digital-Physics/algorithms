from collections import Counter
import heapq

def reorganizeString(s: str) -> str:
    """construct the reorganized chars such that no adjacent chars are the same.
    if we didn't use a max_heap, we'd have to store the counts in a dictionary, 
    and we'd need linear time to figure out which was the max count character remaining... 
    unless we used a SortedDict with the key being the count, and the value being a list of chars... hmmm
    
    but here we do the following:
    counter dict in linear time
    get the (-count, char) in linear time
    heapify in linear time
    heappop in 2*log(unique_chars)
    heappush in 2*log(unique_chars)"""
    char_to_count = Counter(s)
    
    # heapq does a min heap by default, so we need to make count negative
    # a list of tuples will be heapify'd based on the first element in the tuple, then the next (which is the character), just how .sort() and sorted() can have key=lambda tup: tup
    # having the heap sort by the character as a second consideration is actually important because when there is a tie in count, we don't want the second largest in one round to be the first largest in the next
    # consider: {"a": 6, "c": 6, d: "5"} => [a,c] & {"a": 5, "c": 5, d: "5"} => [a, c, c, d] or [a, c, c, a] if the letters weren't take into account
    max_heap = [(-count, char) for char, count in char_to_count.items()] # which is just a list that obeys the max_heap[i][0] < max_heap[2i + 1][0] and max_heap[i][0] < max_heap[2i + 2][0] rule
    heapq.heapify(max_heap)
    
    output = []
    
    while len(max_heap) >= 2:
        count1, char1 = heapq.heappop(max_heap)
        count2, char2 = heapq.heappop(max_heap)
        
        output.extend([char1, char2])
        
        # we are dealing with negatives (because we need a max heap), so we are reducing the count in some sense and putting it back on the stack
        if count1 + 1 < 0: 
            heapq.heappush(max_heap, (count1 + 1, char1))
        if count2 + 1 < 0:
            heapq.heappush(max_heap, (count2 + 1, char2))

    # do we have leftover letters? are their multiple of them?   
    if max_heap: # our max heap is either 1 or 0 in length; this checks to see if it is 1 tuple of (-count, char) left
        count, character = heapq.heappop(max_heap)
        if -count > 1:
            return ""  # this means it is not possible; we have more than one of the same item at the end meaning they'll have to be next to each other
        output.append(character)
        
    return "".join(output)

if __name__ == "__main__":
    print(reorganizeString("aab"))
    print(reorganizeString("aaab"))