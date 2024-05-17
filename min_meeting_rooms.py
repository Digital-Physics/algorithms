
from typing import List
import heapq


# all approaches have the same time: O(n*log(n)) and space: O(n)
def minMeetingRooms(intervals: List[List[int]]) -> int:
    """pointers with one counter var that never decrements"""
    if not intervals: # no meetings
        return 0

    start = sorted(intervals, key=lambda x: x[0])
    end = sorted(intervals, key=lambda x: x[1])

    i_s = 0
    i_e = 0

    counter = 0 # increments when we need a new room and we don't have one; doesn't decrement when rooms open but 
    # open room credit is built up in pointer difference

    while i_s < len(intervals):
        if start[i_s][0] >= end[i_e][1]:
            # counter stays the same
            i_e += 1  # get rid of the end time since it ended before the next meeting started
            i_s += 1  # go to the next start time (and we don't need to count)
        else:
            i_s += 1 # go to the next start time (and count the additional room needed)
            counter += 1

    return counter


def minMeetingRooms2(intervals: List[List[int]]) -> int:
    """pointers with a open_room counter that increments and decrements and a most variable too.
    the end pointer can decrement more than once in a round."""
    if not intervals:
        return 0

    start = sorted([interval[0] for interval in intervals])
    end = sorted([interval[1] for interval in intervals])

    i_s = 0
    i_e = 0

    counter = 0 # increments when we need a new room and decrements when one opens up
    most = 0

    while i_s < len(intervals):
        if start[i_s] >= end[i_e]:
            # open up every room
            while end[i_e] < start[i_s]:
                i_e += 1
                counter -= 1

            i_s += 1  # go to the next start time (and we don't need to count)
        else:
            counter += 1

            if counter > most:
                most = counter

            i_s += 1

    return most


def minMeetingRooms3(intervals: List[List[int]]) -> int:
    """min heap to keep track of the next room opening"""
    minHeap = []  

    for start, end in sorted(intervals, key=lambda x: x[0]):
        # There's no overlap, so we can reuse the same room.
        if minHeap and start >= minHeap[0]:
            heapq.heappop(minHeap) # the new meeting gets that room we just popped off
        
        # put the end time on the min heap to potentially pop for another meeting at some point (we can build up early meeting endings to pop off in the future)
        heapq.heappush(minHeap, end) 

    return len(minHeap)

if __name__ == "__main__":
    print(minMeetingRooms([[1, 10], [2, 4], [4, 6], [8, 9], [3, 5]]))
    print(minMeetingRooms2([[1, 10], [2, 4], [4, 6], [8, 9], [3, 5]]))
    print(minMeetingRooms3([[1, 10], [2, 4], [4, 6], [8, 9], [3, 5]]))