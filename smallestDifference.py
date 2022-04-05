# time: O((m+n)log(m+n)); Clement's: O(mlogm + nlogn)
# space: would have been O(1) since we sort arrays in place,
# ... but actually O(n+m) because we unnecessarily merged our lists :(
def smallestDifference(arrayOne, arrayTwo):
    # sort lists into one while keeping original list info in tuple of (num, array_num)
    # this can be done in (m+n)log(m+n) in one step by constructing a BST
    # but I will just concatenate in m+n and then sort in nlogn
    # Clement's solution didn't merge but has the same complexity
    # His two indicies (in two arrays) also moved only to the right, just like our for loop
    merged_lists = [(1, num) for num in arrayOne] + [(2, num) for num in arrayTwo]
    merged_lists.sort(key=lambda i: i[1])

    best_dist = abs(merged_lists[0][1]) + abs(merged_lists[-1][1])

    # then sweep through sorted list in n times looking at adjacent
    for i in range(1, len(merged_lists)):
        if merged_lists[i][0] != merged_lists[i - 1][0]:
            if merged_lists[i][1] - merged_lists[i - 1][1] < best_dist:
                best_dist = merged_lists[i][1] - merged_lists[i - 1][1]
                if merged_lists[i][0] == 1:
                    winners = [merged_lists[i][1], merged_lists[i - 1][1]]
                else:
                    winners = [merged_lists[i - 1][1], merged_lists[i][1]]

    return winners
