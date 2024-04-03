if __name__ == '__main__':
    list_of_lists = []
    # unique_values = set()
    lowest_value = float("inf")

    for _ in range(int(input())):
        name = input()
        score = float(input())
        if score < lowest_value:
            lowest_value = score
        # we are asked to store the [name, score]s in a nested list
        list_of_lists.append([name, score])

    lowest_removed = [l for l in list_of_lists if l[1] != lowest_value] # including ties
    min_value_now = min([row[1] for row in lowest_removed])
    print(*sorted([row[0] for row in lowest_removed if row[1] == min_value_now]),sep="\n")
