# time complexity: O(test_cases*len_test_case)
# space complexity: O(test_cases*len_test_case), but in theory this could be made O(len_test_case) if take them in one at a time.

from collections import deque

test_cases = int(input())
list_of_lists = []
for test_case in range(test_cases):
    _ = input()
    list_of_lists.append([int(string) for string in input().split(" ")])   

def check_list(l):
    deq = deque(l)
    last_cube = float("inf")

    while deq:
        # print(deq)

        if deq[-1] <= deq[0] <= last_cube:
            last_cube = deq.popleft()
        elif deq[0] <= deq[-1] <= last_cube:
            last_cube = deq.pop()
        else:
            print("No")
            return
    
    print("Yes")

for l in list_of_lists:
    check_list(l)
    

    



