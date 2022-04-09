# time: O(nlogn) to sort
# space: O(n) space
def taskAssignment(k, tasks):
    # load balancing
    # sort and then pair up back and front
    # track original idx while sorting
    tasks_sort = [(i, tasks[i]) for i in range(len(tasks))]
    tasks_sort.sort(key=lambda x: x[1])
    print(tasks_sort)
    l_idx = 0
    r_idx = len(tasks) - 1
    output_array = []

    while l_idx < r_idx:
        output_array.append([tasks_sort[l_idx][0], tasks_sort[r_idx][0]])
        l_idx += 1
        r_idx -= 1

    return output_array