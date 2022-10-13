def solver(c):
    print()
    print("cells")
    print(c)
    print()

    prev_row = [0]*len(c[0])

    for i in range(len(c)):
        prev_row_freeze = prev_row[:]
        for j in range(len(c[0])):
            prev_row[j] = max([c[i][j] + prev_row_freeze[k] - abs(j-k) for k in range(len(c[0]))])
        print(prev_row)

    return max(prev_row)


def solver2(c):
    print()
    print("cells")
    print(c)
    print()

    prev_row = [0]*len(c[0])

    for i in range(len(c)):
        prev_row_freeze = prev_row[:]
        prev_row = [max([c[i][j] + prev_row_freeze[k] - abs(j-k) for k in range(len(c[0]))]) for j in range(len(c[0]))]
        print(prev_row)

    return max(prev_row)


solver([[2,8,3],[100,4,9],[8,8,12]])
solver2([[2,8,3],[100,4,9],[8,8,12]])