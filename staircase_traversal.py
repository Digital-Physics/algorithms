# time: O(k*n) = O(n) each idx representing ways to make that staircase length n goes through constant k max_steps below it
# space: O(n) for array of ways we build up
def staircaseTraversal(height, maxSteps):
    possibilities = [0 for _ in range(height + 1)]
    possibilities[0] = 1  # one way to do a no-step staircase

    idx = 1

    while idx < len(possibilities):
        counter = 0
        print()
        print(possibilities)

        for i in range(idx - maxSteps, idx):
            print("check possibilities for", idx)
            print("considering possiblities of", i, "was", possibilities[i])
            # if idx - idx_for_diff <= maxSteps:
            print("we could just count the number of ways to make", i, "and add a step of", idx - i, "to all those possibilities")
            # just add one step of size n (< maxSteps) on to all those possibilites
            counter += possibilities[i]

        possibilities[idx] = counter

        idx += 1

    print("end state:", possibilities)
    return possibilities[-1]


# first way:
# time: O(n**2)? each idx representing ways to make that staircase length goes through all ways below it
# space: O(n) for array of ways we build up
def staircaseTraversal2(height, maxSteps):
    possibilities = [0 for _ in range(height + 1)]
    possibilities[0] = 1  # one way to do a no-step staircase

    idx = 1

    while idx < len(possibilities):
        counter = 0
        idx_for_diff = 0
        print()
        print(possibilities)

        while idx > idx_for_diff:
            print("check possibilities for", idx)
            print("considering possiblities of", idx_for_diff, "was", possibilities[idx_for_diff])
            if idx - idx_for_diff <= maxSteps:
                print("we could just count the number of ways to make", idx_for_diff, "and add a step of", idx - idx_for_diff,
                      "to all those possibilities")
                # just add one step of size n (< maxSteps) on to all those possibilites
                counter += possibilities[idx_for_diff]
            idx_for_diff += 1

        possibilities[idx] = counter

        idx += 1

    print("end state:", possibilities)
    return possibilities[-1]